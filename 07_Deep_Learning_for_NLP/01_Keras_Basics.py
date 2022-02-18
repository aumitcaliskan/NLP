#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


# In[2]:


iris = load_iris()


# In[3]:


type(iris)


# In[4]:


print(iris.DESCR)


# In[5]:


X = iris.data


# In[6]:


X


# In[7]:


y = iris.target


# In[8]:


y


# In[9]:


from tensorflow.keras.utils import to_categorical


# In[10]:


y = to_categorical(y)


# In[11]:


y


# In[12]:


from sklearn.model_selection import train_test_split


# In[13]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[14]:


from sklearn.preprocessing import MinMaxScaler


# In[15]:


scaler = MinMaxScaler()


# In[16]:


scaled_X_train = scaler.fit_transform(X_train)


# In[17]:


scaled_X_test = scaler.transform(X_test)


# In[19]:


from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense


# In[21]:


model = Sequential()
model.add(Dense(8,input_dim=4, activation='relu'))
model.add(Dense(8,input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax')) # [0.2,0.3,0.5]
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[22]:


model.summary()


# In[24]:


model.fit(scaled_X_train,y_train, epochs=150, verbose=2)


# In[36]:


predictions = model.predict(scaled_X_test).argmax(axis=1)


# In[33]:


y_test.argmax(axis=1)


# In[37]:


from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


# In[38]:


confusion_matrix(y_test.argmax(axis=1),predictions)


# In[39]:


print(classification_report(y_test.argmax(axis=1),predictions))


# In[40]:


accuracy_score(y_test.argmax(axis=1),predictions)


# In[41]:


model.save('kerasmodel.h5')


# In[42]:


from keras.models import load_model


# In[43]:


new_model = load_model('kerasmodel.h5')


# In[45]:


new_model.predict(scaled_X_test).argmax(axis=1)


# In[ ]:




