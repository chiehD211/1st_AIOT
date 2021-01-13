#!/usr/bin/env python
# coding: utf-8

# In[7]:


#作業1 : 練習使用一個民生物聯網 API，例如空氣、地震等感測站所回傳的紀錄資料。
#           參考資料網址： https://ci.taiwan.gov.tw/dsp/environmental.aspx


# In[8]:


# 科技部 智慧園區空品測站
import requests
import json
import pprint
url = "https://sta.ci.taiwan.gov.tw/STA_AirQuality_MOST/v1.0/Things?$expand=Locations&$select=name,properties&$count=true"
r = requests.get(url)
result = r.json()
pprint.pprint(result)


# In[9]:


#作業2 : 練習操作 OGC SensorThings API，將環保局測站位置的資料抓取下來，並且觀察下載資料的內容。
#           參考網址：https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things


# In[10]:


URL2 = "https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things"
response2 = requests.get(URL2)
data = response2.json()
pprint.pprint(data)


# In[11]:


#作業3 : 依據作業 2 所下載的各個環保局測站感測器的描述資料，進一步點選 Datastreams、Locations，以及 Datastreams 點選進入後，
#點選 Observations 的 URL，觀察所下載到的資料內容，其中 Observations 內部是否包含個別感測器紀錄的資料。


# In[12]:


# Get the detail of each value
value = data["value"]
print("\nThere are {} data in this page".format(len(value)))

len_data= len(value)
for i in range(len_data):
    print("=============data {}=============".format(value[i]["@iot.id"]))
    print("Description:", value[i]["description"])
     # You can print set up your own data


# In[ ]:




