import pandas as pd
from app.fetcher import Fetcher
from app.processor import Processor

class Manager:
    def __init__(self):
        self.path="../data/weapons.txt"
        self.data=self.run()

    def run(self):
        fetcher=Fetcher()



        data = pd.DataFrame(fetcher.get_data())
        proc = Processor(data)
        print(proc.df.head())
        # data = fetcher.get_data()
        proc.add_col_rare()
        print(data.columns)
        proc.add_col_sentiment()
        print(data.columns)
        proc.add_col_weapons(self.path)


        proc.df.rename(columns={'TweetID': 'id','Text':'original_text','WordRare':'rarest_word',}, inplace=True)

        return proc.df.to_dict(orient='records')


    def display(self):
        return self.data








