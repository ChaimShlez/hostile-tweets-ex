from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Processor:
    def __init__(self):
        nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()



    def help_counting(self,text):
        word_counts = Counter(text.split())
        min=float('inf')
        min_word=""

        for k,v in word_counts.items():
            if v < min:
                min = v
                min_word=k
        return min_word

    def find_word_rare(self ,data):


        data['WordRare'] = data['Text'].apply(self.help_counting)
        return data

    def help_counting_finding_emotion_text(self,tweet):
        score = self.analyzer.polarity_scores(tweet)
        compound = score['compound']
        if 1 > compound > 0.5:
            return 'positive'
        elif 0.49 > compound > -0.49:
            return 'neutral'
        elif -1 > compound > -0.5:
            return 'negative'

    def finding_emotion_text(self,data):
        data['Sentiment']= data['Text'].apply(self.help_counting_finding_emotion_text)
        return data







