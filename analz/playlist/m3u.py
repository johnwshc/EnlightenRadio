import requests
from analz.playlist.m3u_to_html import M3UList
from pathlib import Path
from config import Config
import os
from  urllib.parse import unquote, quote
import pandas as pd


class M3U:

    playlist_dir = Config.playlists_dir # default pls directory
    # test files
    test_file_vlc = f"{playlist_dir}\\test_vlc1.m3u"
    test_file = f"{playlist_dir}\\example_1.m3u"
    test_json = f"{Config.playlists_json}\\example_1.json"

    # Google Blogger API keys
    blogger_key = f"{Config.blogger_api_key}"
    blogger_client_id = f"{Config.blogger_client_id}"

    @staticmethod
    def compute_min_sec(secs):
        """convert seconds into string: x mins, x secs"""
        s = secs % 60
        m = int(secs / 60)
        mss = f"{str(m)} mins, {str(s)} secs"
        return mss

    @staticmethod
    def from_json(fn):
        """ json util ... load json file and return python dictionary """
        import json
        with open(fn) as f:
            d = json.load(f)
        return d

    @staticmethod
    def to_json_file(fn, m, gen=[]):
        """ save an M3U object, representing an m3u file, as a json file. """
        import json
        if isinstance(m, M3U):
            with open(fn, "w") as f:
                json.dump(m.to_dict(), f)
            return True
        else:
            raise Exception('error writing file')


    @staticmethod
    def pandas_to_html(htm='static\\playlist.html'):
        """ Read a radioDJ created html playlist output,
        edit fields to 3, input as pandas dataframe, and convert
        to simple html suitable for Blogger. """
        dfs = pd.read_html(htm)
        df = dfs[0]
        df.columns = df.loc[0,]
        dff = df[['Artist', 'Title', 'Duration']].copy()
        dff.drop([0], axis=0, inplace=True)
        dff.reset_index(drop=True, inplace=True)
        return dff.to_html()


    # url as file format default for VLC player
    @staticmethod
    def make_vlc_m3u_playlist(tracks:list):
        """ Return a string text version of an m3u file representing a list of audio tracks.."""
        lines = list()
        lines.append(M3UList.xf_descriptor)

        for t in tracks:
            if isinstance(t, VLC_Track):
                lines.append(t.l1)
                lines.append(t.url)
                # print(f"line 2 of trk: {t.str_win_path}")
            else:
                # print(type(t))
                raise Exception("not a VLC_Track obj")
        return '\n'.join(lines)

    # make a standard non url formatted extended m3u file from VLC_Track objs
    @staticmethod
    def make_std_m3u_playlist(tracks:list):
        """ convert a standard m3u file to a list of Track objects. """
        lines = []
        lines.append(M3UList.xf_descriptor)
        for t in tracks:
            if isinstance(t, VLC_Track):
                lines.append(t.l1)
                lines.append(t.str_win_path)
            else:
                print(type(t))
                raise Exception(" not a VLC_Track obj")

        return '\n'.join(lines)



    @staticmethod
    def convert_vlc_m3u(file=test_file_vlc):
        "converts vlc formatted track addresses to standard. Returns Track objects. "
        # print("in convert: ", file)
        with open(file, encoding='latin-1') as f:
            vlc_lines = [l.strip() for l in f.readlines() if not l.startswith('#RDJDATA')]

        # print(f"xf_descriptor: {M3UList.xf_descriptor}")
        # print(f" vlc_lines[0]: {vlc_lines[0]}")
        if vlc_lines[0] != M3UList.xf_descriptor:
            raise Exception("invalid VLC m3u")
#             compact  lines
        else:

            vlc_info_lines = vlc_lines[1:]
            vlc_info_lines = [l for l in vlc_info_lines if len(l) > 2]

            if len(vlc_info_lines) % 2 == 0:
                l1s = vlc_info_lines[::2]
                l2s = vlc_info_lines[1::2]
                zipped = list(zip(l1s,l2s))
                tracks = [VLC_Track(l1, l2) for (l1, l2) in zipped ]
                return pd.Series(tracks)
            else:
                print(f"lines length in {file} are not mod2, returning None")
                return None

    # @staticmethod  -- not used now
    # def parse_m3u_file(surl=test_file):
    #     furl = surl
    #     print(furl)
    #     # "/home/pawan/Downloads/ru.m3u"
    #     # useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    #     parser = M3uParser()
    #     # parser.parse_m3u(furl)
    #     # parser.remove_by_extension('mp4')
    #     # parser.filter_by('status', 'GOOD')
    #     # print(len(parser.get_list()))
    #     # parser.to_file('test.json')
    #     return parser

    @staticmethod
    def get_m3u_playlists(d=playlist_dir):
        """Retrieve all playlists from the active playlist directory as Playlist objects"""

        files = os.listdir(d)
        plists = [M3U(file_name=f"{d}\\{f}") for f in files]
        # d = {pl.playlist_name: pl for pl in plists}
        return plists

    @staticmethod
    def get_m3u_playlists_from_mongo_list(pls:[]=None):
        """ aggregate M3U objx from a dictionary source. Expects the
        dictionary keys to be names of playlists, which point to a
        dictionary of playlist attributes, including a list of tracks,
        represented also as dictionaries. Dictionaries (persisted as json) are best
         source files for MongoDB collections. """
        lists = []
        for m in pls:

            m3u = M3U(file_name=None, dic=m)
            lists.append(m3u)
        return lists


    # M3U instance constructor and instamce methods ####################################

    def __init__(self, file_name=None, dic:dict=None, trks:dict=None):
        if file_name is not None:  # presumes the source is an m3u file
            self.fn = Path(file_name).as_posix() # file name -- no support for http sources in this object
            print(f" in m3u inir: {self.fn}")
            self.playlist_name = Path(self.fn).stem
            # self.uri = f"/playlist/{self.playlist_name}"
            self.tracks = M3U.convert_vlc_m3u(self.fn)
            self.cols = ['Artist - Title', 'Duration']
            ttrks = [[t.artist_title, t.duration] for t in self.tracks]
            self.df = pd.DataFrame(ttrks, columns=self.cols)
            self.df.Duration = self.df.Duration.apply(M3U.compute_min_sec)
            self.simple_html = self.df.to_html(na_rep='unknown')

            # print(f"file name: {file_name}")
            sumt = 0
            for t in self.tracks:
                sumt  += int(t.duration)
            self.duration = sumt
            tups = [t.genres for t in self.tracks]
            self.genres  = [g for t in tups for g in t]
        elif dic is not None:
            # alternative initialization via a dictionary instead of a file.
            self.json_to_m3u(dic)

        elif trks is not None:
            self.fn = trks['fn']
            self.genres = trks['genres']
            self.duration = trks['duration']
            dtracks = trks['tracks']

            self.tracks = [VLC_Track.from_dict(t) for t in dtracks]
            self.playlist_name = trks['name']
            self.cols = ['Artist - Title', 'Duration']
            ttrks = [[t.artist_title, t.duration] for t in self.tracks]
            self.df = pd.DataFrame(ttrks, columns=self.cols)
            self.df.Duration = self.df.Duration.apply(M3U.compute_min_sec)
            self.simple_html = self.df.to_html(na_rep='unknown')
            sumt = 0
            for t in self.tracks:
                sumt += int(t.duration)
            self.duration = sumt




        else:
            raise Exception("no data")
        if self.duration  and self.duration > 0:
            durs = [t.duration for t in self.tracks]
            serdurs = pd.Series(durs)
            self.max_trk_dur = max(serdurs)
            self.median_trk_dur = serdurs.median()
            self.minimum_trk_dur = serdurs.min()
            # self.hist = Hist(durs)
            self.mean = serdurs.mean()

    def json_to_m3u(self, dic):
        """helper M3U initialization for dict sourced object. In this case,
         a single m3u list as a python dictionary. """
        self.playlist_name = dic['name']
        m3u = dic
        self.fn = m3u['fn']
        self.genres = m3u['genres']
        self.duration = m3u['duration']
        tracks = m3u['tracks']
        self.tracks = []
        for td in tracks:
            artist_title = td['artist_title']
            dur = td['duration']
            gens = td['genres']
            url = td['url']
            l1 = f"#EXTINF:{dur},{artist_title}"
            l2 = url
            vtrack = VLC_Track(l1, l2)
            vtrack.set_genres(gens)
            self.tracks.append(vtrack)
        cols = ['Artist - Title', 'Duration']
        ttrks = [[t.artist_title, t.duration] for t in self.tracks]
        self.df = pd.DataFrame(ttrks, columns=cols)
        self.simple_html = self.df.to_html(na_rep='unknown')

    #  add a track to the playlist
    def add_track(self, trk):
        if isinstance(trk, VLC_Track):
            self.tracks.append(trk)
    #         recompute duration, genres, html
            ttrks = [[t.artist_title, t.duration] for t in self.tracks]
            self.df = pd.DataFrame(ttrks, columns=self.cols)
            self.df.Duration = self.df.Duration.apply(M3U.compute_min_sec)
            self.simple_html = self.df.to_html(na_rep='unknown')
            self.genres = []
            for t in self.tracks:
                for g in t.genres:
                    self.genres.append(g)

            # print(f"success: {trk.artist_title} added to {self.playlist_name} ")
        else:
            print(f"not a track")


    # remove a track
    def remove_track(self, fn):

        for t in list(range(len(self.tracks))):
            if self.tracks[t].str_win_path == fn:
                tr = self.tracks.pop(t)
                # update playlist data  -- recompute duration, genres, html
                ttrks = [[x.artist_title, x.duration] for x in self.tracks]
                self.df = pd.DataFrame(ttrks, columns=self.cols)
                self.df.Duration = self.df.Duration.apply(M3U.compute_min_sec)
                self.simple_html = self.df.to_html(na_rep='unknown')
                self.genres = []
                for t in self.tracks:
                    for g in t.genres:
                        self.genres.append(g)
                return tr
            else:
                continue

    def to_dict(self):
        """convert this object into a dictionary representation"""
        dtracks =  [t.to_dict() for t in self.tracks ]
        d = {
                 'name': self.playlist_name,
                 'tracks': dtracks,
                 'duration': self.duration,
                 'fn': self.fn,
                 'genres': self.genres
        }

        return d

    # update mongo
    def update_mongo(self, d:dict):
        from analz.mongo.mongo_sandbox import RadioPlaylists
        rpl = RadioPlaylists()
        doc = rpl.update_playlist(d)
        return doc


    # ####################################################################
class Track:
    """Representation of an M3U Track"""
    def __init__(self, url=None, artist_title=None, duration=-1, genres=[]):
        import datetime
        self.url = url
        self.artist_title = artist_title
        if isinstance(duration, int) and duration != -1:
            secs = duration
            self.str_dur = str(datetime.timedelta(seconds=secs))
            self.duration = secs
        elif isinstance(duration, str):
            time = duration
            self.str_dur = time
            date_time = datetime.datetime.strptime(time, "%H:%M:%S")
            a_timedelta = date_time - datetime.datetime(1900, 1, 1)
            self.duration = a_timedelta.total_seconds()
        else:
            self.duration = duration
        self.genres = genres

    def set_genres(self, gens):
        self.genres = gens
    def to_dict(self):
        return {'artist_title': self.artist_title, 'url': self.url, 'duration': self.duration,
                'genres': self.genres}


class VLC_Track(Track):
    """Representation of a VLC Track"""
    line_feed = '\n'

    def __init__(self, line_1, line_2):
        """initialization from two lines allowed track
        definition in standard extended M3U spec."""
        # print(line_1)
        # print(line_2)
        self.l1 = line_1
        l2p = Path(line_2)
        self.l2 = str(l2p)
        artist_title = None
        dur = -1
        try:
            dur = (int(self.l1.split(',', 1)[0].split(':')[1]))
            artist_title = self.l1.split(',', 1)[1]
        except Exception as inst:
            print(str(inst))
            print ('line 1: ', self.l1)
        url = line_2
        if url[1] == ':':  # a windows drive designation
            # print(f"url: {url}")
            p = Path(url)
            self.str_win_path = str(p.as_posix())
            # print(f"str_win_path: {self.str_win_path}")

            super().__init__(url=self.str_win_path, artist_title=artist_title, duration=int(dur))
        else: # urn format
            if url.startswith('file://'):

                self.url_unq_pth = Path(unquote(url))
                self.windows_path = Path(self.url_unq_pth)
                self.str_win_path = str(self.windows_path.as_posix())
                super().__init__(url=self.str_win_path, artist_title=artist_title, duration=int(dur))
            else:
                raise Exception(f"{url} not recognized")

        if os.path.exists(self.str_win_path):
            self.exists = True
        else:
            self.exists = False
            # print(f"{self.l2} does not exist")
    def to_std_m3u_string(self):
        return f"{self.l1}{VLC_Track.line_feed}{self.str_win_path}"

    def to_vlc_m3u_string(self):
        return f"{self.l1}{VLC_Track.line_feed}{self.url}"

    @staticmethod
    def from_dict(dict_track):
        if isinstance(dict_track,dict):
            at = dict_track['artist_title']
            dur = dict_track['duration']
            url = dict_track['url']
            genres = dict_track['genres']
            l1 = f"{M3UList.xf_rec_marker}{dur},{at}"
            l2 = f"{url}"
            trk = VLC_Track(l1,l2)
            trk.set_genres(genres)
            return trk
        else:
            raise Exception('not a dictionary')


class HM3UList:
    def __init__(self, file_name, name=None):
        """Instance of http addressed m3ulist"""
        self.fn = file_name
        self.lname = name
        with open(self.fn) as f:
            lines = f.readlines()
            self.htracks = [HTrack(l.strip(), self.lname) for l in lines if l.startswith('http')]

class HTrack(Track):
    """ instance of an http addressed Track"""
    def __init__(self, url, auth=None, dur=-1, title=None, bytes=-1, mtype=None, desc=None, src=None):
        self.author = auth
        # artist_title = None
        duration = dur
        self.title = title
        self.bytes = bytes
        self.mtype = mtype
        self.source = src
        self.description = desc


        p = Path(url)
        if auth:
            if title:
                artist_title = " - ".join([auth, title])
            else:
                artist_title = p.name
        elif title:
            artist_title = title
        else:
            artist_title = p.name

        super().__init__(url=url, artist_title=artist_title, duration=duration)
        self.name = p.name
        status_code = requests.get(url).status_code
        self.exists = (status_code == 200)

    # def from_Pdt(trk:Pdt):
    #     url = trk.url
    #     author = trk.author
    #     ht = HTrack(trk.url, auth=trk.author,dur=trk.duration,title=trk.title,
    #                 bytes=trk.bytes, mtype=trk.type, desc=trk.description, src=trk.source)
    #     return ht









