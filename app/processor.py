from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Processor:
    def __init__(self,data):
        self.df=data
        nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()



    def find_word_rare(self,text):
        word_counts = Counter(text.split())
        min=float('inf')
        min_word=""

        for k,v in word_counts.items():
            if v < min:
                min = v
                min_word=k
        return min_word

    def add_col_rare(self):

        self.df['WordRare'] =  self.df['Text'].apply(self.find_word_rare)


    def finding_emotion_text(self,tweet):
        score = self.analyzer.polarity_scores(tweet)
        compound = score['compound']
        if 0.5 < compound <= 1:
            return 'positive'
        elif -0.49 <= compound <= 0.49:
            return 'neutral'
        elif -1 <= compound < -0.5:
            return 'negative'

    def add_col_sentiment(self):
        self.df['Sentiment']=  self.df['Text'].apply(self.finding_emotion_text)



    def find_weapons(self,text,path):
        with open(path) as f:


            weapons=[line.strip().lower() for line in f]

        words = text.split()
        for weapon in weapons:
            if weapon in words:
                return weapon
        return ""



    def add_col_weapons(self,path):
        self.df['weapons_detected'] = self.df['Text'].apply(lambda x: self.find_weapons(x, path))











