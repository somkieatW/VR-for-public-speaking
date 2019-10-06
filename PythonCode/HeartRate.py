#!/usr/bin/env python
# coding: utf-8

# In[54]:


import fitbit
from fitbit import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime
import time
CLIENT_ID = '22B63K'
CLIENT_SECRET = '40c8ec5af315783465ef0b72e071d538'


# In[7]:


server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


# In[153]:


yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y-%m-%d"))
y = datetime.datetime.now()
timeEnd = y.strftime("%H"":""%M")
timeStart = y - datetime.timedelta(seconds=duration+600)
timeStart = timeStart.strftime("%H"":""%M")


# In[154]:


fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=today, detail_level='1sec' , start_time=timeStart, end_time = timeEnd )
time_list = []
val_list = []
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_list.append(i['value'])
    time_list.append(i['time'])
heartdf = pd.DataFrame({'Heart Rate':val_list,'Time':time_list})
heartdf


# In[142]:


#start button:
t0 = time.time()
#Codeasdaasdsdasdsadadsasdasd
time.sleep(3.0)
#stop button
t1 = time.time()
duration = t1 - t0 


# In[150]:


duration+50


# In[ ]:




