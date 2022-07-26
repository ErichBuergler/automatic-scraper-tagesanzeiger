#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get("https://www.tagesanzeiger.ch/")
doc = BeautifulSoup(response.text)


# ### how to do it with find
# response = requests.get('https://www.tagesanzeiger.ch/')
# doc = BeautifulSoup(response.text)
# website = "https://www.tagesanzeiger.ch/"
# link = website + doc.find(class_ = "article-teaser-list").find('a')['href']
# link

# In[3]:


#doc.select('.ArticleTeaser_title__tlltn') here i would get all the titles


# In[9]:


doc.find_all('h3')[0]


# In[11]:


doc.find_all('h3', class_="ArticleTeaser_title__tlltn")


# In[15]:


doc.select('.ArticleTeaser_title__tlltn')[0] #this gives me the top article of the webpage


# In[16]:


for headline in doc.select('.ArticleTeaser_title__tlltn')[0]:
    print(headline.text) #that gives me the headline of the front article


# In[17]:


doc.find(class_ = "article-teaser-list").find('a')['href'] #thats how i find  the link


# In[19]:


website = "https://www.tagesanzeiger.ch/"
link = website + doc.find(class_ = "article-teaser-list").find('a')['href']
link


# In[27]:


for headline in doc.select('.ArticleTeaser_title__tlltn')[0]:
    print(headline.text) #that gives me the headline of the front article
    print(link)


# ### now we make a dataframe out of it

# In[31]:


stories = []
for headline in doc.select('.ArticleTeaser_title__tlltn')[0]:
    frontstory = (headline.text) #that gives me the headline of the front article
    url = (link)
    
    story = {
        'frontstory': frontstory,
        'url': url
        
    }
    stories.append(story)
    
df = pd.DataFrame(stories)
df


# In[32]:


#now we create a csv file out of it:
df.to_csv("tagesanzeiger.csv", index=False)


# In[ ]:




