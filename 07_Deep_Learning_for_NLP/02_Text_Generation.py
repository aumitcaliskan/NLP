#!/usr/bin/env python
# coding: utf-8

# ### RECURRENT NEURAL NETWORK (RNN)

# Example of Sequences
# 
# * Time Series Data
# * Sentences
# * Audio
# * Car Trajectories
# * Music
# 
# **Recurrent Neuron** sends output back to itself.  
# Input(t=0) ---> Activation function ---> Output(t=0) ---> Input to Activation Function(t+1) ---> Activation Function ---> Output(t+1).  
# These cells are called **memory cells**.  
# 
# RNN are also very flexible in their inputs and outputs:  
# 
# - Sequence to Sequence 
# - Sequence to Vector
# - Vector to Sequence

# ### LONG SHORT-TERM MEMORY (LSTM)

# After awhile the RNN will begin to **forget** the first inputs. So we need **long-term memory** for our networks. **Cell state** decide to forget information and store in cell state. Then update the old cell state. C(t) = f(t)*C(t-1) + i* Chat(t).Final decision is filtered version of cell state. 

# In[3]:


def read_file(filepath):
    with open(filepath) as f:
        str_text = f.read()
    return str_text


# In[4]:


read_file('moby_dick_four_chapters.txt')


# In[38]:


import spacy
import numpy as np
import pandas as pd
from tensorflow import keras


# In[7]:


nlp = spacy.load('en_core_web_sm',disable=['parser','tagger','ner'])


# In[8]:


nlp.max_length = 1198623


# In[9]:


def seperate_punc(doc_text):
    return [token.text.lower() for token in nlp(doc_text) if token.text not in '\n\n \n\n\n!"-#$%&()--.*+,-/:;<=>?@[\\]^_`{|}~\t\n ']

# for not overfitting to punctuation


# In[10]:


d = read_file('moby_dick_four_chapters.txt')


# In[11]:


tokens = seperate_punc(d)


# In[13]:


len(tokens)


# In[14]:


# 25 words ---> network predict 26


# In[15]:


train_len = 25 + 1 

text_sequences = []

for i  in range(train_len, len(tokens)):
    seq = tokens[i-train_len:i]
    
    text_sequences.append(seq)


# In[16]:


type(text_sequences)


# In[21]:


' '.join(text_sequences[0])


# In[22]:


' '.join(text_sequences[1])


# In[23]:


' '.join(text_sequences[2])


# In[24]:


from keras.preprocessing.text import Tokenizer


# In[25]:


tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_sequences)


# In[26]:


sequences = tokenizer.texts_to_sequences(text_sequences)


# In[28]:


sequences[0]


# In[29]:


sequences[1]


# In[ ]:


tokenizer.index_word


# In[33]:


for i in sequences[0]:
    print(f"{i} : {tokenizer.index_word[i]}")


# In[34]:


tokenizer.word_counts


# In[36]:


vocabulary_size = len(tokenizer.word_counts)
vocabulary_size


# In[37]:


type(sequences)


# In[39]:


sequences = np.array(sequences)


# In[40]:


sequences


# In[42]:


from tensorflow.keras.utils import to_categorical


# In[43]:


X = sequences[:,:-1]


# In[44]:


y = sequences[:,-1]


# In[45]:


y = to_categorical(y, num_classes=vocabulary_size+1)


# In[47]:


seq_len = X.shape[1]


# In[48]:


X.shape


# In[52]:


from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding


# In[54]:


def create_model(vocabulary_size, seq_len):
    
    model = Sequential()
    model.add(Embedding(vocabulary_size, seq_len, input_length=seq_len))
    model.add(LSTM(50,return_sequences=True))
    model.add(LSTM(50))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(vocabulary_size,activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
              
    return model


# In[55]:


model = create_model(vocabulary_size+1,seq_len)


# In[56]:


from pickle import dump,load


# In[58]:


model.fit(X,y,batch_size=128,epochs=20,verbose=1)


# In[59]:


model.save('mobydick.h5')


# In[60]:


dump(tokenizer, open('my_tokenizer','wb'))


# In[71]:


from keras.preprocessing.sequence import pad_sequences

def generate_text(model, tokenizer, seq_len, seed_text, num_gen_words):

    output_text = []
    input_text = seed_text
    
    # Create num_gen_words
    for i in range(num_gen_words):
        
        # Take the input text string and encode it to a sequence
        encoded_text = tokenizer.texts_to_sequences([input_text])[0]
        
        # Pad sequences to our trained rate (50 words in the video)
        pad_encoded = pad_sequences([encoded_text], maxlen=seq_len, truncating='pre')
        
        # Predict Class Probabilities for each word
        pred_word_ind = model.predict(pad_encoded, verbose=0).argmax(axis=1)[0]
        
        # Grab word
        pred_word = tokenizer.index_word[pred_word_ind] 
        
        # Update the sequence of input text (shifting one over with the new word)
        input_text += ' ' + pred_word
        
        output_text.append(pred_word)
        
    # Make it look like a sentence.
    return ' '.join(output_text)


# In[62]:


text_sequences[0]


# In[63]:


np.random.seed(101)
random_pick = np.random.randint(0, len(text_sequences))


# In[66]:


random_seed_text = text_sequences[random_pick]
random_seed_text


# In[67]:


seed_text = ' '.join(random_seed_text)
seed_text


# In[72]:


generate_text(model,tokenizer,seq_len,seed_text=seed_text,num_gen_words=25)


# In[73]:


# epochs should be increased


# In[ ]:




