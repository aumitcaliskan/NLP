#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import movie_reviews


# In[4]:


import nltk
nltk.download('movie_reviews')


# In[5]:


movie_reviews.categories()


# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('moviereviews.tsv',sep='\t')


# In[14]:


df.head()


# In[7]:


df.info()


# In[6]:


df.dropna(inplace=True)


# In[8]:


# Is there space string?


# In[9]:


blanks = []

for i,l,r in df.itertuples():
    if type(r) == str:
        if r.isspace():
            blanks.append(i)        


# In[23]:


blanks


# In[12]:


df.drop(blanks,inplace=True)


# In[19]:


df.reset_index(drop=True, inplace=True)


# In[24]:


df['label'].value_counts()


# In[25]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[26]:


sid = SentimentIntensityAnalyzer()


# In[29]:


df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))


# In[35]:


df['compound_score'] = df['scores'].apply(lambda d: d['compound'])


# In[38]:


df['compound_label'] = df['compound_score'].apply(lambda label: 'pos' if label >= 0 else 'neg')


# In[39]:


df


# In[41]:


from sklearn.metrics import accuracy_score, confusion_matrix,classification_report


# In[42]:


accuracy_score(df['label'],df['compound_label'])


# In[43]:


confusion_matrix(df['label'],df['compound_label'])


# In[44]:


print(classification_report(df['label'],df['compound_label']))


# So, it looks like VADER couldn't judge the movie reviews very accurately. This demonstrates one of the biggest challenges in sentiment analysis - understanding human semantics. Many of the reviews had positive things to say about a movie, reserving final judgement to the last sentence.

# In[ ]:




