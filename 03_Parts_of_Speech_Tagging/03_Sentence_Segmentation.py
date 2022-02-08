#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
nlp = spacy.load('en_core_web_sm')


# In[2]:


doc = nlp('This is the first sentence. This is another sentence. This is the last sentence.')


# In[3]:


for sent in doc.sents: # doc.sents is a generator
    print(sent)


# In[4]:


doc.sents[0]


# In[5]:


list(doc.sents)


# In[6]:


doc_sents = [sent for sent in doc.sents]
type(doc_sents[1])


# In[7]:


doc = nlp('"Management is doing the right things; leadership is doing the right things." - Peter Drucker')


# In[8]:


doc.text


# In[9]:


for sent in doc.sents: 
    print(sent)
    print('\n')


# ## Add a Segmentation Rule

# In[76]:


from spacy.language import Language

@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
    return doc


# In[77]:


nlp.add_pipe("set_custom_boundaries",before='parser')


# In[78]:


nlp.pipe_names


# In[79]:


doc4 = nlp('"Management is doing the right things; leadership is doing the right things." - Peter Drucker')


# In[80]:


for sent in doc4.sents:
    print(sent)
    print('\n')


# https://spacy.io/usage/linguistic-features#sbd

# In[ ]:




