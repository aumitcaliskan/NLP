#!/usr/bin/env python
# coding: utf-8

# * NMF is an unsupervised algorithm that simultaneously performs dimensionality reduction and clustering. We can use it in conjuction with TF-IDF to model topics across documents
# * Data matrix A is a non-negative (n x m) ---> Basis Vectors W (n x k) x Coefficient Matrix H (k x m)
# 
# 1. Construct vector space model for documents(after stopword filtering), result in a term-document matrix A
# 2. Apply TF-IDF term weight normalisation to A
# 3. Normalize TF-IDF vectors to  unit length
# 4. Inıtialise factors using NNDSVD on A
# 5. Apply Projected Gradient NMF to A
# 
# **We need to select k**

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('npr.csv')


# In[3]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[4]:


tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')

# min_df = 2 show words at least shown up in 2 documents


# In[5]:


dtm = tfidf.fit_transform(df['Article'])


# In[6]:


dtm


# In[7]:


from sklearn.decomposition import NMF


# In[8]:


nmf_model = NMF(n_components=7, random_state=42)


# In[9]:


nmf_model.fit(dtm)


# In[11]:


tfidf.get_feature_names_out()[2300]


# In[12]:


for i, topic in enumerate(nmf_model.components_):
    print(f"The top 15 words for topic # {i}")
    print([tfidf.get_feature_names_out()[index] for index in topic.argsort()[-15:]])


# In[15]:


topic_results = nmf_model.transform(dtm)


# In[19]:


topic_results.argmax(axis=1)


# In[20]:


df['Topic'] = topic_results.argmax(axis=1)


# In[23]:


topic_dict = {0:'Healthcare', 1:'Politics', 2:'Healtcare Politics', 3:'Foreign Affairs', 4:'Democrats', 5:'Music', 6:'Education'}
df['Topic_Label'] = df['Topic'].map(topic_dict)

df.head()


# In[ ]:




