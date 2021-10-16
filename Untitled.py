#!/usr/bin/env python
# coding: utf-8

# In[2]:


import glob
import pandas as pd
#df_final = pd.DataFrame(index=index, columns=columns)
#df_final = df_final.fillna(0)

csv_files = glob.glob("./*.csv")
#print(csv_files)
for i in range(len(csv_files)):
    csv_df = pd.read_csv(csv_files[i])
    if i == 0:
        final_copy = csv_df
        #print(final_copy)
        continue
    final_copy = pd.concat([final_copy, csv_df], axis=1)

print(final_copy)
    


# In[3]:


final_copy.columns


# In[4]:


final_copy.drop(columns=['Unnamed: 0'],inplace=True)


# In[5]:


final_copy = final_copy.loc[:,~final_copy.columns.duplicated()]

#print(final_copy)


# In[6]:


final_copy


# In[7]:


final_copy=final_copy[['Area id','12/10/2021 23:42:07','14/10/2021 23:07:41','15/10/2021 09:52:07','15/10/2021 14:41:20','15/10/2021 19:46:39','15/10/2021 23:12:45','16/10/2021 10:32:05']]


# In[8]:


final_copy


# In[9]:



# Convention for import of the pyplot interface
import matplotlib.pyplot as plt

# Set-up to have matplotlib use its support for notebook inline plots
get_ipython().run_line_magic('matplotlib', 'inline')
 
plt.rc('font', size=12)
fig, ax = plt.subplots(figsize=(20, 6))

scrap_time = ["12/10/2021 23:42:07","14/10/2021 23:07:41","15/10/2021 09:52:07","15/10/2021 14:41:20","15/10/2021 19:46:39","15/10/2021 23:12:45","16/10/2021 10:32:05"]
y_ax = [final_copy["12/10/2021 23:42:07"][0],final_copy["14/10/2021 23:07:41"][0],final_copy["15/10/2021 09:52:07"][0],final_copy["15/10/2021 14:41:20"][0],final_copy["15/10/2021 19:46:39"][0],final_copy["15/10/2021 23:12:45"][0],final_copy["16/10/2021 10:32:05"][0]]
# Specify how our lines should look
ax.plot(scrap_time,y_ax, color='tab:orange', label='Ships')

# Same as above
ax.set_xlabel('Scrap Time')
ax.set_ylabel('Ships detected')
ax.set_title('Area ID: {}'.format(final_copy["Area id"][0]))
ax.grid(True)
ax.legend(loc='upper left');


# In[10]:


import numpy as np
# Set-up to have matplotlib use its support for notebook inline plots
get_ipython().run_line_magic('matplotlib', 'inline')
 


for i in range(0,100):
    plt.rc('font', size=12)
    fig, ax = plt.subplots(figsize=(20, 6))
    scrap_time = ["12/10/2021 23:42:07","14/10/2021 23:07:41","15/10/2021 09:52:07","15/10/2021 14:41:20","15/10/2021 19:46:39","15/10/2021 23:12:45","16/10/2021 10:32:05"]
    y_ax = [final_copy["12/10/2021 23:42:07"][i],final_copy["14/10/2021 23:07:41"][i],final_copy["15/10/2021 09:52:07"][i],final_copy["15/10/2021 14:41:20"][i],final_copy["15/10/2021 19:46:39"][i],final_copy["15/10/2021 23:12:45"][i],final_copy["16/10/2021 10:32:05"][i]]
    # Specify how our lines should look
    ax.plot(scrap_time,y_ax, color='tab:orange', label='Ship Count')

    # Same as above
    ax.set_xlabel('Scrap Time')
    ax.set_ylabel('Ships detected')
    ax.set_title('Area ID: {}'.format(final_copy["Area id"][i]))
    ax.grid(True)
    ax.legend(loc='upper left');


# In[ ]:




