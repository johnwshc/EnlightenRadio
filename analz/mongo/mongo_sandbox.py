import pandas as pd
import requests
import json
from config import Config
from pymongo import MongoClient



class MongoER:
    atlas_radio_uri = "mongodb+srv://admin:Uncl3H0H0!!@sandbox.xtifj.mongodb.net/radio?retryWrites=true&w=majority"
    atlas_bamazon_uri = "mongodb+srv://admin:Uncl3H0H0!!@sandbox.xtifj.mongodb.net/bamazon?retryWrites=true&w=majority"
    mongo_local_uri = 'mongodb://localhost:27017/'
    mongosh_uri = "mongodb+srv://sandbox.xtifj.mongodb.net/myFirstDatabase"
    mongo_json_export_dir = Config.playlists_json
    data_api_url = 'https://data.mongodb-api.com/app/data-jqglk/endpoint/data/beta'

    # mongosh_conn = mongosh "mongodb+srv://sandbox.xtifj.mongodb.net/radio" --apiVersion 1 --username admin

class MongoAZ(MongoER):
    api_key_AZC = 'cYhgSNFoSqkMcYloZbzwBlfXL3Sp096RUCXxdJcAstaR9QEI0x4ofmmW1zATesiK'
    ffcs_cols = ['state', 'county', 'address', 'Median_Household_Income',
                 'Unemployment_rate_2019', 'Unemployment_rate_2020',
                 'pct_under_hs_diploma_15_19', 'pct_hs_diploma_only_15_19',
                 'pct_some_college_15_19', 'pct_college_plus_15_19', 'POP_Est_2010',
                 'POP_Est_2019', 'avg_pct_cng', 'In_Poverty_2019', 'Pct_Poverty_2019',
                 'Child_Poverty_2019', 'Child_poverty_pct_2019',
                 'Median_household_inc_2019', 'TOT_POP', 'TOT_MALE',
                 'TOT_FEMALE', 'WA_MALE', 'WA_FEMALE', 'BA_MALE', 'BA_FEMALE', 'IA_MALE',
                 'H_MALE', 'H_FEMALE', 'IA_FEMALE', 'AA_MALE', 'AA_FEMALE', 'NA_MALE',
                 'NA_FEMALE', 'TOM_MALE', 'TOM_FEMALE']
    def __init__(self):
        from pymongo import MongoClient
        self.client_az = MongoClient(MongoER.atlas_bamazon_uri)

    @staticmethod
    def test(): # use REST DATA API
        url = "https://data.mongodb-api.com/app/data-jqglk/endpoint/data/beta/action/findOne"
        payload = json.dumps({
            "collection": "ffcs",
            "database": "bamazon",
            "dataSource": "sandbox",
            "projection": {
                "_id": 1
            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': MongoAZ.api_key_AZC
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

    @staticmethod
    def load_ffcs(): # from exported amazon ffcs json file with reduced columns into pandas dataframe
        import os
        jfile = os.path.join(Config.basedir, 'mongo\\ffcs.json')
        with open(jfile) as f:
            d = json.load(f)
            df = pd.DataFrame(d)[MongoAZ.ffcs_cols]
        return df

    #  utility for extracting poll responders by states
    # @staticmethod
    # def get_htmls(df):
    #     import os
    #     for s in ['NY', 'CA', 'AZ', 'TX']:
    #         dfs = df[df.state == s]
    #         dfs.to_html(os.path.join(Config.basedir, f"mongo\\{s}.html"))


class RadioPlaylists(MongoER):
    def __init__(self):
        from pymongo import MongoClient
        self.local_c = MongoClient(MongoER.mongo_local_uri)
        # Mongo db radio on local cluster
        self.db = self.local_c['radio']
        # playlists collection
        self.coll = self.db['playlists']

        # self.client_radio = MongoClient(MongoER.mongo_radio_uri)

    def update_playlist(self, pl_dic):
        fn = pl_dic['filename']
        query = {'filename': fn}
        oldpl = self.coll.find_one(query)
        if oldpl:
            doc1 = self.coll.delete_one(query)
            doc2 = self.coll.insert_one(pl_dic)
            return doc1, doc2
        else:
            raise Exception('query failed')

class RadioDeployments(MongoER):
    def __init__(self):

        self.local_c = MongoClient(MongoER.mongo_local_uri)
        # Mongo db radio on local cluster
        self.db = self.local_c['radio']
        # playlists collection
        self.coll = self.db['deployments']
        # Now Playing Records
        self.coll_npl = self.db['now_playing']

    def insertDeployment(self, doc):
        self.coll.insert_one(doc)

    def update_deployments(self, dep_dic):
        fn = dep_dic['filename']
        query = {'filename': fn}
        oldpl = self.coll.find_one(query)
        if oldpl:
            doc1 = self.coll.delete_one(query)
            doc2 = self.coll.insert_one(dep_dic)
            return doc1, doc2
        else:
            raise Exception('query failed')

    def insert_npl_record(self, tup:tuple):
        self.coll_npl.insert_one({tup[1]:tup[0]})
