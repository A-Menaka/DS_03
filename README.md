# PRODIGY_DS_03
Task 3 - Data Science internship at Prodigy InfoTech

Sentiment Analysis on Social Media Data

Task Overview
This task analyzes sentiment patterns in social media data, specifically from Twitter, to understand public opinion and attitudes towards specific topics or brands. Using a Kaggle dataset, the sentiment of tweets is categorized into Positive, Negative, Neutral, and Irrelevant. The goal is to explore sentiment trends and identify how the public feels about various topics based on social media conversations.

Dataset
The dataset used in this task is the Twitter Entity Sentiment Analysis dataset, which contains tweets related to various topics or brands. You can access the dataset on Kaggle here.

Columns in the Dataset:
ID: Unique identifier for the tweet.
Topic: The topic or brand mentioned in the tweet.
Sentiment: The sentiment associated with the tweet (Positive, Negative, Neutral, Irrelevant).
Text: The actual content of the tweet.

Tools and Libraries Used
Python: The primary programming language.
Pandas: For data manipulation and analysis.
Matplotlib and Seaborn: For visualizing the sentiment data.
TextBlob: For analyzing the sentiment of tweets.
WordCloud: To visualize frequent words in Positive and Negative tweets.

Steps Involved

Data Loading:
The dataset is loaded from a CSV file.
Data is preprocessed to remove missing values or irrelevant entries.

Sentiment Analysis:
Sentiment is classified into four categories: Positive, Negative, Neutral, and Irrelevant.
TextBlob is used to perform sentiment analysis on each tweet's text.

Data Visualization:
The sentiment distribution for each topic is calculated and visualized.
A sentiment summary (in percentages) is created for the top topics.

Sentiment Summary:
Sentiment percentages for each topic are presented to show how the public feels about the topic.
Topics with the highest tweet counts are identified.

Word Clouds:
Word clouds are generated to visualize the most common words in tweets categorized by Positive and Negative sentiments for each topic.

Outputs
1. Sentiment Distribution Summary
For each topic, sentiment distribution is calculated as a percentage of the total tweets for that topic.
Sentiment Summary by Topic (in %):
Sentiment                          Irrelevant   Negative    Neutral   Positive
Topic
Amazon                               8.29       24.87      53.37     13.47
ApexLegends                          8.08       25.25      39.65     27.02
AssassinsCreed                       11.76      16.84      6.95      64.44

3. Top Topics with the Highest Number of Tweets
The top topics based on the highest number of tweets are:
Top Topics with the Highest Number of Tweets:
Topic
Microsoft               2400
MaddenNFL               2400
TomClancysRainbowSix    2400

4. Word Clouds
Word clouds are generated to visualize frequent words in Positive and Negative tweets for each topic. These visualizations help identify trends in the language used in tweets based on sentiment.

How to Run the Code
Clone the repository or download the task files.
Install the required libraries by running:

pip install pandas seaborn matplotlib textblob wordcloud

Run the script:
python task_4_sentimentanalysis.py

Conclusion
This sentiment analysis task helps uncover insights from social media data, focusing on understanding how people feel about various topics or brands. The visualizations and sentiment summaries enable a better understanding of public opinion trends, helping to shape strategies for brands or topics based on consumer sentiment.
