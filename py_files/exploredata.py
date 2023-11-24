#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Let's view the first few columns of each dataframe to see what we are working with

# In[2]:


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
# MAKE STRINGS UPPERCASE SO SEARCHING IS EASIER IN THE FUTURE
gas_types['City'] = gas_types['City'].str.upper()
gas_types['County'] = gas_types['County'].str.upper()
gas_types['Gas Code'] = gas_types['Gas Code'].str.upper()
gas_types['Gas Name'] = gas_types['Gas Name'].str.upper()
gas_types['Facility Name'] = gas_types['Facility Name'].str.upper()
# REMOVE 'COUNTY' FROM ENTRIES IN THE 'COUNTY' COLUMN TO MATCH COUNTY NAMES IN THE AIR QUALITY DATAFRAME
gas_types['County'] = gas_types['County'].str.split(' ').str[0]
# DROPPED COLUMNS WITH NO DATA
gas_types = gas_types.dropna(subset =['Address Line 1'] )
# DROPPED COLUMNS WITH MANY MISSING VALUES OR DATA THAT IS NOT IDENTIFYING
gas_types = gas_types.drop(columns = ['State', 'Address Line 2', 'FIPS'])

gas_types.head()


# The gas_type dataframe contains data about the location of emitter facilities and gas types emitted from each one. There are ~220,000 entries.

# In[3]:


air_quality = pd.read_csv('us_air_quality_measures.csv')
# MAKE STATE AND COUNTY NAMES UPPERCASE
air_quality['StateName'] = air_quality['StateName'].str.upper()
air_quality['CountyName'] = air_quality['CountyName'].str.upper()
air_quality.head()


# The air_quality dataframe contains air quality measures across different states/counties in the United States. It contains over 218,000 entries.

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
#facilities.head()


# The facilities dataframe contains data about each facility, namely address, location, and IDs (FIPS, NAICS). There are ~77,000 rows.

# # Question a 
# ## How does air quality relate to the number of emitting facilities and and level of emissions in the area?
# We can answer this question using the air_quality and gas_types dataframes. There are a few things we need to choose first:
# - what year we will use
# - which air quality measure type to use

# In[6]:


# air quality rows where 'MeasureType' is average
# we are doing this because other measure types contain a lot of 0s
aq_avg = air_quality[air_quality['MeasureType'] == 'Average']


# The air quality dataframe has data from the years 1999 - 2013 while gas_types has data from 2010 - 2019. Let's use the year 2011 since both have a good amount of data for this year.

# In[6]:


# UNCOMMENT CODE BELOW TO SEE NUM ENTRIES FOR EACH YEAR
#gas_types['Year'].value_counts()
#aq_avg['ReportYear'].value_counts()


# Now let's find the number of facilities in a county in a given year and put that data together. Below is a trial run. Following a successful trial run, I put the following code into a for loop to do the same for every state and county in 2011.

# In[7]:


# air_quality rows where Weston is the county and year is 2011
weston_aq_2011 = aq_avg[(aq_avg['CountyName'] == 'WESTON') & (aq_avg['ReportYear'] == 2011) & (aq_avg['StateName'] == 'WYOMING')]

# gas_types rows where Weston is county and year is 2011
weston_gas_2011 = gas_types[(gas_types['County'] == 'WESTON') & (gas_types['Year'] == 2011)]
# get number of facilities in that county and year
num_weston_facilities = weston_gas_2011['Facility Name'].nunique()

# add number of facilities column to weston_aq
#weston_aq['NumFacilities'] = num_weston_facilities
weston_aq_and_facilities = weston_aq_2011.assign(NumFacilities= num_weston_facilities)
weston_aq_and_facilities


# ## ATTENTION
# Do not run the cell below. It takes ~3.5 hours to produce the resulting dataframe. The code remains here for the sake of documentation and its output can be found in the file 'county-airq-num-facilities-with-none.csv'

# In[13]:



# create an empty DataFrame to store the results: air quality
county_aq_with_facilities = pd.DataFrame()

# get unique counties and states from the aq_avg
counties = aq_avg['CountyName'].unique()
states = aq_avg['StateName'].unique()

# iterate through each combination of county and state
for county in counties:
    for state in states:
        # filter 'aq_avg' for current county and state in 2011
        county_aq_2011 = aq_avg[(aq_avg['CountyName'] == county) & (aq_avg['StateName'] == state) & (aq_avg['ReportYear'] == 2011)]

        # filter 'gas_types' for the current county and state in 2011
        county_gas_2011 = gas_types[(aq_avg['CountyName'] == county) & (gas_types['State Name'] == state) & (gas_types['Year'] == 2011)]
        # get the number of unique facilities for the current county and state in 2011
        num_facilities = county_gas_2011['Facility Name'].nunique()

        # add number of facilities column to county_aq_data
        county_aq_and_facilities_entry = county_aq_2011.assign(NumFacilities= num_facilities)

        # create a new row for the resulting dataframe with the county, state, and number of facilities
        county_aq_with_facilities = pd.concat([county_aq_with_facilities, county_aq_and_facilities_entry], ignore_index=True)
# Display the result DataFrame
county_aq_with_facilities.head()


# In[7]:


# save dataframe to a CSV file. Obviously this cell won't work sinde you didnt run the above cell.
# county_aq_with_facilities.to_csv('county-airq-num-facilities-with-none.csv', index=False)


# There are some state/county combos for which we have air quality data but no facility data. NumFacilities is 0 for these states/counties.

# In[16]:


county_aq_with_facilities_with_none = pd.read_csv('county-airq-num-facilities-with-none.csv')
county_aq_with_facilities_with_none.head()

print(f'The number of non-zero values in the NumFacilities column is {len(county_aq_with_facilities_with_none) - county_aq_with_facilities_with_none["NumFacilities"].eq(0).sum()}.')


# Of the 3634 rows in county_aq_with_facilities, only 424 of them have non-zero values for NumFacilities. Maybe can use our generative model to predict the number of facilities in some of these places based on air quality value. For now, let's remove these values so we can plot air quality vs num facilities and air quality vs emission value

# In[18]:


# county_aq_with_facilities = county_aq_with_facilities_with_none[county_aq_with_facilities_with_none['NumFacilities'] != 0]
# county_aq_with_facilities.head()

# save to CSV as well. This also won't work anymore, but is here to document what was done
#county_aq_with_facilities.to_csv('county-airq-num-facilities.csv', index=False)


# The next time this notebook was loaded, county_aq_with_facilities was read from the CSV it was saved to last time

# In[19]:


# read from csv to continue working
county_aq_with_facilities = pd.read_csv('county-airq-num-facilities.csv')

county_aq_with_facilities.head()


# Finally, let's make a scatter plot to visualize the relationship between number of facilities and air quality measure values.

# In[20]:


sns.scatterplot(x = "NumFacilities", y = "Value", data=county_aq_with_facilities)


# In[22]:


county_aq_with_facilities['StateName'].value_counts()


# # Question c
# ## Is there a gas type associated with especially bad AQ measures?
# We can answer this question using the air_quality and gas_types dataframes. We will use:
# - aq measures from a particular gas type

# In[24]:


# air quality rows where 'MeasureType' is average
# we are doing this because other measure types contain a lot of 0s
aq_avg = air_quality[air_quality['MeasureType'] == 'Average']
# rename the county column in aq_avg so they have the same name and merging is easier
aq_avg = aq_avg.rename(columns = {'CountyName': 'County'})


# The air quality dataframe has data from the years 1999 - 2013 while gas_types has data from 2010 - 2019. Let's use the year 2011 since both have a good amount of data for this year.

# In[25]:


# UNCOMMENT CODE BELOW TO SEE NUM ENTRIES FOR EACH YEAR
#gas_types['Year'].value_counts()
#aq_avg['ReportYear'].value_counts()


# Let's merge both dataframes based on County so we get a dataframe with both gas codes and aq values (fingers crossed)

# In[26]:


gas_types_aq_avg_merged = pd.merge(gas_types, aq_avg, on='County')
gas_types_aq_avg_merged.tail()


# Nice! Now let's plot Values VS Gas Codes on a scatterplot to visualize any correlation between the two.

# In[28]:


sns.scatterplot(x = "Gas Code", y = "Value", data=gas_types_aq_avg_merged)


# Visually, the scatterplot does not show much correlation between a specific gas type and air quality values. Another way to do this would be to groupby gas type and get the average air quality value.

# In[29]:


avg_value_by_gas_code = gas_types_aq_avg_merged.groupby('Gas Code')['Value'].mean()
# now we make bar graph
avg_value_by_gas_code.plot.bar(use_index=True)

plt.title('Bar Graph of Gas Code vs. Value')
plt.xlabel('Gas Code')
plt.ylabel('Value')
plt.show()


# Average values are all around the same thing. There doesn't seem to be a correlation between an air quality value and a gas type. Tbh this question seems kinda weak (or seems like it'll be too hard to extract the data in a way that will correctly answer the question)

# Now plot CO2 emission VS aq measure

# In[32]:


plt.figure(figsize=(10, 6))
gas_types_aq_avg_2011 = gas_types_aq_avg_merged[gas_types_aq_avg_merged['ReportYear'] == 2011]

sns.scatterplot(x = "CO2 Emission", y = "Value", data=gas_types_aq_avg_2011, s=10)

plt.xlabel("CO2 Emission")
plt.ylabel("Air Quality Measurement")
# plt.title("Scatterplot of CO2 Emission vs. AQ Value")
plt.show()


# In[ ]:




