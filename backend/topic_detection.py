from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

import nltk
nltk.download("stopwords")
nltk.download("punkt_tab")

# Predefined STEM topics
STEM_TOPICS = {
    "Physics": ["force", "gravity", "motion", "energy", "light", "quantum", "particle", "wave", "mechanics"],
    "Chemistry": ["molecule", "atom", "reaction", "chemical", "bond", "acid", "base", "solution"],
    "Biology": ["cell", "dna", "gene", "organism", "evolution", "protein", "species", "enzyme"],
    "Mathematics": ["algebra", "geometry", "calculus", "probability", "equation", "function", "derivative"]
    #"Computer Science": ["algorithm", "data", "ai", "machine", "learning", "network", "python", "programming"]
}

STOPWORDS = set(stopwords.words("english"))

def detect_topic(request_text: str):
    # 1. Tokenize + remove punctuation + lowercase
    tokens = word_tokenize(request_text)
    words = [w.lower() for w in tokens if w.isalpha() and w.lower() not in STOPWORDS]

    # 2. Count matches per STEM topic
    topic_scores = {topic: 0 for topic in STEM_TOPICS}
    for topic, keywords in STEM_TOPICS.items():
        for word in words:
            if word in keywords:
                topic_scores[topic] += 1

    # 3. Select topic with highest score
    detected_topic = max(topic_scores, key=topic_scores.get)

    # 4. If no keywords matched, fallback
    if topic_scores[detected_topic] == 0:
        detected_topic = "General STEM"

    return detected_topic
