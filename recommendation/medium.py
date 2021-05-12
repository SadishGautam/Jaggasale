#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
import pickle
import json


# In[2]:

def read_database():
    try:
        property_data = pd.read_csv('realestate.csv')
        return property_data


    except Exception as e:
        print(e)
        return None


def adarsha():
    property_data = read_database()

    # property_data.head()
    if property_data is None:
        return None

    # property_data.drop(property_data.columns[[18]], axis=1, inplace=True)

    # property_data.head()

    property_data = property_data.fillna('')

    property_data['combine']= property_data['title']+property_data['address']

    property_data.head()

    tfidf_vectorizer_params = TfidfVectorizer(analyzer='word')

    tfidf_vectorizer = tfidf_vectorizer_params.fit_transform(property_data['combine'])

    cosine_similarity_combine = linear_kernel(tfidf_vectorizer,tfidf_vectorizer)

    indices_property = pd.Series(property_data['id'])

    inddict = indices_property.to_dict()

    inddict = dict((v,k) for k,v in inddict.items())
    return cosine_similarity_combine, property_data ,inddict




def get_Property(Property_ID):
    try:
        cosine_similarity_combine,property_data,inddict =adarsha()

    except Exception as e:
        print(e)

        return {}


    Property_ID=int(Property_ID) - 1
    list2 = ['Property_ID','Title', 'Price', 'email', 'discount_price', 'slug', 'category', 'label', 'sold_or_rent', 'picture_count', 'area', 'owner_name', 'phone_number', 'rooms', 'bathrooms', 'Floors', 'Description', 'location', 'date', 'have_parking', 'have_garden', 'have_drinage', 'have_balcony', 'have_hallRoom', 'have_diningRoom', 'have_elevator', 'have_water', 'have_electricityBackup', 'have_securityStaff', 'have_lift', 'have_kidsPlayground', 'have_electricityPole', 'have_road', 'have_waterSupply', 'image','user_id', 'area_face', 'built_date', 'Latitude', 'Longitude',
    'AP_have_electricity',	'Ap_have_dining_room',	'Ap_have_drinage',	'Ap_have_kids_playground',	'Ap_have_lift',	'Ap_have_parking',	'Ap_have_water_supply',	'La_have_drinage',	'La_have_electricity',	'La_have_road',	'La_have_water',	'Address']
    dic = {}
    for i,j in enumerate(property_data.iloc[Property_ID].values):
        dic[list2[i]] = str(j)
    return dic
    # return json.dumps(

    #     print(i)
    # breakpoint()

    # list2 = ['Property_ID','Title', 'Address', 'City', 'Price', 'Floors', 'Parking', 'Views', 'Posted']
    # data=list(property_data.iloc[Property_ID].values)
    # dic = {}
    # for i in range(0,len(list2)):
    #     dic[list2[i]] = data[i]
    # return dic


    # return inddict[Property_ID]


# In[3]:



def recommend_Property(Property_ID):
    Property_ID=int(Property_ID)
    try:
        cosine_similarity_combine,property_data,inddict =adarsha()

    except Exception:
        return None

    id = inddict[Property_ID]

    similarity_scores = list(enumerate(cosine_similarity_combine[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:6]


    property_index = [i[0] for i in similarity_scores]
    print(similarity_scores)

    return property_data.iloc[property_index].to_dict('records')


# In[13]:




# In[ ]:
