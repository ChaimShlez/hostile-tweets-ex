import pandas as pd
from app.fetcher import Fetcher
from app.processor import Processor

class Manager:
    def __init__(self):
        pass

    def run(self):
        fetcher=Fetcher()
        proc=Processor()


        data = pd.DataFrame(fetcher.get_data())
        # data = fetcher.get_data()
        data=proc.find_word_rare(data)
        print(data.columns)
        data=proc.finding_emotion_text(data)
        print(data.columns)



if __name__ == '__main__':
    m = Manager()
    m.run()
