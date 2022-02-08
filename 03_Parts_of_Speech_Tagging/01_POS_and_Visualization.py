#!/usr/bin/env python
# coding: utf-8

# Processing raw text intelligently is difficult: most words are rare, and it's common for words that look completely different to mean almost the same thing. The same words in a different order can mean something completely different. Even splitting text into useful word-like units can be difficult in many languages. While it's possible to solve some problems starting from only the raw characters, it's usually better to use linguistic knowledge to add useful information. That's exactly what spaCy is designed to do: you put in raw text, and get back a **Doc** object, that comes with a variety of annotations.

# In[1]:


import spacy
nlp = spacy.load('en_core_web_sm')


# In[2]:


doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")


# In[3]:


print(doc.text)


# In[4]:


print(doc[4])


# In[5]:


print(doc[4].pos_)


# In[6]:


print(doc[4]._)


# 
# Tokens are subsequently given a fine-grained tag as determined by morphology:
# <table>
# <tr><th>POS</th><th>Description</th><th>Fine-grained Tag</th><th>Description</th><th>Morphology</th></tr>
# <tr><td>ADJ</td><td>adjective</td><td>AFX</td><td>affix</td><td>Hyph=yes</td></tr>
# <tr><td>ADJ</td><td></td><td>JJ</td><td>adjective</td><td>Degree=pos</td></tr>
# <tr><td>ADJ</td><td></td><td>JJR</td><td>adjective, comparative</td><td>Degree=comp</td></tr>
# <tr><td>ADJ</td><td></td><td>JJS</td><td>adjective, superlative</td><td>Degree=sup</td></tr>
# <tr><td>ADJ</td><td></td><td>PDT</td><td>predeterminer</td><td>AdjType=pdt PronType=prn</td></tr>
# <tr><td>ADJ</td><td></td><td>PRP\$</td><td>pronoun, possessive</td><td>PronType=prs Poss=yes</td></tr>
# <tr><td>ADJ</td><td></td><td>WDT</td><td>wh-determiner</td><td>PronType=int rel</td></tr>
# <tr><td>ADJ</td><td></td><td>WP\$</td><td>wh-pronoun, possessive</td><td>Poss=yes PronType=int rel</td></tr>
# <tr><td>ADP</td><td>adposition</td><td>IN</td><td>conjunction, subordinating or preposition</td><td></td></tr>
# <tr><td>ADV</td><td>adverb</td><td>EX</td><td>existential there</td><td>AdvType=ex</td></tr>
# <tr><td>ADV</td><td></td><td>RB</td><td>adverb</td><td>Degree=pos</td></tr>
# <tr><td>ADV</td><td></td><td>RBR</td><td>adverb, comparative</td><td>Degree=comp</td></tr>
# <tr><td>ADV</td><td></td><td>RBS</td><td>adverb, superlative</td><td>Degree=sup</td></tr>
# <tr><td>ADV</td><td></td><td>WRB</td><td>wh-adverb</td><td>PronType=int rel</td></tr>
# <tr><td>CONJ</td><td>conjunction</td><td>CC</td><td>conjunction, coordinating</td><td>ConjType=coor</td></tr>
# <tr><td>DET</td><td>determiner</td><td>DT</td><td>determiner</td><td></td></tr>
# <tr><td>INTJ</td><td>interjection</td><td>UH</td><td>interjection</td><td></td></tr>
# <tr><td>NOUN</td><td>noun</td><td>NN</td><td>noun, singular or mass</td><td>Number=sing</td></tr>
# <tr><td>NOUN</td><td></td><td>NNS</td><td>noun, plural</td><td>Number=plur</td></tr>
# <tr><td>NOUN</td><td></td><td>WP</td><td>wh-pronoun, personal</td><td>PronType=int rel</td></tr>
# <tr><td>NUM</td><td>numeral</td><td>CD</td><td>cardinal number</td><td>NumType=card</td></tr>
# <tr><td>PART</td><td>particle</td><td>POS</td><td>possessive ending</td><td>Poss=yes</td></tr>
# <tr><td>PART</td><td></td><td>RP</td><td>adverb, particle</td><td></td></tr>
# <tr><td>PART</td><td></td><td>TO</td><td>infinitival to</td><td>PartType=inf VerbForm=inf</td></tr>
# <tr><td>PRON</td><td>pronoun</td><td>PRP</td><td>pronoun, personal</td><td>PronType=prs</td></tr>
# <tr><td>PROPN</td><td>proper noun</td><td>NNP</td><td>noun, proper singular</td><td>NounType=prop Number=sign</td></tr>
# <tr><td>PROPN</td><td></td><td>NNPS</td><td>noun, proper plural</td><td>NounType=prop Number=plur</td></tr>
# <tr><td>PUNCT</td><td>punctuation</td><td>-LRB-</td><td>left round bracket</td><td>PunctType=brck PunctSide=ini</td></tr>
# <tr><td>PUNCT</td><td></td><td>-RRB-</td><td>right round bracket</td><td>PunctType=brck PunctSide=fin</td></tr>
# <tr><td>PUNCT</td><td></td><td>,</td><td>punctuation mark, comma</td><td>PunctType=comm</td></tr>
# <tr><td>PUNCT</td><td></td><td>:</td><td>punctuation mark, colon or ellipsis</td><td></td></tr>
# <tr><td>PUNCT</td><td></td><td>.</td><td>punctuation mark, sentence closer</td><td>PunctType=peri</td></tr>
# <tr><td>PUNCT</td><td></td><td>''</td><td>closing quotation mark</td><td>PunctType=quot PunctSide=fin</td></tr>
# <tr><td>PUNCT</td><td></td><td>""</td><td>closing quotation mark</td><td>PunctType=quot PunctSide=fin</td></tr>
# <tr><td>PUNCT</td><td></td><td>``</td><td>opening quotation mark</td><td>PunctType=quot PunctSide=ini</td></tr>
# <tr><td>PUNCT</td><td></td><td>HYPH</td><td>punctuation mark, hyphen</td><td>PunctType=dash</td></tr>
# <tr><td>PUNCT</td><td></td><td>LS</td><td>list item marker</td><td>NumType=ord</td></tr>
# <tr><td>PUNCT</td><td></td><td>NFP</td><td>superfluous punctuation</td><td></td></tr>
# <tr><td>SYM</td><td>symbol</td><td>#</td><td>symbol, number sign</td><td>SymType=numbersign</td></tr>
# <tr><td>SYM</td><td></td><td>\$</td><td>symbol, currency</td><td>SymType=currency</td></tr>
# <tr><td>SYM</td><td></td><td>SYM</td><td>symbol</td><td></td></tr>
# <tr><td>VERB</td><td>verb</td><td>BES</td><td>auxiliary "be"</td><td></td></tr>
# <tr><td>VERB</td><td></td><td>HVS</td><td>forms of "have"</td><td></td></tr>
# <tr><td>VERB</td><td></td><td>MD</td><td>verb, modal auxiliary</td><td>VerbType=mod</td></tr>
# <tr><td>VERB</td><td></td><td>VB</td><td>verb, base form</td><td>VerbForm=inf</td></tr>
# <tr><td>VERB</td><td></td><td>VBD</td><td>verb, past tense</td><td>VerbForm=fin Tense=past</td></tr>
# <tr><td>VERB</td><td></td><td>VBG</td><td>verb, gerund or present participle</td><td>VerbForm=part Tense=pres Aspect=prog</td></tr>
# <tr><td>VERB</td><td></td><td>VBN</td><td>verb, past participle</td><td>VerbForm=part Tense=past Aspect=perf</td></tr>
# <tr><td>VERB</td><td></td><td>VBP</td><td>verb, non-3rd person singular present</td><td>VerbForm=fin Tense=pres</td></tr>
# <tr><td>VERB</td><td></td><td>VBZ</td><td>verb, 3rd person singular present</td><td>VerbForm=fin Tense=pres Number=sing Person=3</td></tr>
# <tr><td>X</td><td>other</td><td>ADD</td><td>email</td><td></td></tr>
# <tr><td>X</td><td></td><td>FW</td><td>foreign word</td><td>Foreign=yes</td></tr>
# <tr><td>X</td><td></td><td>GW</td><td>additional word in multi-word expression</td><td></td></tr>
# <tr><td>X</td><td></td><td>XX</td><td>unknown</td><td></td></tr>
# <tr><td>SPACE</td><td>space</td><td>_SP</td><td>space</td><td></td></tr>
# <tr><td></td><td></td><td>NIL</td><td>missing tag</td><td></td></tr>
# </table>

# In[12]:


for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")


# In[37]:


doc = nlp(u"I read books on NLP.")


# In[38]:


word = doc[1]


# In[39]:


word.text


# In[40]:


token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")


# In[44]:


doc = nlp(u"I read a book on NLP yesterday.")


# In[45]:


word = doc[1]
token = word


# In[46]:


print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")


# ## Counting POS Tags
# The `Doc.count_by()` method accepts a specific token attribute as its argument, and returns a frequency count of the given attribute as a dictionary object. Keys in the dictionary are the integer values of the given attribute ID, and values are the frequency. Counts of zero are not included.

# In[64]:


doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")


# In[48]:


POS_counts = doc.count_by(spacy.attrs.POS)


# In[49]:


POS_counts


# In[50]:


doc.vocab[84].text


# In[52]:


doc[1]


# In[53]:


doc[1].pos


# In[54]:


doc[1].pos_


# In[57]:


for k,v in sorted(POS_counts.items()):
    print(f"{k:{3}} {doc.vocab[k].text:{5}} {v}")


# In[59]:


TAG_counts = doc.count_by(spacy.attrs.TAG)

for k,v in sorted(TAG_counts.items()):
    print(f"{k} {doc.vocab[k].text:{5}} {v}")


# In[60]:


len(doc.vocab)


# In[63]:


DEP_counts = doc.count_by(spacy.attrs.DEP)

for k,v in sorted(DEP_counts.items()):
    print(f'{k} {doc.vocab[k].text:{5}}: {v}')


# # Visualizing Parts of Speech

# In[65]:


from spacy import displacy


# In[68]:


displacy.render(doc, style='dep',jupyter=True, options=options)


# In[67]:


options = {'distance':110, 'compact':'True','color':'yellow','bg':'#09a3d5','font':'Times'}


# ## Customizing the Appearance
# Besides setting the distance between tokens, you can pass other arguments to the `options` parameter:
# 
# <table>
# <tr><th>NAME</th><th>TYPE</th><th>DESCRIPTION</th><th>DEFAULT</th></tr>
# <tr><td>`compact`</td><td>bool</td><td>"Compact mode" with square arrows that takes up less space.</td><td>`False`</td></tr>
# <tr><td>`color`</td><td>unicode</td><td>Text color (HEX, RGB or color names).</td><td>`#000000`</td></tr>
# <tr><td>`bg`</td><td>unicode</td><td>Background color (HEX, RGB or color names).</td><td>`#ffffff`</td></tr>
# <tr><td>`font`</td><td>unicode</td><td>Font name or font family for all text.</td><td>`Arial`</td></tr>
# </table>
# 
# For a full list of options visit https://spacy.io/api/top-level#displacy_options

# In[74]:


doc2 = nlp("This is for Google server. It can be a huge list of Jose sentences.")


# In[75]:


spans = list(doc2.sents)


# In[78]:


displacy.serve(spans, style='ent', options={'distance':110})


# In[ ]:




