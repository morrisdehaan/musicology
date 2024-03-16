from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import json

LYRICS_FILE = "./res/lyrics.json"

def annotate():
    pass

if __name__ == "__main__":
    nltk.download('vader_lexicon')
    
    analyzer = SentimentIntensityAnalyzer()

    with open(LYRICS_FILE) as f:
        lyrics = json.load(f)

        for i in range(len(lyrics)):
            if 'lyrics' in lyrics[i] and not 'sentiment' in lyrics[i]:
                score = analyzer.polarity_scores(lyrics[i]['lyrics'])
                lyrics[i]['sentiment'] = score['compound']

    with open(LYRICS_FILE, 'w') as f:
        json.dump(lyrics, f, indent=2)
