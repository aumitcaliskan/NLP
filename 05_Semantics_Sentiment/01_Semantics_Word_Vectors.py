#!/usr/bin/env python
# coding: utf-8

# # Word Vectors
# Word vectors - also called *word embeddings* - are mathematical descriptions of individual words such that words that appear frequently together in the language will have similar values. In this way we can mathematically derive *context*. As mentioned above, the word vector for "lion" will be closer in value to "cat" than to "dandelion".

# In[42]:


import spacy
nlp = spacy.load('en_core_web_md') 


# In[5]:


nlp('The quick brown fox jumped').vector.shape


# In[6]:


nlp('fox').vector.shape


# In[7]:


tokens = nlp('lion cat pet')


# In[8]:


for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# In[9]:


tokens = nlp('like love hate')


# In[10]:


for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# In[13]:


nlp.vocab.vectors.shape


# In[29]:


tokens = nlp('dog cat nargle')


# In[30]:


for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)


# ## Vector arithmetic
# 
# "king" - "man" + "woman" = "queen" ???
# 

# In[43]:


from scipy import spatial


# In[44]:


cosine_similarity = lambda vec1,vec2: 1-spatial.distance.cosine(vec1,vec2)


# In[62]:


prince = nlp.vocab['prince'].vector
man = nlp.vocab['man'].vector
woman= nlp.vocab['woman'].vector


# In[63]:


new_vector = prince - man + woman


# In[64]:


computed_similarities = []

for word in nlp.vocab:
    if word.has_vector:
        if word.is_lower:
            if word.is_alpha:
                similarity = cosine_similarity(new_vector,word.vector)
                computed_similarities.append((word, similarity))


# In[65]:


computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])


# In[66]:


print([t[0].text for t in computed_similarities[:10]])


# In[ ]:




