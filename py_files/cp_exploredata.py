#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import csv


# Let's view the first few columns of each dataframe to see what we are working with

# In[3]:


gas_types = pd.read_csv('us_greenhouse_gas_emission_direct_emitter_gas_type.csv')
# RENAME ALL COLUMNS SO IT'S NOT SUCH AN EYESORE
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.ADDRESS1': 'Address Line 1'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.ADDRESS2': 'Address Line 2'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.CITY': 'City'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.CO2E_EMISSION': 'CO2 Emission'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.COUNTY': 'County'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.FACILITY_ID': 'Facility ID'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.GAS_CODE': 'Gas Code'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.GAS_NAME': 'Gas Name'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.LATITUDE': 'Latitude'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.LONGITUDE': 'Longitude'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.STATE': 'State'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.STATE_NAME': 'State Name'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.YEAR': 'Year'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.ZIP': 'Zip Code'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.FACILITY_NAME': 'Facility Name'})
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.COUNTY_FIPS': 'FIPS'})
# MAKE ADDRESSES ALL UPPERCASE, THEN DROP ROWS WITH NO ADDRESS
gas_types['Address Line 1'] = gas_types['Address Line 1'].str.upper()
gas_types = gas_types.dropna(subset =['Address Line 1'] )

gas_types.head()


# The gas_type dataframe contains data about the location of emitter facilities and gas types emitted from each one. There are ~220,000 entries.

# In[4]:


facilities = pd.read_csv('us_greenhouse_gas_emissions_direct_emitter_facilities.csv')
# RENAME ALL COLUMNS SO IT'S NOT SUCH AN EYESORE
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.ADDRESS1': 'Address Line 1'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.ADDRESS2': 'Address Line 2'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.CEMS_USED': 'CEMS Used'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.CITY': 'City'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.COUNTY': 'County'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.COUNTY_FIPS': 'FIPS'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.FACILITY_ID': 'Facilities ID'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.LATITUDE': 'Latitude'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.LONGITUDE': 'Longitude'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.PRIMARY_NAICS_CODE': 'NAICS Code'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.STATE': 'State'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.STATE_NAME': 'State Name'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.YEAR': 'Year'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.ZIP': 'Zip Code'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.FACILITY_NAME': 'Facility Name'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.SECONDARY_NAICS_CODE': 'Secondary NAICS Code'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.ADDITIONAL_NAICS_CODES': 'Additional NAICS Codes'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.COGENERATION_UNIT_EMISS_IND': 'Cogeneration Unit Emission Index(?)'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.EPA_VERIFIED': 'EPA Verified'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.PARENT_COMPANY': 'Parent Company'})
facilities = facilities.rename(columns = {'V_GHG_EMITTER_FACILITIES.PLANT_CODE_INDICATOR': 'Plant Code Indicator'})
# MAKE ADDRESSES ALL UPPERCASE, THEN DROP ROWS WITH NO ADDRESS
facilities['Address Line 1'] = facilities['Address Line 1'].str.upper()
facilities = facilities.dropna(subset =['Address Line 1'] )

facilities.head()


# The facilities dataframe contains data about each facility, namely address, location, and IDs (FIPS, NAICS). There are ~77,000 rows.

# In[5]:


len(facilities)


# In[6]:


facilities.nunique()


# Total length of gas_types, when compared to number of facilites with no adress2 we see the whole column is empty - drop

# In[7]:


len(gas_types)


# Number of NA vlaues in each column gas_types

# In[14]:


gas_types.head(5)


# In[18]:


avg_co2=gas_types.groupby("State")["CO2 Emission"].mean().reset_index()
avg_co2.head()


# In[21]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[23]:


plt.figure(figsize=(15, 7))
sns.barplot(data=avg_co2, x="State", y="CO2 Emission")
plt.xticks(rotation=45, fontsize=10)


# In[ ]:


gas_types.isna().sum()


# The number of umique values in eahc, could be useful to kno what to group by such as state, gas code and name 

# In[ ]:


gas_types.nunique()


# In[ ]:


air_quality = pd.read_csv('us_air_quality_measures.csv')
air_quality.tail()


# The air_quality dataframe contains air quality measures across different states/counties in the United States. It contains over 218,000 entries.

# In[ ]:


# Ran out of steam. Next step is to change all addresses to uppercase or lowercase so we can merge

merged_gas_types_and_facilities = gas_types.merge(facilities, on = 'Address Line 1')
merged_gas_types_and_facilities.head(5)


# In[ ]:


merged_gas_types_and_facilities.value_counts("County_x")


# In[ ]:


facilities.head(5)


# In[ ]:


facilities.value_counts("County")


# In[ ]:


harris=facilities[facilities["County"]== "HARRIS COUNTY"]


# In[ ]:


harris.nunique()


# we have 328 unique facilty ids but only 204 unique facility addresses 

# In[ ]:


harris.groupby("Address Line 1").describe


# In[ ]:


val=harris.groupby("Address Line 1").count
val


# In[ ]:


harris.pivot_table(index='Address Line 1', columns='Facilities ID', aggfunc='size', fill_value=0).head(5)


# In[ ]:


count = harris.groupby('Facilities ID')['Address Line 1'].count().to_frame()
multiples= count[count >1].index
# multiples.
count


# In[ ]:


multiplies_val = harris[harris['Facilities ID'].isin(multiples)]
multiplies_val.head()


# In[ ]:


# Step 1: Group by 'Facilities ID' and get counts.
count = harris.groupby('Facilities ID')['Address Line 1'].count()

# Step 2: Sort these counts in descending order.
sorted_count = count.sort_values(ascending=False).to_frame()

# Step 3: For each 'Facilities ID', get the actual addresses.
def list_addresses(group):
    return ', '.join(group['Address Line 1'].unique())

addresses = harris.groupby('Facilities ID').apply(list_addresses).to_frame(name='Unique Addresses')

# Merge counts and addresses into a single DataFrame.
result = sorted_count.join(addresses)
result


# Moving on, i needed help doing that
# 

# In[ ]:


facilities['Latitude'].value_counts()


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


facilities.head()


# In[ ]:


graph=facilities[['Latitude','Longitude']].dropna()
sns.jointplot(data=graph, x='Longitude', y='Latitude', kind="hex")


# In[ ]:


world = gpd.read_file('ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
world.head()


# In[ ]:


import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
world = gpd.read_file('ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')

# Filter for the United States
us = world[world['ADMIN'] == "United States of America"]

# Create a base matplotlib axis
fig, ax = plt.subplots(figsize=(20, 20))
ax.set_xlim([-200, 0])
ax.set_aspect('equal')

# Plot the United States on that axis
us.plot(ax=ax, color="white", edgecolor="black")

# Overlay the KDE plot on the same axis
sns.kdeplot(data=graph, x='Longitude', y='Latitude', fill=True, ax=ax)

plt.show()


# In[ ]:


sns.kdeplot(data=graph, x='Longitude', y='Latitude', fill=True, ax=ax)


# In[ ]:


facilities.value_counts("State").head(5)

