#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('quora_questions.csv')


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[7]:


tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')


# In[8]:


dtm = tfidf.fit_transform(df['Question'])


# In[9]:


dtm


# In[10]:


from sklearn.decomposition import NMF


# In[24]:


nmf_model = NMF(n_components=20, random_state=42)


# In[25]:


nmf_model.fit(dtm)


# In[26]:


tfidf.get_feature_names_out()[11010]


# In[27]:


nmf_model.components_


# In[28]:


for i,topic in enumerate(nmf_model.components_):
    print(f"The top 15 words for topic #{i}")
    print([tfidf.get_feature_names_out()[index] for index in topic.argsort()[-15:]])


# In[20]:


topic_results = nmf_model.transform(dtm)


# In[21]:


topic_results.argmax(axis=1)


# In[22]:


df['Topic'] = topic_results.argmax(axis=1)


# In[23]:


df


# In[ ]:




