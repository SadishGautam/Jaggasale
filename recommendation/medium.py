#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
import pickle


# In[2]:


property_data = pd.read_csv('realestate.csv')


# In[3]:


property_data.head()


# In[4]:


property_data.drop(property_data.columns[[5,6,7,8,9,12,13,14,15,16,18]], axis=1, inplace=True)


# In[5]:


property_data.head()


# In[6]:


property_data.count()


# In[7]:


property_data['combine']= property_data['Title']+property_data['Address']
property_data.head()


# In[8]:


tfidf_vectorizer_params = TfidfVectorizer(analyzer='word')


# In[9]:


tfidf_vectorizer = tfidf_vectorizer_params.fit_transform(property_data['combine'])


# In[10]:


cosine_similarity_combine = linear_kernel(tfidf_vectorizer,tfidf_vectorizer)


# In[11]:


indices_property = pd.Series(property_data['Property_ID'])
inddict = indices_property.to_dict()
inddict = dict((v,k) for k,v in inddict.items())


# In[12]:


def recommend_Property(Property_ID):
    Property_ID=int(Property_ID)

    id = inddict[Property_ID]

    similarity_scores = list(enumerate(cosine_similarity_combine[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:6]


    property_index = [i[0] for i in similarity_scores]
    print(similarity_scores)

    return property_data.iloc[property_index].to_dict('records')


# In[13]:


recommend_Property(5)


# In[14]:


recommend_Property(25)


# In[ ]:
