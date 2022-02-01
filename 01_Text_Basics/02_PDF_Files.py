#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install PyPDF2


# In[2]:


import PyPDF2


# In[4]:


myfile = open('US_Declaration.pdf', mode='rb')


# In[5]:


pdf_reader = PyPDF2.PdfFileReader(myfile)


# In[7]:


pdf_reader.numPages


# In[10]:


page_one = pdf_reader.getPage(0)


# In[13]:


print(page_one.extractText())


# In[14]:


mytext = page_one.extractText()


# In[15]:


myfile.close()


# In[16]:


# can't insert a python string into pdf. But we can add a page to pdf.  


# In[17]:


f = open('US_Declaration.pdf', 'rb')


# In[18]:


pdf_reader = PyPDF2.PdfFileReader(f)


# In[19]:


first_page = pdf_reader.getPage(0)


# In[20]:


pdf_writer = PyPDF2.PdfFileWriter()


# In[21]:


pdf_writer.addPage(first_page)


# In[22]:


pdf_output = open('my_brand_new.pdf', 'wb')


# In[23]:


pdf_writer.write(pdf_output)


# In[24]:


pdf_output.close()


# In[25]:


f.close()


# In[26]:


brand_new = open('my_brand_new.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(brand_new)


# In[27]:


pdf_reader.numPages


# In[29]:


f = open('US_Declaration.pdf','rb')

pdf_text = [0]

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    
    page = pdf_reader.getPage(p)
    
    pdf_text.append(page.extractText())
    
f.close()


# In[30]:


pdf_text


# In[31]:


len(pdf_text)


# In[32]:


for page in pdf_text:
    print(page)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')


# In[ ]:




