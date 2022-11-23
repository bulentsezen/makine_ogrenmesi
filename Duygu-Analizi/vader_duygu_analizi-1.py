import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_Vader(text):
    over_all_polarity = sid.polarity_scores(text)
    print(over_all_polarity)
    if over_all_polarity['compound'] >= 0.05:
        return "pozitif"
    elif over_all_polarity['compound'] <= -0.05:
        return "negatif"
    else:
        return "nötr"


sid = SentimentIntensityAnalyzer()

data_file = pd.read_excel('online_egitim.xlsx')
# print(data_file)

data_file['duygu'] = data_file['metin'].apply(lambda x: sentiment_Vader(x))
csv_data = data_file.to_excel('vader_duygu.xlsx')