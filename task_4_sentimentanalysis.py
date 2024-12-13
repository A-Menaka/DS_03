import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the dataset
df = pd.read_csv('twitter_training.csv', encoding='ISO-8859-1')

# Sentiment Distribution for each Topic (Bar Plot)
plt.figure(figsize=(10, 6))
sns.countplot(x='Sentiment', data=df, palette='viridis')
plt.title('Sentiment Distribution across All Topics')
plt.show()

# Sentiment Distribution by Topic
plt.figure(figsize=(12, 8))
sns.countplot(x='Topic', hue='Sentiment', data=df, palette='Set2')
plt.xticks(rotation=45, ha="right")
plt.title('Sentiment Distribution by Topic')
plt.show()

# WordCloud for Positive Sentiment
positive_text = ' '.join(df[df['Sentiment'] == 'Positive']['Text'].dropna())
wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.title('WordCloud for Positive Sentiment')
plt.axis('off')
plt.show()

# WordCloud for Negative Sentiment
negative_text = ' '.join(df[df['Sentiment'] == 'Negative']['Text'].dropna())
wordcloud_negative = WordCloud(width=800, height=400, background_color='black').generate(negative_text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.title('WordCloud for Negative Sentiment')
plt.axis('off')
plt.show()

# Sentiment Summary by Topic
sentiment_summary = df.groupby(['Topic', 'Sentiment']).size().unstack().fillna(0)
sentiment_summary_percentage = sentiment_summary.div(sentiment_summary.sum(axis=1), axis=0) * 100
print("Sentiment Summary by Topic (in %):")
print(sentiment_summary_percentage)

# Top Topics Summary
top_topics = df['Topic'].value_counts().head(3)
print("\nTop Topics with the highest number of tweets:")
print(top_topics)
