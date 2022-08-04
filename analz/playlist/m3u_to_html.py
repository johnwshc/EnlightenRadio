
from pathlib import PurePath


class MTrack:
    """ A class modeling an audio track extracted from an M3U playlist. """
    cols = ['duration', 'artist', 'title', 'file', 'url']
    def __init__(self):

        self.duration = -1
        self.artist = None
        self.title = None
        self.file = None
        self.url = None

    def to_string(self):
        return 'duration:' + str(self.duration) + ', artist: ' + self.artist + \
               ', title: ' + self.title + ', file: ' + str(self.file) + ', url: ' + self.url

    def get_row(self):
        return [self.duration, self.artist, self.title, self.file, self.url]

    # def get_series_row(self):
    #     ser = pd.Series(self.get_row(), index=MTrack.cols)
    #     return ser

    def is_duplicate(self, mtr):
        pass


class M3UList:
    """ A class parsing and modeling the extended m3u playlist file, plus operations
        extracting audio track data; and converting to HTML."""

    # class attributes

    types = ['EXT', 'SIMPLE']
    xf_descriptor = '#EXTM3U'
    xf_rec_marker = '#EXTINF:'
    xf_desc = '#D:'
    sf_comment = '# '
    http_marker = 'http'

    #  static methods

    @staticmethod
    def get_lines(f:str):
        with open(f) as m3u:
            return m3u.readlines()

    @staticmethod
    def get_type(lines: list):
        if lines[0] == M3UList.xf_descriptor:
            return M3UList.types[0]
        else:
            return M3UList.types[1]

    @staticmethod
    def parse_m3ue2(line: str):
        __doc__ = """returns a tuple (path -- relative or absolute [or None if 
            file is in current directory as m3u] ,file)"""

        # print('in parse_m3ue2: ', line)
        if line.startswith('http'):
            return None, line

        else:  # a windows path
            ss = line.split('\\')
            pp = PurePath('\\\\'.join(ss))
            # path = pp.parent
            file = str(pp)
            return None, file

    @staticmethod
    def parse_m3ue1(line: str):
        """ Returns a tuple (duration,title)
            for line one of EXT M3U format. """

        ref, rest = line.split(':', maxsplit=1)
        lss = rest.split(',', maxsplit=1)
        duration = lss[0]
        artist_title = lss[1]
        if ' - ' in artist_title:
            title, artist = lss[1].split(' - ', maxsplit=1)
        else:
            if '.mp3' in artist_title:
                title = '.'.join(artist_title.split('.')[0:-1])
                artist = None
            else:
                title = artist_title
                artist = None
        return duration, artist, title

    @staticmethod
    def parse_m3u_path(line: str):
        __doc__ = ''' From second line in  M#U EXT Format, returns a tuple (path -- 
            relative or absolute [or None if 
            file is in current directory as m3u] ,file or url)'''

        # print('in parse_m3ue2: ', line)
        if line.startswith('http'):
            return None, line

        else:  # a windows path
            ss = line.split('\\')
            pp = PurePath('\\\\'.join(ss))
            # path = pp.parent
            file = str(pp)
            return None, file

    @staticmethod
    def list_2_html(l):

        ll = [ x for x in l if x is not None]
        if len(l) < 1:
            return None
        else:
            return ll

        # return str(List(l))

    # @staticmethod
    # def m3u2htm_file(fin, fout=None, artist=[], name=None):
    #     m3u = M3UList(fin, artists=artist, name=name)
    #     if fout:
    #         with open(fout, 'w+') as f:
    #             f.write(m3u.table_html)
    #     return m3u.to_HTML()

    # Instance methods

    def __init__(self, m3u_fn:str, artists=[], name=None):

        if not m3u_fn:
            print("error: no file name")
            raise Exception("no file name exception")

        self.fn = m3u_fn
        self.lines = M3UList.get_lines(self.fn)
        self.type = M3UList.get_type(self.lines)
        # self.src = 'LOCAL'
        if name is None:
            self.name = self.fn
        else:
            self.name = name

        self.compact_file()

        self.comments = []
        self.mt = None
        self.tracks = self.process_lines()
        self.list_of_trks = [mt.get_row() for mt in self.tracks]
        self.trk_cnt = 0
        # self.df = self.html_from_array()
        self.artists = artists
        if not self.artists:
            self.artists = self.get_artists()
        else:
            self.artists = artists

        # self.table_html = str(self.html_from_array())

    def compact_file(self):

        self.lines = [line for line in self.lines if line != '\n']
        self.lines = [l.strip() for l in self.lines]

    # def to_HTML(self):
    #     """ Return playlist table with artists header as HTML string. """
    #     return '<div><h3> Playlist Artists </h3> <br/>' + str(List(M3UList.list_2_html(self.artists))) \
    #            + '</div> <br/> <div>' + self.table_html + '</div>'

    # def to_html_file(self):
    #     nfn = PurePath(self.fn)
    #     ppp = str(nfn.parent) + '\\' + str(nfn.stem) + '.html'
    #     with open (ppp, mode="w") as f:
    #         f.write(self.to_HTML())

    def get_artists(self):
        """ Return list of artists in playlist. """

        return list(dict.fromkeys([x.artist for x in self.tracks if x.artist]))

    # def html_from_array(self):
    #     list_of_trks = [mt.get_row() for mt in self.tracks]
    #     htbl = Table(rows=list_of_trks, border=2, header_row=MTrack.cols)
    #     return htbl
        
    def process_lines(self):
        """ Parse lines of M3U Track. """
        line_count = 0
        trks = []
        # parse m3u #EXTINF lines, 2 per track

        for line in self.lines:
            if line == '\n' or line.startswith(M3UList.xf_descriptor):
                continue

            # '''{
            #
            #     "title": null,            #
            #     "url": null,            #
            #     "duration": -1,
            #     "artist": null,
            #     "file": null
            #
            #  }   '''

            elif line.startswith(M3UList.xf_rec_marker) and (
                    line_count % 2 == 0):  # line 1 in m3u ext track format.
                self.mt = MTrack()
                self.mt.duration, self.mt.artist, self.mt.title = M3UList.parse_m3ue1(line)
                line_count += 1

            else:  # line 2 in m3u ext track format.
                if (line_count % 2) != 0:
                    (path, file) = self.parse_m3ue2(line)
                    if path is None and file.startswith('http'):
                        self.mt.url = file
                        self.mt.file = None
                    else:
                        if path is not None:
                            self.mt.file = str(path + file)
                            self.mt.url = None
                        else:
                            self.mt.file = file
                            self.mt.f = path
                            self.mt.url = None

                    trks.append(self.mt)
                    line_count += 1
                    self.mt = MTrack()

                else:
                    # if line.startswith('# '):
                    #     self.comments.append(line)
                    # else:
                    print("Do not recognize: " + line)
                    self.mt = MTrack()

                    continue

        return trks




