import datetime
import os.path
from  pathlib import Path
from analz.playlist.pl_collection import PLCollection, bluegrass, BluesCollection, \
    OTR, rootsrock, country, enlighten, jazz

from config import Config



# ##########################################  TESTS   #####################################
class Test:


    #  test blues lists
    @staticmethod
    def get_salty_m3u(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = BluesCollection.get_blues_rs_mix(hrs, BluesCollection.SALTY_DOG )
        # print(f'out put file for Salty Dog Mix: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    @staticmethod
    def get_moose_m3u(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = BluesCollection.get_blues_rs_mix(hrs, BluesCollection.BLUES_MOOSE)
        # print(f'out put file for Blues Moose Mix: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    @staticmethod
    def get_misc_blues_m3u(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = BluesCollection.get_misc_mix(hrs)
        # print(f'out put file for Misc Blues Mix: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    #  Test jazz lists
    @staticmethod
    def get_jazz_mix(to_file=False, smooth=True, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = jazz.get_jazzmix(hrs,smooth=smooth)
        # print(f'out put file for Jazz Mix: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))

            m3u.fn = dfn
        return m3u, dfn

    #   Test Enlighten Lists, Fanny and Prophesy

    @staticmethod
    def get_fanny(to_file=False, hrs_mult=1.0):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = enlighten.get_fanny_mix(hrs)
        # print(f'out put file for Fanny Mix: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    @staticmethod
    def get_wolfe(to_file=True, hrs_mult=1.0):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = enlighten.get_fanny_mix(hrs)
        # print(f'out put file for Fanny Mix: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    @staticmethod
    def get_prophesy(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = enlighten.get_prophesy_mix(hrs)
        # print(f'out put file for Prophesy Mix: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    # Test Old Time Radio lists
    @staticmethod
    def get_otr_mix(to_file=False, hrs_mult=1.0):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = OTR.get_otr_mix(hrs)
        # print(f'out put file for Old Time Radio mix: {m3u.fn}')
        if to_file:
            dfn  = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        else:
            dfn = None
        return m3u, dfn

    # Test bluegrass lists

    @staticmethod
    def get_bluegrass_mix(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = bluegrass.get_bluegrass_mix(hrs)
        # print(f'out put file for Bluegrass Mix: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    @staticmethod
    def get_RE(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = bluegrass.get_rre_mix(hrs)
        # print(f'out put file for Railroad Earth: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    #  get Bluegrass Sarahs
    @staticmethod
    def get_sarahs(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = bluegrass.get_sarahs(hrs)
        # print(f'out put file for Bluegrass Sarahs: {m3u.fn}')
        if to_file:
           dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
           m3u.fn = dfn
        return m3u, dfn

    #  get AK
    @staticmethod
    def get_AK(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = bluegrass.get_AK(hrs)
        # print(f'out put file for Alison Krauss: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    # get Olds: garcia, et al

    #  get Old s
    @staticmethod
    def get_Olds(to_file=False, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = bluegrass.getOlds(hrs)
        # print(f'out put file for Olds: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    # test country lists
    @staticmethod
    def get_Country(to_file=False, type='divas', hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = None
        if type == 'divas':
            m3u = country.get_country_divas(hrs)
        elif type == 'guys':
            m3u = country.get_country_guys(hrs)
        elif type == 'mix':
            m3u = country.get_country_mix(hrs)
        else:
            raise Exception('invalid country pl type')
        # # print(f'out put file for Olds: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    #  Test Rock Roots lists
    @staticmethod
    def get_rocksroots(to_file=False, type=rootsrock.ROCKERS, hrs_mult=1):
        dfn = None
        hrs = 1 * hrs_mult
        m3u = None

        if type == rootsrock.ROCKERS:
            m3u = rootsrock.get_rockers(hrs)
        elif type == rootsrock.DYLAN:
            m3u = rootsrock.get_dylan(hrs)
        elif type == rootsrock.AVETT:
            m3u = rootsrock.get_avett_roots(hrs)
        elif type == rootsrock.JACKSON:
            m3u = rootsrock.get_jackson(hrs)
        elif type == rootsrock.DIVA:
            m3u = rootsrock.get_divas(hrs)
        elif type == rootsrock.DEAD:
            m3u = rootsrock.get_hornsby_dead(hrs)
        elif type == rootsrock.BRITS:
            m3u = rootsrock.get_brits(hrs)
        elif type == rootsrock.SPRING:
            m3u = rootsrock.get_springsteen(hrs)
        else:
            raise Exception(f"Invalid roots rock type: {type}")
        # print(f'out put file for Olds: {m3u.fn}')
        if to_file:
            dfn = Test.printfile(m3u.fn, m3u.make_vlc_m3u_playlist(m3u.tracks))
            m3u.fn = dfn
        return m3u, dfn

    # print file utility
    @staticmethod
    def printfile(fn, tx, prod_out=True):
        outd = PLCollection.out_top
        print(f"Original fn: {fn}")
        p = Path(fn)
        cat = p.parts[4]
        print(f'cat: {cat}')
        nm = p.name
        if prod_out:
            dic_dir = {'bluegrass_rotation': f"{outd}/bluegrass/{nm}",
                       'otr_rotation': f"{outd}/otr/{nm}",
                       'jazz_rotation': f"{outd}/jazz/{nm}",
                       'rock_roots_rotation': f"{outd}/rrock/{nm}",
                       'enlighten_rotation': f"{outd}/enlighten/{nm}",
                       'country_rotation': f"{outd}/country/{nm}",
                       'blues_rotation': f"{outd}/blues/{nm}"}
            fn = f"{dic_dir[cat]}"
            print(f"writing to file...{fn}")

        try:
            with open(fn, "w", encoding='Latin-1') as f:
                f.write(tx)
        except:
            raise Exception("cannot write file")
        return fn
# ###########################################  staging functions #############################

class stage:
    json_dr = Config.playlists_json
    json_fn = 'test.json'
    outd = PLCollection.out_top
    stage_dirs = {'bluegrass_rotation': f"{outd}/bluegrass/",
                       'otr_rotation': f"{outd}/otr/",
                       'jazz_rotation': f"{outd}/jazz/",
                       'rock_roots_rotation': f"{outd}/rrock/",
                       'enlighten_rotation': f"{outd}/enlighten/",
                       'country_rotation': f"{outd}/country/",
                       'blues_rotation': f"{outd}/blues/"}

    @staticmethod
    def patterns_to_json(pts):
        import json

        ff = f"{stage.json_dr}/{stage.json_fn}"
        with open(ff, "w") as f:
            json.dump(pts, f)


    @staticmethod
    def patterns_from_json():
        import json
        ff = f"{stage.json_dr}/{stage.json_fn}"
        with open(ff) as f:
            patd = json.load(f)
        return patd

    @staticmethod
    def pattern_to_html(pat_day:str):
        # from jinja2 import FileSystemLoader, Environment
        # templates = Config.templates_dir
        # temfl = os.path.join(templates,'menu.html')
        # if not os.path.exists(temfl):
        #     print(f"{temfl} does not exist")
        # loader = FileSystemLoader(templates)
        # templateEnv = Environment(loader=loader)
        # template = templateEnv.get_template(temfl)

        pat_num = stage.days[pat_day]
        pat = stage.patterns[pat_num]
        if pat_num == 'one':
            title = "Smooth, Blue and Old."
        elif pat_num == 'two':
            title = "Bluegrass drums, and the Rock ballad."
        elif pat_num == 'three':
            title = 'The Country of Prophesies'
        else:
            raise Exception(f"Exception: invalid pattern day: {pat_day}")
        props = {'title': title, 'ts': f"Themes for {datetime.datetime.now().strftime('%A, %d %B, %Y')}", 'rows': []}
        for k in pat.keys():
            props['rows'].append((pat[k]['time'],  pat[k]['description']))
        # output = template.render(title=title, ts=props['ts'], rows=props['rows'] )
        return props


    @staticmethod
    def clean_stage_dirs(dir='all'):
        import os, shutil
        if dir == 'all':
            dirs = stage.stage_dirs.values()
            for d in dirs:
                folder = d
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print(f'Failed to delete {file_path}. Reason: {e}')


    # 3 24-hour patterns of playlists and durations

    patterns = {'one': {'otr':
                            {'time': '00:01:00 - 08:01:00',
                             'description': "The Old Time Radio Tracks: Holmes, Marlowe, Dollar, the Firesign Theater"},
                        'enlighten.prophesy':
                            {'time': '08:02:00 - 12:00:00',
                             'description': "The Prophesy Tracks: It is Late but everything comes next."},

                        'blues.salty, blues.moose':
                            {'time':'12:01:00 - 16:59:00',
                             'description': "Blues across the world: Bluesmoose from Sweden, Salty Dog from Australia."},

                        'enlighten.programs' : {'time':'17:01:00 - 18:59:00',
                                                 'description': "The Enlighten Radio Storytelling Show, "
                                                                "Richard Wolfe's Economic Update"},

                        'jazz.smooth': {'time': '19:01:00 - 23:59:00',
                                        'description': "Smooth Jazz Through the Darkness"}
                        },
                'two': {'rock.dylan, rock.springsteen':  {'time': '00:01:00 - 08:01:00',
                             'description': "Bob and Bruce trade profundities"},
                        'enlighten.prophesy': {'time': '08:02:00 - 12:00:00',
                             'description': "The Prophesy Tracks: It is Late but everything comes next."},
                        'bluegrass.rre, bluegrass.sarahs': {'time':'12:01:00 - 16:59:00',
                             'description': "The Sarahs, and Railroad Earth"},
                        'enlighten.programs':  {'time':'17:01:00 - 18:59:00',
                                                 'description': "The Enlighten Radio Storytelling Show, "
                                                                "Richard Wolfe's Economic Update"},
                        'rrock.brits, rrock.jackson': {'time': '19:01:00 - 23:59:00',
                                        'description': "Smooth Jazz Through the Darkness"}
                        },
                'three': {'otr':
                              {'time': '00:01:00 - 08:01:00',
                             'description': "The Old Time Radio Tracks: Holmes, Marlowe, Dollar, the Firesign Theater"
                               },

                          'enlighten.prophesy':
                              {'time': '08:02:00 - 12:00:00',
                               'description': "The Prophesy Tracks: It is Late but everything comes next."
                               },

                          'country.mix,county.divas':
                              {'time':'12:01:00 - 16:59:00',
                               'description': "The Sarahs, and Railroad Earth"
                               },

                          'enlighten.programs':
                              {'time':'17:01:00 - 18:59:00',
                               'description': "The Enlighten Radio Storytelling Show, Richard Wolfe's Economic Update"
                               },
                          'jazz.classic':
                              {'time': '19:01:00 - 23:59:00',
                                'description': "Smooth Jazz Through the Darkness"
                               }
                          }
                }

    days = {'mon': 'one',
            'tue': 'two',
            'wed': 'three',
            'thu': 'one',
            'fri': 'two',
            'sat': 'three',
            'sun': 'one'}

    def __init__(self, day):
        self.day = day
        self.pat = stage.days[day]
        self.patterns = stage.patterns_from_json()
        self.patd = self.patterns[self.pat]
        self.FMT = '%H:%M:%S'
        self.day_dic = {}
        self.now = datetime.datetime.utcnow()
        self.get_day_dic()


    def load_coll_dict(self, coll:str, colld:dict ):
        timestrs = self.patd[coll]['time'].split(' - ')
        tms = [datetime.datetime.strptime(t.strip(), self.FMT) for t in timestrs]
        if len(tms) != 2:
            raise Exception('times not equal to 2')
        colld['start'] = tms[0]
        colld['end'] = tms[1]
        tdelta = tms[1] - tms[0]
        colld['tdelta'] = str(tdelta)
        colld['duration'] = tdelta.seconds
        colld['hrs'] = float(colld['duration'] / 3600)
        # print(f"number of hours for {coll}: {colld['hrs']}")



    def get_day_dic(self):
        self.day_dic['utc_date'] = datetime.datetime.utcnow()
        self.day_dic['day'] = self.day
        self.day_dic['name'] = f"{self.pat}_{str(self.day_dic['utc_date'])}"
        if self.pat == 'one':
            # {'one': {'otr': '00:01:00 - 08:01:00',
            #          'enlighten.prophesy': '08:02:00 - 12:00:00',
            #          'blues.salty, blues.moose': '12:01:00 - 16:59:00',
            #          'enlighten.programs': '17:00:00  -  19:00:00',
            #          'jazz.smooth': '19:01:00 - 23:59:00'
            #          },
            for coll in self.patd.keys():
                colld = {}
                coll = coll.strip()
                if coll == 'otr':
                    self.load_coll_dict(coll, colld)
                    m3u, fn = Test.get_otr_mix(to_file=True, hrs_mult=colld['hrs'])
                    colld['fn'] = [fn]
                    colld['m3u'] = [m3u.to_dict()]
                    self.day_dic[coll] = colld




                elif coll == 'enlighten.prophesy':
                    self.load_coll_dict(coll, colld)
                    m3u, fn = Test.get_prophesy(to_file=True, hrs_mult=colld['hrs'])
                    colld['fn'] = [fn]
                    colld['m3u'] = m3u.to_dict()
                    self.day_dic[coll] = colld

                elif coll == 'enlighten.programs': # streamed podcast: needs no m3u file, managed from RDJ
                    pass

                elif coll == 'jazz.smooth':
                    self.load_coll_dict(coll, colld)
                    m3u, fn = Test.get_jazz_mix(to_file=True, smooth=True, hrs_mult=colld['hrs'])
                    colld['fn'] = [fn]
                    colld['m3u'] = [m3u.to_dict()]
                    self.day_dic[coll] = colld
                elif coll == 'blues.salty, blues.moose':
                    self.load_coll_dict(coll, colld)
                    dhrs = colld['hrs']
                    # print(f"type dhrs: {type(dhrs)}, value is: {dhrs}")
                    m3us, fns = Test.get_salty_m3u(to_file=True, hrs_mult=dhrs/2)
                    m3um, fnm = Test.get_moose_m3u(to_file=True, hrs_mult=(colld['hrs'])/2)
                    colld['fn'] = [fns]
                    colld['fn'].append(fnm)
                    colld['m3u'] = [m3us.to_dict()]
                    colld['m3u'].append(m3um.to_dict())
                    self.day_dic[coll] = colld
                else:
                    raise Exception(f"{coll} is wrong category for pattern one")
            else:
                pass

        elif self.pat == 'two':

            # 'two': {'rock.dylan, rock.springsteen': '00:01:00 - 08:01:00',
            #         'enlighten.prophesy': '08:02:00 - 12:00:00',
            #         'bluegrass.rre, bluegrass.sarahs': '12:01:00 - 16:59:00',
            #         'enlighten.programs': '17:00:00  -  19:00:00',
            #         'rrock.brits, rrock.jackson': '19:01:00 - 23:59:00'

            for coll in self.patd.keys():
                coll = coll.strip()
                colld = {}
                if coll == 'rock.dylan, rock.springsteen':
                    self.load_coll_dict(coll, colld)
                    dhrs = colld['hrs']
                    hrs = dhrs / 2
                    # print(f"type dhrs: {type(dhrs)}, value is: {dhrs}")
                    m3ub, fnb = Test.get_rocksroots(to_file=True, type=rootsrock.DYLAN, hrs_mult=hrs)
                    m3uj, fnj = Test.get_rocksroots(to_file=True, type=rootsrock.SPRING, hrs_mult=hrs)
                    colld['fn'] = [fnb]
                    colld['fn'].append(fnj)
                    colld['m3u'] = [m3ub.to_dict()]
                    colld['m3u'].append(m3uj.to_dict())
                    self.day_dic[coll] = colld



                elif coll == 'enlighten.prophesy':
                    self.load_coll_dict(coll, colld)
                    m3u, fn = Test.get_prophesy(to_file=True, hrs_mult=colld['hrs'])
                    colld['fn'] = [fn]
                    colld['m3u'] = [m3u.to_dict()]
                    self.day_dic[coll] = colld

                elif coll == 'enlighten.programs': # streamed podcast: needs no m3u file, managed from RDJ
                    pass

                elif coll == 'bluegrass.rre, bluegrass.sarahs':
                    self.load_coll_dict(coll, colld)

                    dhrs = colld['hrs']
                    hrs = dhrs / 2
                    m3urr, fnr = Test.get_RE(to_file=True, hrs_mult=hrs)
                    m3uss, fns = Test.get_sarahs(to_file=True, hrs_mult=hrs)

                    colld['fn'] = [fnr,fns]
                    colld['m3u'] = [m3urr.to_dict(), m3uss.to_dict()]
                    self.day_dic[coll] = colld
                elif coll == 'rrock.brits, rrock.jackson':
                    self.load_coll_dict(coll, colld)
                    dhrs = colld['hrs']
                    hrs = dhrs / 2
                    # print(f"type dhrs: {type(dhrs)}, value is: {dhrs}")
                    m3ub, fnb = Test.get_rocksroots(to_file=True, type=rootsrock.BRITS,hrs_mult=hrs)
                    m3uj, fnj = Test.get_rocksroots(to_file=True, type=rootsrock.JACKSON,hrs_mult=hrs)
                    colld['fn'] = [fnb]
                    colld['fn'].append(fnj)
                    colld['m3u'] = [m3ub.to_dict()]
                    colld['m3u'].append(m3uj.to_dict())
                    self.day_dic[coll] = colld
                else:
                    raise Exception(f"{coll} is wrong category for pattern two")
            else:
                pass

        elif self.pat == 'three':

            # 'three': {'otr': '00:01:00 - 08:01:00',
            #                           'enlighten.prophesy': '08:02:00 - 12:00:00',
            #                           'country.mix,county.divas': '12:01:00 - 16:59:00',
            #                           'enlighten.programs': '17:00:00  -  19:00:00',
            #                           'jazz.classic': '19:01:00 - 23:59:00'
            #                           }
            for coll in self.patd.keys():
                coll = coll.strip()
                colld = {}
                if coll == 'otr':
                    self.load_coll_dict(coll, colld)
                    m3u, fn = Test.get_otr_mix(to_file=True, hrs_mult=colld['hrs'])
                    colld['fn'] = [fn]
                    colld['m3u'] = [m3u.to_dict()]
                    self.day_dic[coll] = colld

                elif coll == 'enlighten.prophesy':
                    self.load_coll_dict(coll, colld)
                    m3u, fn = Test.get_prophesy(to_file=True, hrs_mult=colld['hrs'])
                    colld['fn'] = [fn]
                    colld['m3u'] = [m3u.to_dict()]
                    self.day_dic[coll] = colld

                elif coll == 'enlighten.programs': # streamed podcast: needs no m3u file, managed from RDJ
                    pass

                elif coll == 'country.mix,county.divas':
                    self.load_coll_dict(coll, colld)
                    dhrs = colld['hrs']
                    hrs = dhrs / 2
                    m3um, fnm = Test.get_Country(to_file=True, type='mix', hrs_mult=hrs)
                    m3ud, fnd = Test.get_Country(to_file=True, type='divas', hrs_mult=hrs)

                    colld['fn'] = [fnm, fnd]
                    colld['m3u'] = [m3um.to_dict(),m3ud.to_dict()]
                    self.day_dic[coll] = colld
                elif coll == 'jazz.classic':
                    self.load_coll_dict(coll, colld)
                    dhrs = colld['hrs']
                    # print(f"type dhrs: {type(dhrs)}, value is: {dhrs}")
                    m3u, fn = Test.get_jazz_mix(to_file=True, smooth=False, hrs_mult=dhrs)
                    colld['fn'] = [fn]
                    colld['m3u'] = [m3u.to_dict()]
                    self.day_dic[coll] = colld
                else:
                    raise Exception(f"{coll} is wrong category for pattern three")
        else:
            pass












