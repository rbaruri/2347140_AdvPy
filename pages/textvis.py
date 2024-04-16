import streamlit as st

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
import re
from nltk import FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('all')

st.title('Text Visualization')

df = pd.read_csv('WomensClothingE-CommerceReviews.csv')


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

    
def preprocess_text(review_text):
    
    review_text = re.sub(r'<.*?>', '', review_text)
    
    
    tokenizer = RegexpTokenizer(r'\b[a-zA-Z]{2,}\b')
    
    
    tokens = tokenizer.tokenize(review_text)
    
    
    stop_words = set(stopwords.words('english'))
    
    
    tokens = [token.lower() for token in tokens if token.lower() not in stop_words]
    
    
    lemmatizer = WordNetLemmatizer()
    
    
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return lemmatized_tokens

preprocessed_texts = [preprocess_text(str(text)) for text in df['ReviewText']]


for i in range(5):
    print(f'Review {i + 1}: {preprocessed_texts[i]}')



all_text = ' '.join([' '.join(tokens) for tokens in preprocessed_texts])

wordcloud = WordCloud(width=800, height=400, max_words=50).generate(all_text)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(wordcloud)
ax.axis('off')

st.pyplot(fig)


all_tokens = []

for tokens in preprocessed_texts:
    all_tokens.extend(tokens)

fd = FreqDist(all_tokens)

most_common_words = fd.most_common(5)

st.write("The 5 most frequent words and their frequencies:")
for word, frequency in most_common_words:
    st.write(f"{word}: {frequency}")
    
    
general_reviews = df[df['Division Name'] == 'General']['ReviewText']
general_petite_reviews = df[df['Division Name'] == 'General Petite']['ReviewText']
initmates_reviews = df[df['Division Name'] == 'Initmates']['ReviewText']


general_reviews = general_reviews.dropna()
general_petite_reviews = general_petite_reviews.dropna()
initmates_reviews = initmates_reviews.dropna()


vectorizer = TfidfVectorizer()
general_vector = vectorizer.fit_transform(general_reviews)
general_petite_vector = vectorizer.transform(general_petite_reviews)
initmates_vector = vectorizer.transform(initmates_reviews)


labels = ['General and General Petite', 'General and Intimates', 'General Petite and Intimates']
scores = [cosine_similarity(general_vector, general_petite_vector)[0][0], cosine_similarity(general_vector, initmates_vector)[0][0], cosine_similarity(general_petite_vector, initmates_vector)[0][0]]

fig, ax = plt.subplots()
ax.bar(labels, scores, color=['red', 'purple', 'blue'])
ax.set_xlabel('Pair of Divisions')
ax.set_ylabel('Cosine Similarity Score')
ax.set_title('Comparison of Cosine Similarity Scores between Different Divisions')

st.pyplot(fig)

