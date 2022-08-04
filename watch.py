import datetime
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import Config
import logging
import json
import requests

from logging.handlers import RotatingFileHandler
from analz.mongo.mongo_sandbox import RadioDeployments as RD

class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        #  init Mongo DB
        # rd = RD()
        # get logger
        logger = logging.getLogger('Enlighten_Radio_WP_Log')
        logger.setLevel(logging.INFO)
        log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add a rotating log handler
        log_handler = RotatingFileHandler(Config.ER_LOG_FILE_PATH, maxBytes=50000,
                                          backupCount=5)
        log_handler.setFormatter(log_formatter)
        logger.addHandler(log_handler)


        rel_src = str(event.src_path)
        print(f"event source path: {rel_src}")
        src = rel_src[9:]
        # type = str(event.event_type)
        print(f"event: {event}")
        logger.info(f'event: {event}')

        if event.event_type == 'modified' and src == 'Now_Playing.txt':
            print(f'caught an event, src={src}')
            with open(Config.ER_WP) as f:
                txt = f.readline()
                res = Watcher.post_to_site({'wp': txt})
                print(f"result of post to wp site: {res}")
                msg = f"wp update txt: {txt}"
                print(msg)
                logger.info(msg)
                logger.info(f"update_res: {res}")
                # rd.insert_npl_record((txt, str(datetime.datetime.utcnow())))
        handlers = logger.handlers[:]
        for handler in handlers:
            logger.removeHandler(handler)
            handler.close()

class Watcher:
    # now_playing = []
    @staticmethod
    def post_to_site(d:dict):
        url = f"{Config.SITE_URL}/whats_playing"
        data = d
        r = requests.post(url, json=data)
        return r.text

    def __init__(self, directory="./wp_out", handler=MyHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print(f"\nWatcher Running in {self.directory}/\n")
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")






if __name__=="__main__":
    w = Watcher(directory="./wp_out", handler=MyHandler())
    w.run()

