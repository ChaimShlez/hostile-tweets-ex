import pandas as pd
from app.fetcher import Fetcher
from app.processor import Processor

class Manager:
    def __init__(self):
        self.path=r"C:\Users\User\development\data\hostile-tweets-ex\data\weapons.txt"

    def run(self):
        fetcher=Fetcher()



        data = pd.DataFrame(fetcher.get_data())
        proc = Processor(data)
        print(proc.df.head())
        # data = fetcher.get_data()
        proc.find_word_rare()
        print(data.columns)
        proc.finding_emotion_text()
        print(data.columns)
        proc.find_weapons(self.path)


        proc.df.rename(columns={'TweetID': 'id','Text':'original_text','WordRare':'rarest_word',}, inplace=True)

        return proc.df.to_dict(orient='records')








