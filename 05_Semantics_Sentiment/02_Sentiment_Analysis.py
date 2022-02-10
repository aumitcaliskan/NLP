#!/usr/bin/env python
# coding: utf-8

# ## Broad Steps:
# * First, consider the text being analyzed. A model trained on paragraph-long movie reviews might not be effective on tweets. Make sure to use an appropriate model for the task at hand.
# * Next, decide the type of analysis to perform. A bag-of-words technique that considered only single tokens, or *unigrams*. Some rudimentary sentiment analysis models go one step further, and consider two-word combinations, or *bigrams*. We'd like to work with complete sentences, and for this we're going to import a trained NLTK lexicon called *VADER*.
# 
# * Sentiment analysis aims to determine the attitude of a speaker, writer, or other subject with respect to some topic or the overall contextual polarity or emotional reaction to a document, interaction, or event.
# 
# * VADER (Valence Aware Dictionary for Sentiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) and intensity(strength) of emotion. It is available in the NLTK.
# 
# * Positive and Negative sentiment in the same text data
# * Sarcasm using positive words in a negative way

# ### NLTK's VADER module
# VADER is an NLTK module that provides sentiment scores based on words used ("completely" boosts a score, while "slightly" reduces it), on capitalization & punctuation ("GREAT!!!" is stronger than "great.")(strength), and negations (words like "isn't" and "doesn't" affect the outcome).
# <br>To view the source code visit https://www.nltk.org/_modules/nltk/sentiment/vader.html

# In[1]:


import nltk


# In[2]:


nltk.download('vader_lexicon')


# In[3]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[4]:


sid = SentimentIntensityAnalyzer()


# VADER's `SentimentIntensityAnalyzer()` takes in a string and returns a dictionary of scores in each of four categories:
# * negative
# * neutral
# * positive
# * compound *(computed by normalizing the scores above)*

# In[13]:


a = 'This is a good movie'


# In[14]:


sid.polarity_scores(a)


# In[15]:


b = 'This was the best, most awesome movie EVER MADE!!!'
sid.polarity_scores(b)


# In[17]:


c = 'This was the WORST movie that has ever disgraced the screen.'
sid.polarity_scores(c)


# In[18]:


import pandas as pd
df = pd.read_csv('amazonreviews.tsv', sep='\t')


# In[20]:


df.tail()


# In[21]:


df['label'].value_counts()


# In[22]:


df.dropna(inplace=True)


# In[23]:


blanks = []

for i,l,r in df.itertuples():
    if type(r) == str:
        if  r.isspace():
            blanks.append(i)


# In[24]:


blanks


# In[26]:


df.iloc[0]['review']


# In[25]:


sid.polarity_scores(df.iloc[0]['review'])


# In[27]:


df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))


# In[28]:


df.head()


# In[29]:


df['compound'] = df['scores'].apply(lambda d:d['compound'])


# In[30]:


df.head()


# In[44]:


df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')


# In[45]:


df.head()


# In[46]:


from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


# In[47]:


accuracy_score(df['label'],df['comp_score'])


# In[48]:


confusion_matrix(df['label'],df['comp_score'])


# In[49]:


print(classification_report(df['label'],df['comp_score']))


# In[ ]:





# In[ ]:




