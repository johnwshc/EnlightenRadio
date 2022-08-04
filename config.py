import os
from pathlib import Path
import zipfile
import datetime

import logging.handlers


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    static_dir = Path(basedir,'app/static').as_posix()
    templates_dir = Path(basedir, 'app/templates').as_posix()
    playlists_dir = Path(basedir,'m3us').as_posix()
    playlists_json = Path(basedir, 'json').as_posix()
    er_pl_out = Path(f'{playlists_dir}/pl_out').as_posix()
    ER_LOG_FILE_PATH = os.path.join(basedir,"logs/er_manage.log")
    ER_WP = os.path.join(basedir,"wp_out/Now_Playing.txt" )
    ER_WP_P = os.path.join(basedir,"wp_out_p/Now_Playing.txt" )
    SITE_HOST = '127.0.0.1'
    SITE_PORT = 5000
    SITE_URL = f"http://{SITE_HOST}:{SITE_PORT}"
    GIT_REPO = "https://github.com/johnwshc/EnlightenRadio.git"

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    azure_url = 'https://flaskfolium.azurewebsites.net'
    browser_sync = 'browser-sync start --server --files "*/**'

    blogger_api_key = 'AIzaSyBfVB6vTPwTBrWcCLi_NK4kPxOcBh_xjNI'
    blogger_client_id = '946832198726-eub0q1jk1b46emlsqdrbsj3aupsij1ue.apps.googleusercontent.com'
    blogger_client_id2 = '946832198726-eub0q1jk1b46emlsqdrbsj3aupsij1ue.apps.googleusercontent.com'
    bloger_api_key2 = 'AIzaSyD862XP1RJesWfqiGwTMQW3p47A3wgw-dk'



    # #######################  logging ###########################

    #

    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #                     handlers=[RotatingFileHandler(filename=ER_LOG_FILE_PATH, maxBytes=50000, backupCount=5)])
    # logger = logging.getLogger('main')

    #  unzip ##################################################

    @staticmethod
    def unzip(zipf: str, dir: str):
        with zipfile.ZipFile(zipf, 'r') as zip_ref:
            zip_ref.extractall(dir)


    #  datetime.dateime to and from strings utilities
    @staticmethod
    def date2str(d: datetime.datetime):
        return d.strftime('%m/%d/%Y')

    @staticmethod
    def str2date(s: str):
        return datetime.datetime.strptime(s, '%m/%d/%Y' )


