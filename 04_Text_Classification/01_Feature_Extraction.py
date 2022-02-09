#!/usr/bin/env python
# coding: utf-8

# # Building a Natural Language Processor From Scratch
# In this section we'll use basic Python to build a rudimentary NLP system. We'll build a *corpus of documents* (two small text files), create a *vocabulary* from all the words in both documents, and then demonstrate a *Bag of Words* technique to extract features from each document.<br>

# In[47]:


get_ipython().run_cell_magic('writefile', '1.txt', 'This is a story about cats\nour feline pets\nCats are furry animals')


# In[48]:


get_ipython().run_cell_magic('writefile', '2.txt', 'This story is about surfing\nCatching waves is fun\nSurfing is a popular water sport')


# ## Build a vocabulary
# The goal here is to build a numerical array from all the words that appear in every document. Later we'll create instances (vectors) for each individual document.

# In[49]:


vocab = {}
i = 1

with open('1.txt') as f:
    x = f.read().lower().split()

for word in x:
    if word in vocab:
        continue
    else:
        vocab[word]=i
        i+=1

print(vocab)


# In[50]:


with open('2.txt') as f:
    x = f.read().lower().split()

for word in x:
    if word in vocab:
        continue
    else:
        vocab[word]=i
        i+=1

print(vocab)


# Even though `2.txt` has 15 words, only 7 new words were added to the dictionary.
# 
# ## Feature Extraction
# Now that we've encapsulated our "entire language" in a dictionary, let's perform *feature extraction* on each of our original documents:

# In[51]:


# Create an empty vector with space for each word in the vocabulary:
one = ['1.txt']+[0]*len(vocab)
one


# In[52]:


# map the frequencies of each word in 1.txt to our vector:
with open('1.txt') as f:
    x = f.read().lower().split()
    
for word in x:
    one[vocab[word]]+=1
    
one


# In[53]:


# Do the same for the second document:
two = ['2.txt']+[0]*len(vocab)

with open('2.txt') as f:
    x = f.read().lower().split()
    
for word in x:
    two[vocab[word]]+=1


# In[54]:


# Compare the two vectors:
print(f'{one}\n{two}')


# ## Bag of Words and Tf-idf
# In the above examples, each vector can be considered a *bag of words*. By itself these may not be helpful until we consider *term frequencies*, or how often individual words appear in documents. A simple way to calculate term frequencies is to divide the number of occurrences of a word by the total number of words in the document. In this way, the number of times a word appears in large documents can be compared to that of smaller documents.
# 
# However, it may be hard to differentiate documents based on term frequency if a word shows up in a majority of documents. To handle this we also consider *inverse document frequency*, which is the total number of documents divided by the number of documents that contain the word. In practice we convert this value to a logarithmic scale, as described [here](https://en.wikipedia.org/wiki/Tf%E2%80%93idf#Inverse_document_frequency).
# 
# Together these terms become [**tf-idf**](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

# ## Stop Words and Word Stems
# Some words like "the" and "and" appear so frequently, and in so many documents, that we needn't bother counting them. Also, it may make sense to only record the root of a word, say `cat` in place of both `cat` and `cats`. This will shrink our vocab array and improve performance.

# ## Tokenization and Tagging
# When we created our vectors the first thing we did was split the incoming text on whitespace with `.split()`. This was a crude form of *tokenization* - that is, dividing a document into individual words. In this simple example we didn't worry about punctuation or different parts of speech. In the real world we rely on some fairly sophisticated *morphology* to parse text appropriately.
# 
# Once the text is divided, we can go back and *tag* our tokens with information about parts of speech, grammatical dependencies, etc. This adds more dimensions to our data and enables a deeper understanding of the context of specific documents. For this reason, vectors become ***high dimensional sparse matrices***.

# 
# # Feature Extraction from Text
# In the **Scikit-learn Primer** lecture we applied a simple SVC classification model to the SMSSpamCollection dataset. We tried to predict the ham/spam label based on message length and punctuation counts. In this section we'll actually look at the text of each message and try to perform a classification based on content. We'll take advantage of some of scikit-learn's [feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) tools.

# In[63]:


import numpy as np
import pandas as pd

df = pd.read_csv('smsspamcollection.tsv', sep='\t')
df.head()


# In[56]:


df.isnull().sum()


# In[58]:


# Is there space in the rows?


# In[59]:


mystring = 'hello'
mystring.isspace()


# In[61]:


empty = ' '
empty.isspace()


# In[65]:


blanks = []

# (index,label,message,length,punct)
for i,lb,m,l,p in df.itertuples():
    if m.isspace():
        blanks.append(i)    


# In[66]:


blanks


# In[68]:


# There is no empty row


# In[13]:


df['label'].value_counts()


# In[14]:


from sklearn.model_selection import train_test_split


# In[15]:


X = df['message']


# In[16]:


y = df['label']


# In[17]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# ### CountVectorizer

# In[18]:


from sklearn.feature_extraction.text import CountVectorizer


# In[19]:


count_vect = CountVectorizer()


# In[21]:


X_train_counts = count_vect.fit_transform(X_train)


# In[22]:


X_train_counts


# In[24]:


X_train.shape


# In[25]:


X_train_counts.shape


# ### Tf-Idf Transformer

# In[26]:


from sklearn.feature_extraction.text import TfidfTransformer


# In[27]:


tfidf_transformer = TfidfTransformer()


# In[28]:


X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


# In[29]:


X_train_tfidf.shape


# ### Combine Steps with TfidVectorizer
# 

# In[30]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[31]:


vectorizer = TfidfVectorizer()


# In[32]:


X_train_tfidf = vectorizer.fit_transform(X_train)


# In[33]:


X_train_tfidf.shape


# ### Model

# In[34]:


from sklearn.svm import LinearSVC


# In[35]:


clf = LinearSVC()


# In[36]:


clf.fit(X_train_tfidf,y_train)


# ### Pipeline

# In[37]:


from sklearn.pipeline import Pipeline


# In[38]:


text_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LinearSVC())
])


# In[39]:


text_clf.fit(X_train,y_train)


# ### Test

# In[40]:


preds = text_clf.predict(X_test)


# In[41]:


from sklearn.metrics import confusion_matrix,classification_report


# In[42]:


print(confusion_matrix(y_test,preds))


# In[43]:


print(classification_report(y_test, preds))


# In[44]:


text_clf.predict(["Hello how are you?"])


# In[46]:


text_clf.predict(["Congratulations! You have been selected as a winner."])


# In[ ]:




