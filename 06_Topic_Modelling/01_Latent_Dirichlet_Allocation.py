#!/usr/bin/env python
# coding: utf-8

# Topic Modelling allows us to analyse large volumes of **unlabeled** text by clustering documents into topics. ---> Unsupervised Machine Learning
# 
# 1) LDA (Latent Dirichlet Allocation)  
# 2) NMF (Non-negative Matrix Factorization)

# ## LDA
# 
# **Assumptions**
# * Documents are probability distributions over latent topics
# * Topics themselves are probability distributions over words
# 
# **How it works**
# * Decide on the  number of words N the document will have
# * Choose a topic mixture for the document(according to a Dirichleet distribution over a fixed set of K topics. e.g. 60% business, 20% politics, 20% food)
# * Generate each word in the document: using topic to generate the word itself. e.g. if we selected food topic, word apple with %60, money %30 probability.

# In[28]:


import numpy as np
import pandas as pd


# In[10]:


df = pd.read_csv('npr.csv')


# In[11]:


df.head()


# In[12]:


df.info()


# In[7]:


npr['Article'][0]


# In[8]:


from sklearn.feature_extraction.text import CountVectorizer


# In[9]:


cv = CountVectorizer(max_df=0.9,min_df=2, stop_words='english')


# **`max_df`**` : float in range [0.0, 1.0] or int, default=1.0`<br>
# When building the vocabulary ignore terms that have a document frequency strictly higher than the given threshold (corpus-specific stop words). If float, the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.
# 
# **`min_df`**` : float in range [0.0, 1.0] or int, default=1`<br>
# When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold. This value is also called cut-off in the literature. If float, the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.

# In[13]:


dtm = cv.fit_transform(df['Article'])


# In[14]:


dtm


# In[15]:


from sklearn.decomposition import LatentDirichletAllocation


# In[16]:


LDA = LatentDirichletAllocation(n_components=7,random_state=42)


# In[17]:


LDA.fit(dtm)


# ### Grab the vocabulary of words

# In[21]:


len(cv.get_feature_names_out())


# In[26]:


type(cv.get_feature_names_out())


# In[27]:


cv.get_feature_names_out()[50000]


# In[41]:


random_word_id = np.random.randint(0,54777)

cv.get_feature_names_out()[random_word_id]


# ### Grab the topics

# In[42]:


len(LDA.components_)


# In[43]:


type(LDA.components_)


# In[44]:


LDA.components_.shape


# In[45]:


LDA.components_


# In[46]:


single_topic = LDA.components_[0]


# In[47]:


single_topic.argsort()


# In[49]:


arr = np.array([10,200,1])


# In[50]:


arr.argsort()


# In[52]:


# 10 greatest values
single_topic.argsort()[-10:]


# In[55]:


top_ten_words = single_topic.argsort()[-20:]


# In[56]:


for i in top_ten_words:
    print(cv.get_feature_names_out()[i])


# ### Grab the highest probability words per topic

# In[59]:


for i,topic in enumerate(LDA.components_):
    print(f"The Top 15 words for topic #{i}")
    print([cv.get_feature_names_out()[index] for index in topic.argsort()[-15:]])
    print('\n')


# In[60]:


dtm


# In[61]:


df


# In[62]:


topic_results = LDA.transform(dtm)


# In[66]:


topic_results[0].round(2)


# In[68]:


df['Article'][0]


# In[69]:


topic_results[0].argmax()


# In[70]:


df['Topic'] = topic_results.argmax(axis=1)


# In[72]:


df.head(10)


# In[ ]:




