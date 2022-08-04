

class EPrograms:
    programs = {
                        'catnights':
                           { 'events': ['Midnight Sunday', 'Midnight Monday', 'Midnight Tuesday',
                                        'Midnight Wednesday', 'Midnight Thursday', 'Midnight Friday',
                                        'Midnight Saturday'],
                             'evt_duration': 6

                            },
                        'catnews':
                            {'times': ["7AM Monday", '5PM Monday', "7AM Tuesday", '5PM Tuesday',"7AM Wednesday", '5PM Wednesday',
                                   "7AM Thursday", '5PM Thursday', "7AM Friday", '5PM Friday',"7AM Saturday", '5PM Saturday',
                                   "7AM Sunday", '5PM Sunday'],
                             'duration': 2
                             },
                        'catlive':
                            {
                                'times': ['9AM Sunday', '9AM Monday' , '9AM Planet Tuesday','9AM Wednesday', '9AM Thursday',
                                            '9AM Friday', '9AM Saturday'],
                                'duration': 3
                            },
                        'cataft':
                            {
                                'times': ['Noon Sunday', 'Noon Monday' , 'Noon Tuesday','Noon Wednesday', 'Noon Thursday',
                                            'Noon Friday', 'Noon Saturday'],

                                'duration':5
                            },
                        'catstories':
                            {
                                'times': ['7PM Sunday', '7PM Monday' , '7PM Tuesday','7PM Wednesday', '7PM Thursday',
                                            '7PM Friday', '7PM Saturday'],
                                'duration': 2

                            },
                        'cateves':
                            {
                                'times': ['9PM Sunday', '9PM Monday', '9PM Tuesday', '9PM Wednesday', '9PM Thursday',
                                          '9PM Friday', '9PM Saturday'],
                                'duration': 2
                            }

                  }
    genres = ['blues', 'spoken', 'stories', 'shows', 'concerts', 'country', 'bluegrass',
              'rock', 'oldies', 'folk', 'folk-rock', 'dylanesque', 'divas', 'rnb', 'soul',
              'commie', 'science', 'jacksons', 'bruces', 'reggae', 'world', 'holiday', 'rap',
              'roots', 'classical',  'comedy', 'country', 'alternative', 'unknown']

#     plss = [AK_UNION STATION.m3u
# all_bluesd_up_dylan2.m3u
# all_bluesd_up_mix.m3u
# all_bluesed_up_dylan.m3u
# art_pepper_w_sauce.m3u
# bluegrass_mix.m3u
# blues1.m3u
# BONNIE_BIG.m3u
# BR549.m3u
# chris_stapleton.m3u
# commander_cody.m3u
# divas.m3u
# dixie_chicks.m3u
# dolly.m3u
# eagles.m3u
# ella fitzgerald.m3u
# ellery queen.m3u
# fanny_and_stas.m3u
# george_jones.m3u
# george_strait.m3u
# gimme_shelter.m3u
# guy_clark.m3u
# hiatt.m3u
# hornsby.m3u
# jackson_and_willie.m3u
# jason_isbell.m3u
# jazz_1.m3u
# jazz monk.m3u
# johnny_dollar.m3u
# johnny_cash.m3u
# john_cippolina.m3u
# joni_joyce.m3u
# julie_london.m3u
# lightnin_hopkins.m3u
# mary_chapin.m3u
# merle.m3u
# mon_morn_early.m3u
# news.m3u
# norahs.m3u
# phillip_marlowe.m3u
# philo vance.m3u
# prophesy2.m3u
# prophesy3.m3u
# raina1.m3u
# recovery.m3u
# salty_dog.m3u
# sherlock_holmes.m3u
# sonny_sonny_brownie.m3u
# steve_martin_scr.m3u
# talkin_socialism.m3u
# tammy_wynette.m3u
# warren_zevon_95.m3u]


class Catnights(EPrograms):

    def __init__(self, cat):
        self.cat = cat
        self.times = cat['times']
        self.duration = int(cat['duration'])
        self.events = cat['events']

