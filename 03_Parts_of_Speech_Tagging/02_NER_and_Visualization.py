#!/usr/bin/env python
# coding: utf-8

# # Named Entity Recognition (NER)
# spaCy has an **'ner'** pipeline component that identifies token spans fitting a predetermined set of named entities. These are available as the `ents` property of a `Doc` object.

# In[1]:


import spacy


# In[2]:


nlp = spacy.load('en_core_web_sm')


# In[4]:


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
    else:
        print('No entities found.')


# In[5]:


doc = nlp("Hi. How are you?")


# In[7]:


show_ents(doc)


# In[8]:


doc = nlp("I want to go to Tokyo next August to see the Tokyo Tower.")


# In[9]:


show_ents(doc)


# ## Entity annotations
# `Doc.ents` are token spans with their own set of annotations.
# <table>
# <tr><td>`ent.text`</td><td>The original entity text</td></tr>
# <tr><td>`ent.label`</td><td>The entity type's hash value</td></tr>
# <tr><td>`ent.label_`</td><td>The entity type's string description</td></tr>
# <tr><td>`ent.start`</td><td>The token span's *start* index position in the Doc</td></tr>
# <tr><td>`ent.end`</td><td>The token span's *stop* index position in the Doc</td></tr>
# <tr><td>`ent.start_char`</td><td>The entity text's *start* index position in the Doc</td></tr>
# <tr><td>`ent.end_char`</td><td>The entity text's *stop* index position in the Doc</td></tr>
# </table>
# 
# 

# In[10]:


doc = nlp("Can I please  have 500 dollars of  Microsoft stock?")


# In[11]:


show_ents(doc)


# In[12]:


doc = nlp("Tesla to build a U.K. factory for $6 million.")


# In[13]:


show_ents(doc)


# In[14]:


# couldn't recognize Tesla as ORG


# ## NER Tags
# Tags are accessible through the `.label_` property of an entity.
# <table>
# <tr><th>TYPE</th><th>DESCRIPTION</th><th>EXAMPLE</th></tr>
# <tr><td>`PERSON`</td><td>People, including fictional.</td><td>*Fred Flintstone*</td></tr>
# <tr><td>`NORP`</td><td>Nationalities or religious or political groups.</td><td>*The Republican Party*</td></tr>
# <tr><td>`FAC`</td><td>Buildings, airports, highways, bridges, etc.</td><td>*Logan International Airport, The Golden Gate*</td></tr>
# <tr><td>`ORG`</td><td>Companies, agencies, institutions, etc.</td><td>*Microsoft, FBI, MIT*</td></tr>
# <tr><td>`GPE`</td><td>Countries, cities, states.</td><td>*France, UAR, Chicago, Idaho*</td></tr>
# <tr><td>`LOC`</td><td>Non-GPE locations, mountain ranges, bodies of water.</td><td>*Europe, Nile River, Midwest*</td></tr>
# <tr><td>`PRODUCT`</td><td>Objects, vehicles, foods, etc. (Not services.)</td><td>*Formula 1*</td></tr>
# <tr><td>`EVENT`</td><td>Named hurricanes, battles, wars, sports events, etc.</td><td>*Olympic Games*</td></tr>
# <tr><td>`WORK_OF_ART`</td><td>Titles of books, songs, etc.</td><td>*The Mona Lisa*</td></tr>
# <tr><td>`LAW`</td><td>Named documents made into laws.</td><td>*Roe v. Wade*</td></tr>
# <tr><td>`LANGUAGE`</td><td>Any named language.</td><td>*English*</td></tr>
# <tr><td>`DATE`</td><td>Absolute or relative dates or periods.</td><td>*20 July 1969*</td></tr>
# <tr><td>`TIME`</td><td>Times smaller than a day.</td><td>*Four hours*</td></tr>
# <tr><td>`PERCENT`</td><td>Percentage, including "%".</td><td>*Eighty percent*</td></tr>
# <tr><td>`MONEY`</td><td>Monetary values, including unit.</td><td>*Twenty Cents*</td></tr>
# <tr><td>`QUANTITY`</td><td>Measurements, as of weight or distance.</td><td>*Several kilometers, 55kg*</td></tr>
# <tr><td>`ORDINAL`</td><td>"first", "second", etc.</td><td>*9th, Ninth*</td></tr>
# <tr><td>`CARDINAL`</td><td>Numerals that do not fall under another type.</td><td>*2, Two, Fifty-two*</td></tr>
# </table>

# In[15]:


from  spacy.tokens import Span


# In[16]:


ORG = doc.vocab.strings["ORG"]


# In[17]:


ORG


# In[18]:


new_ent = Span(doc,0,1,label=ORG)


# In[19]:


doc.ents = list(doc.ents) + [new_ent]


# In[20]:


show_ents(doc)


# ## Adding Named Entities to All Matching Spans

# In[24]:


doc = nlp('Our company plans to introduce a new vacuum cleaner. '
          'If successful, the vacuum-cleaner will be our best product.')


# In[25]:


show_ents(doc)


# In[26]:


from spacy.matcher import PhraseMatcher


# In[27]:


matcher = PhraseMatcher(nlp.vocab)


# In[30]:


phrase_list = ['vacuum cleaner','vacuum-cleaner']


# In[31]:


phrase_patterns = [nlp(text) for text in phrase_list]


# In[33]:


matcher.add('new product', None, *phrase_patterns)


# In[34]:


found_matches = matcher(doc)


# In[35]:


found_matches


# In[36]:


PROD = doc.vocab.strings["PRODUCT"]


# In[39]:


new_ents = [Span(doc,match[1],match[2],label=PROD) for match in found_matches]


# In[42]:


doc.ents = list(doc.ents) + new_ents


# In[43]:


show_ents(doc)


# ## Counting Entities

# In[44]:


doc = nlp(u'Originally priced at $29.50, the sweater was marked down to five dollars.')


# In[45]:


show_ents(doc)


# In[47]:


[ent for ent in doc.ents if ent.label_ == "MONEY"]


# In[48]:


doc.ents


# # Visualizing Named Entities
# Besides viewing Part of Speech dependencies with `style='dep'`, **displaCy** offers a `style='ent'` visualizer:

# In[51]:


from spacy import displacy


# In[64]:


doc = nlp(u'Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million. '
         u'By contrast, Sony sold only 7 thousand Walkman music players.')


# In[65]:


displacy.render(doc, style='ent', jupyter=True)


# In[66]:


for sent in doc.sents:
    displacy.render(nlp(sent.text), style='ent', jupyter=True)


# In[71]:


colors = {'ORG':'linear-gradient(90deg, #aa9cfc, #fc9ce7)','PRODUCT':'radial-gradient(yellow, green)'}
options = {'ents':['PRODUCT','ORG'],'colors':colors}


# In[72]:


displacy.render(doc, style='ent', jupyter=True, options=options)


# In[ ]:




