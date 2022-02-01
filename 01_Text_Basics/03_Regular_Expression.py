#!/usr/bin/env python
# coding: utf-8

# In[34]:


text = "The phone number of the agent is 408-555-1234. Call soon!"


# In[4]:


"408-555-1234" in text


# In[5]:


import re


# In[6]:


pattern = "phone"


# In[7]:


re.search(pattern,text)


# In[8]:


my_match = re.search(pattern,text)


# In[11]:


my_match.span()

# begin text[4] end text[9]


# In[14]:


my_match.start()


# In[15]:


my_match.end()


# In[25]:


text = "my phone is a new phone"


# In[26]:


match = re.search(pattern,text)


# In[27]:


match.span()

# just first match


# In[28]:


all_matches = re.findall("phone", text)


# In[29]:


all_matches


# In[30]:


len(all_matches)


# In[31]:


for match in re.finditer("phone",text):
    print(match.span())


# ## Identifiers

# <table ><tr><th>Character</th><th>Description</th><th>Example Pattern Code</th><th >Exammple Match</th></tr>
# 
# <tr ><td><span >\d</span></td><td>A digit</td><td>file_\d\d</td><td>file_25</td></tr>
# 
# <tr ><td><span >\w</span></td><td>Alphanumeric</td><td>\w-\w\w\w</td><td>A-b_1</td></tr>
# 
# 
# 
# <tr ><td><span >\s</span></td><td>White space</td><td>a\sb\sc</td><td>a b c</td></tr>
# 
# 
# 
# <tr ><td><span >\D</span></td><td>A non digit</td><td>\D\D\D</td><td>ABC</td></tr>
# 
# <tr ><td><span >\W</span></td><td>Non-alphanumeric</td><td>\W\W\W\W\W</td><td>*-+=)</td></tr>
# 
# <tr ><td><span >\S</span></td><td>Non-whitespace</td><td>\S\S\S\S</td><td>Yoyo</td></tr></table>

# ## Quantifiers

# <table ><tr><th>Character</th><th>Description</th><th>Example Pattern Code</th><th >Exammple Match</th></tr>
# 
# <tr ><td><span >+</span></td><td>Occurs one or more times</td><td>	Version \w-\w+</td><td>Version A-b1_1</td></tr>
# 
# <tr ><td><span >{3}</span></td><td>Occurs exactly 3 times</td><td>\D{3}</td><td>abc</td></tr>
# 
# 
# 
# <tr ><td><span >{2,4}</span></td><td>Occurs 2 to 4 times</td><td>\d{2,4}</td><td>123</td></tr>
# 
# 
# 
# <tr ><td><span >{3,}</span></td><td>Occurs 3 or more</td><td>\w{3,}</td><td>anycharacters</td></tr>
# 
# <tr ><td><span >\*</span></td><td>Occurs zero or more times</td><td>A\*B\*C*</td><td>AAACC</td></tr>
# 
# <tr ><td><span >?</span></td><td>Once or none</td><td>plurals?</td><td>plural</td></tr></table>

# In[50]:


text


# In[36]:


pattern = r'\d\d\d-\d\d\d-\d\d\d\d'


# In[37]:


phone_number = re.search(pattern,text)


# In[38]:


phone_number


# In[39]:


phone_number.group()


# In[40]:


pattern = r'\d{3}-\d{3}-\d{4}'


# In[41]:


phone_number = re.search(pattern,text)


# In[42]:


phone_number


# In[43]:


phone_number.group()


# In[51]:


pattern = r'(\d{3})-(\d{3})-(\d{4})'


# In[52]:


phone_number = re.search(pattern,text)


# In[57]:


phone_number.group(1)


# In[59]:


re.search(r"man|woman", "This woman was here")


# In[62]:


re.findall(r"..at", "The cat in the hat sat splat")


# In[63]:


re.findall(r"\d$", 'This ends with a number 2')


# In[66]:


re.findall(r"^\d", '1 is the first positive number')


# In[67]:


phrase = "there are 3 numbers 34 inside 5 this sentence"


# In[68]:


re.findall(r"[^\d]",phrase)


# In[69]:


re.findall(r"[^\d]+",phrase)


# In[70]:


test_phrase = "This is a string! but it has puncutation. How to remove it?"


# In[78]:


mylist = re.findall(r"[^!.? ]+",test_phrase)


# In[79]:


mylist


# In[81]:


' '.join(mylist)


# In[82]:


text = "Only find the hyphen-words. Were are the long-ish dash words?"


# In[83]:


re.findall(r"[\w]+-[\w]+",text)


# In[ ]:




