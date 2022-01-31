#!/usr/bin/env python
# coding: utf-8

# In[1]:


person = "Ahmet"


# In[3]:


print("my name is {}".format(person))


# In[4]:


print(f"my name is {person}")


# In[5]:


d = {'a':123,'b':456}


# In[7]:


print(f"my number is {d['a']}")


# In[8]:


mylist = [0,1,2]


# In[9]:


print(f"my number is {mylist[0]}")


# In[10]:


library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]


# In[11]:


library


# In[12]:


for book in library:
    print(book)


# In[13]:


for book in library:
    print(f"Author is {book[0]}")


# In[16]:


for author,topic,pages in library:
    print(f"{author} {topic} {pages}")


# In[17]:


library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting in water alone', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]


# In[21]:


for author,topic,pages in library:
    print(f"{author:{10}} {topic:{30}} {pages:>{10}}")


# In[22]:


for author,topic,pages in library:
    print(f"{author:{10}} {topic:{30}} {pages:.>{10}}")


# In[23]:


from datetime import datetime


# In[24]:


today = datetime(year=2022,month=2,day=26)


# In[25]:


print(f"{today}")


# In[26]:


today


# In[29]:


print(f"{today:%B %d, %Y}")


# # Text Files

# In[31]:


get_ipython().run_cell_magic('writefile', 'test.txt', 'Hello, this is a quick test file.\nThis is the second line of the file.')


# In[32]:


# This is specific for jupyter notebook


# In[1]:


myfile = open('test.txt')

# just for read


# In[2]:


myfile


# In[3]:


myfile.read()


# In[41]:


myfile.read()


# In[42]:


# You can't read multiple times


# In[44]:


myfile.seek(0)

# reset the cursor


# In[45]:


myfile.read()


# In[46]:


myfile.seek(0)


# In[47]:


content = myfile.read()


# In[49]:


content


# In[48]:


print(content)


# In[50]:


myfile.close()


# In[52]:


myfile = open('test.txt')


# In[53]:


myfile.readlines()


# In[54]:


myfile.seek(0)


# In[55]:


mylines = myfile.readlines()


# In[56]:


mylines


# In[57]:


for line in mylines:
    print(line[0])


# In[60]:


for line in mylines:
    print(line.split()[0])


# In[62]:


myfile = open('test.txt', 'w+')


# 'r'       open for reading (default)  
# 'w'       open for writing, truncating the file first  
# 'x'       create a new file and open it for writing  
# 'a'       open for writing, appending to the end of the file if it exists  
# 'b'       binary mode  
# 't'       text mode (default)  
# '+'       open a disk file for updating (reading and writing)  
# 'U'       universal newline mode (deprecated)

# In[63]:


myfile.read()


# In[64]:


myfile.write('my new text')


# In[69]:


myfile.seek(0)


# In[70]:


myfile.read()

# overwrite 


# In[71]:


myfile.close()


# In[73]:


myfile = open('wrong.txt','a+')


# In[74]:


myfile.write('really')


# In[75]:


myfile.close()


# In[76]:


newfile = open('wrong.txt')


# In[77]:


newfile.read()


# In[79]:


newfile.close()


# In[78]:


myfile = open('wrong.txt', mode='a+')


# In[80]:


myfile.write('This is an added line')


# In[81]:


myfile.seek(0)


# In[82]:


myfile.read()


# In[83]:


myfile.write('\nThis is a real new line')


# In[87]:


myfile.seek(0)


# In[85]:


myfile.read()


# In[88]:


print(myfile.read())


# In[89]:


myfile.close()


# In[92]:


with open('test.txt', 'r') as mynewfile:
    myvar = mynewfile.readlines()
    
# we don't need to close,


# In[93]:


myvar


# In[ ]:




