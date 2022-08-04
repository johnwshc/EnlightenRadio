import os
from analz.playlist.m3u import M3U
from analz.mongo.mongo_sandbox import MongoER
from config import Config
import os
from  pathlib import Path
import pandas as pd


class PLCollection:

    fd = Config.playlists_dir
    json_deploy_dir = f"{Config.playlists_json}/er_deployments"
    pl_hr = 3600
    out_top = Config.er_pl_out
    blues_collection_dir = Path(os.path.join(f"{fd}",'blues_rotation')).as_posix()
    bluegrass_collection_dir = Path(os.path.join(f"{fd}",'bluegrass_rotation')).as_posix()
    rock_roots_collection_dir = Path(os.path.join(f"{fd}",'rock_roots_rotation')).as_posix()
    country_collection_dir = Path(os.path.join(f"{fd}",'country_rotation')).as_posix()
    # fix jazz path
    jazz_collection_dir = Path(os.path.join(f"{fd}", 'jazz_rotation')).as_posix()
    jazz_path = Path(jazz_collection_dir)
    jazz_pth_parts = jazz_path.parts
    all_parts = [jazz_path.drive]
    all_parts.extend(jazz_pth_parts[1:])
    jazz_collection_dir = '/'.join(all_parts)
    enlighten_collection_dir = Path(os.path.join(f"{fd}", 'enlighten_rotation')).as_posix()
    otr_collection_dir = Path(os.path.join(f"{fd}", 'otr_rotation')).as_posix()



    @staticmethod
    def secs2_dt_str(duration:int):
        import datetime
        secs = duration
        str_dur = str(datetime.timedelta(seconds=secs))
        return str_dur

    @staticmethod
    def merge_m3u(mult:float, strks:pd.Series, out_fn, lname):
        max = PLCollection.pl_hr * mult
        curr = 0
        num_tracks = 0
        for t in strks:
            curr += t.duration
            num_tracks += 1
            if curr >= max:
                break;

        trks = strks.iloc[0:num_tracks - 1, ].copy()
        dtrks = [t.to_dict() for t in trks]
        dur = pd.Series([t.duration for t in trks]).sum()
        return M3U(trks={
            'fn': out_fn,
            'duration': dur,
            'genres': ['bluegrass'],
            'tracks': dtrks,
            'name': lname
        })



class rootsrock(PLCollection):

    AVETT = 0
    DYLAN = 1
    JACKSON = 2
    DIVA = 3
    DEAD = 4
    BRITS = 5
    SPRING = 6
    ROCKERS = 7
    hr = 3600.0
    rrdir = PLCollection.rock_roots_collection_dir

    @staticmethod
    def get_rockers(mult:float):
        src_dir = PLCollection.rock_roots_collection_dir
        out_fn = f"{src_dir}/rr_rockers.m3u"
        lname = "Rockers"
        src_fn = f"{src_dir}/rockers1.m3u"
        srctrks = M3U(src_fn).tracks
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_avett_roots(mult: float):
        lname = 'Roots Revival Nothing Finer in Carolina'
        rr_dir = PLCollection.rock_roots_collection_dir
        src_fn = f"{rr_dir}/roots_avett_hiss.m3u"
        out_fn = f"{rr_dir}/rr_avett.m3u"
        m3u = M3U(src_fn)
        src_trks = m3u.tracks
        samp_trks = src_trks.sample(frac=1).copy().reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_dylan(mult:float):

        src_dir = PLCollection.rock_roots_collection_dir
        out_fn = f"{src_dir}/rr_dylan.m3u"
        lname = "Bob Dylan Mix"
        src_fns = [f"{src_dir}/dylan1.m3u", f"{src_dir}/dylan2.m3u", f"{src_dir}/dylan3.m3u"]
        l_strks = [M3U(x).tracks for x in src_fns]
        srctrks = pd.concat(l_strks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_jackson(mult:float):

        src_dir = PLCollection.rock_roots_collection_dir
        out_fn = f"{src_dir}/rrjackson_mix.m3u"
        lname = "Jackson Brown Mix"
        src_fns = [f"{src_dir}/jackson1.m3u", f"{src_dir}/jackson2.m3u", f"{src_dir}/jackson3.m3u",
                   f"{src_dir}/jackson4.m3u",f"{src_dir}/jackson_and_willie.m3u"]
        l_strks = [M3U(x).tracks for x in src_fns]
        srctrks = pd.concat(l_strks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_divas(mult:float):
        src_dir = PLCollection.rock_roots_collection_dir
        out_fn = f"{src_dir}/divas_mix.m3u"
        lname = "Rock Roots Divas Mix"
        src_fns = [f"{src_dir}/BONNIE_BIG.m3u", f"{src_dir}/armatrading.m3u", f"{src_dir}eliza_g.m3u",
                   f"{src_dir}rockdivas.m3u", f"{src_dir}jackson_and_willie.m3u"]
        l_strks = [M3U(x).tracks for x in src_fns]
        srctrks = pd.concat(l_strks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_hornsby_dead(mult:float):
        src_dir = PLCollection.rock_roots_collection_dir
        out_fn = f"{src_dir}/rr_dh.m3u"
        lname = "The Dead Band and the Keyboarder"
        src_fn = f"{src_dir}/dead_hornsby.m3u"
        srctrks = M3U(src_fn).tracks
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_brits(mult:float):
        src_dir = PLCollection.rock_roots_collection_dir
        out_fn = f"{src_dir}/brits.m3u"
        lname = "Brits Survival Gear"
        src_fns = [f"{src_dir}/vanmorrison.m3u", f"{src_dir}/sting_stones_u2.m3u"]
        l_strks = [M3U(x).tracks for x in src_fns]
        print(f'type of l_strks is {type(l_strks)}')
        srctrks = pd.concat(l_strks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_springsteen(mult:float):
        src_dir = PLCollection.rock_roots_collection_dir
        out_fn = f"{src_dir}/rr_springsteen.m3u"
        lname = "Springsteen"
        src_fn = f"{src_dir}/springsteen.m3u"
        srctrks = M3U(src_fn).tracks
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)


class country(PLCollection):
    @staticmethod
    def get_country_mix(mult:float):
        lname = 'The Country Mix'
        src_dir = PLCollection.country_collection_dir
        out_fn = f"{src_dir}/country_mix.m3u"
        src_fns = [f"{src_dir}/country2.m3u", f"{src_dir}/country3.m3u", f"{src_dir}/country4.m3u",
                   f"{src_dir}/country5.m3u", f"{src_dir}/country6.m3u"]

        l_strks = [M3U(x).tracks for x in src_fns]
        srctrks = pd.concat(l_strks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_country_divas(mult:float):
        lname = "Country Divas"

        src_dir = PLCollection.country_collection_dir
        out_fn = f"{src_dir}/countrydivas.m3u"
        src_fns = [f"{src_dir}/mcc.m3u", f"{src_dir}/jewel.m3u", f"{src_dir}/pistol_annie.m3u",
                   f"{src_dir}/patty_griffin.m3u",f"{src_dir}/dolly.m3u", f"{src_dir}/eliza_g.m3u",
                   f"{src_dir}/emmy_rita_rosanne.m3u"]

        l_strks = [M3U(x).tracks for x in src_fns]
        srctrks = pd.concat(l_strks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_country_guys(mult:float):
        lname = "Country Boys"
        src_dir = PLCollection.country_collection_dir
        out_fn = f"{src_dir}/countryboys.m3u"
        src_fns = [f"{src_dir}/willie_and_others.m3u", f"{src_dir}/morrissey1.m3u", f"{src_dir}/merle.m3u",
                   f"{src_dir}/jason_isbell.m3u", f"{src_dir}/guy_clark.m3u", f"{src_dir}/country_georges.m3u",
                   f"{src_dir}/cash_kris.m3u"]

        l_strks = [M3U(x).tracks for x in src_fns]
        srctrks = pd.concat(l_strks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

class bluegrass(PLCollection):

    hr = 3600.0
    bgdir = PLCollection.bluegrass_collection_dir


    @staticmethod
    def get_bluegrass_mix(mult:float):
        lname = "Addicted to Grass"
        src_fn = '/'.join([bluegrass.bgdir,'bluegrass_mix.m3u'])
        out_fn = '/'.join([bluegrass.bgdir, 'bluegrass1.m3u'])
        m3u = M3U(src_fn)
        src_trks = m3u.tracks
        samp_trks = src_trks.sample(frac=1).copy().reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)


    @staticmethod
    def get_rre_mix(mult: float):
        lname = "Railroad Earth Evolves"
        src_fn = '/'.join([bluegrass.bgdir, 'railroad_earth.m3u'])
        out_fn = '/'.join([bluegrass.bgdir, 'bluegrassRE.m3u'])
        m3u = M3U(src_fn)
        src_trks = m3u.tracks
        samp_trks = src_trks.sample(frac=1).copy().reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_sarahs(mult:float):
        lname = "The Bluegrass Sarahs"
        src_dir = bluegrass.bgdir
        src_file = 'sarahs.m3u'
        src_fn = '/'.join([src_dir,src_file])
        out_fn = '/'.join([bluegrass.bgdir, 'bluegrassSarahs3.m3u'])
        m3u = M3U(src_fn)
        strks = m3u.tracks
        samp_trks = strks.sample(frac=1).copy().reset_index(drop=True)

        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_AK(mult:float):
        lname = "The Brotherhood of Man"
        out_fn = f"{bluegrass.bgdir}/bbluegrassAK.m3u"
        m3uAK = M3U(f"{bluegrass.bgdir}/AK_UNIONSTATION.m3u")
        m3u_seldom = M3U(f"{bluegrass.bgdir}/seldomPlus.m3u")
        strks = pd.concat([m3uAK.tracks, m3u_seldom.tracks], ignore_index=True)
        samp_trks = strks.sample(frac=1).copy().reset_index(drop=True)

        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)


    @staticmethod
    def getOlds(mult:float):

        lname = "The Old Men and the Land"
        src_fn = f"{bluegrass.bgdir}/olds.m3u"
        out_fn = f"{bluegrass.bgdir}/bluegrass4olds.m3u"
        m3u = M3U(src_fn)
        src_trks = m3u.tracks
        samp_trks = src_trks.sample(frac=1).copy().reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)


class enlighten(PLCollection):
    lname = 'Stories, and the Prophesy Fix'

    @staticmethod
    def get_fanny_mix(mult:float):
        lname = 'Enlighten Radio Storytelling'
        srcs_fanny = f"{PLCollection.enlighten_collection_dir}/fanny_and_stas.m3u"
        src_trks = M3U(srcs_fanny).tracks
        out_fn = f"{PLCollection.enlighten_collection_dir}/fanny.m3u"
        samp_trks = src_trks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    @staticmethod
    def get_prophesy_mix(mult:float):
        srcs = [
            f"{PLCollection.enlighten_collection_dir}/prophesy2.m3u",
            f"{PLCollection.enlighten_collection_dir}/prophesy3.m3u"
        ]
        out_fn = f"{PLCollection.enlighten_collection_dir}/prophesy.m3u"
        lname = "Crow Prophesies"
        ltrks = [M3U(f).tracks for f in srcs]
        srctrks = pd.concat(ltrks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)



class jazz(PLCollection):
    src_smooth = [
        f"{PLCollection.jazz_collection_dir}/marsallis_montgomery_jazz.m3u",
        f"{PLCollection.jazz_collection_dir}/smooth_jazz.m3u",
        f"{PLCollection.jazz_collection_dir}/bruce_abbot_brubeck.m3u"
    ]
    src_reg = [
        f"{PLCollection.jazz_collection_dir}/divas.m3u",
        f"{PLCollection.jazz_collection_dir}/jazz monk.m3u",
        f"{PLCollection.jazz_collection_dir}/bruce_abbot_brubeck.m3u",
        f"{PLCollection.jazz_collection_dir}/armstrong_jazz.m3u"
    ]
    hr = PLCollection.pl_hr


    @staticmethod
    def get_jazzmix(mult:float, smooth=True):
        out_fn = f"{PLCollection.jazz_collection_dir}/jazz.m3u"
        if smooth:
            lname = "smooth jazz mix"
            ltrks = [M3U(f).tracks for f in jazz.src_smooth]
        else:
            lname = "Classic jazz Mix"
            ltrks = [M3U(f).tracks for f in jazz.src_reg]
        srctrks = pd.concat(ltrks, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

class OTR(PLCollection):
    """Old Time Radio lists"""
    src_lists = [
    f"{PLCollection.otr_collection_dir}/phillip_marlowe.m3u",
    f"{PLCollection.otr_collection_dir}/johnny_dollar.m3u",
    f"{PLCollection.otr_collection_dir}/sherlock_holmes.m3u",
    f"{PLCollection.otr_collection_dir}/firesign.m3u"]


    @staticmethod
    def get_otr_mix(mult:float):
        lname = 'Old Time Radio Mix'
        out_fn = f"{PLCollection.otr_collection_dir}/otr_misc.m3u"
        src_m3us = [M3U(f).tracks for f in OTR.src_lists]
        srctrks = pd.concat(src_m3us, ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

###########################   Blues Collection Playlists  #########################
class BluesCollection(PLCollection):
    SALTY_DOG = 0
    BLUES_MOOSE = 1
    src_rs_filenames = ['salty_dog.m3u', 'bluesmoose1.m3u']
    rs_names = ['Salty Dog Mix.m3u', 'Blues Moose Mix.m3u']
    lnames = ['Salty Dog Mix', 'Blues Moose Mix']
    src_misc_filenames = ['all_bluesd_up_mix.m3u', 'Buddy_guy_junior_wells.m3u', 'lightnin_hopkins.m3u']
    hr = PLCollection.pl_hr
    # dur_secs = multiplier times hrs of playlist length

    def get_blues_rs_mix(mult:float, src_id:int):
        src_name = None
        out_fn = None
        lname = None
        if src_id == BluesCollection.SALTY_DOG:
            src_name = BluesCollection.src_rs_filenames[BluesCollection.SALTY_DOG]
            out_fn = f"{PLCollection.blues_collection_dir}/{BluesCollection.rs_names[BluesCollection.SALTY_DOG]}"
            lname = BluesCollection.lnames[BluesCollection.SALTY_DOG]

        elif src_id == 1:
            src_name = BluesCollection.src_rs_filenames[BluesCollection.BLUES_MOOSE]
            out_fn = f"{PLCollection.blues_collection_dir}/{BluesCollection.rs_names[BluesCollection.BLUES_MOOSE]}"
            lname = BluesCollection.lnames[BluesCollection.BLUES_MOOSE]
        else:
            raise Exception('Blues Radio Show invalid src id')
        m3u_f = f"{Config.playlists_dir}/blues_rotation/{src_name}"
        m3u = M3U(file_name=m3u_f)
        ser_trks = pd.Series([t for t in m3u.tracks])
        samp_trks = ser_trks.sample(frac=1).copy().reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)

    def get_misc_mix(mult:float):
        lname = 'Miscellaneous Blues'
        out_fn = f"{Config.playlists_dir}/blues_rotation/misc_mix.m3u"
        m1_trks = M3U(file_name=f"{Config.playlists_dir}/blues_rotation/{BluesCollection.src_misc_filenames[0]}").tracks
        m2_trks = M3U(file_name=f"{Config.playlists_dir}/blues_rotation/{BluesCollection.src_misc_filenames[1]}").tracks
        m3_trks = M3U(file_name=f"{Config.playlists_dir}/blues_rotation/{BluesCollection.src_misc_filenames[2]}").tracks
        srctrks  = pd.concat([m1_trks, m2_trks, m3_trks], ignore_index=True)
        samp_trks = srctrks.sample(frac=1).reset_index(drop=True)
        return PLCollection.merge_m3u(mult, samp_trks, out_fn, lname)









