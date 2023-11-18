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
gas_types = gas_types.rename(columns = {'V_GHG_EMITTER_GAS.CO2E_EMISSION': 'CO2 Emission (equivalent)'})
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

gas_types #.head()


# The gas_type dataframe contains data about the location of emitter facilities and gas types emitted from each one. There are ~220,000 entries.

# In[4]:


new_york_df = gas_types[gas_types["State Name"] == "NEW YORK"]


for value in gas_types["Gas Code"].unique():
    print(value)
for value in gas_types["Gas Name"].unique():
    print(value)


# In[5]:


air_quality = pd.read_csv('us_air_quality_measures.csv')
# MAKE STATE AND COUNTY NAMES UPPERCASE
air_quality['StateName'] = air_quality['StateName'].str.upper()
air_quality['CountyName'] = air_quality['CountyName'].str.upper()
# DROP COLUMNS WHERE THE 'Value' COLUMN IS 0.000000
#air_quality = air_quality[air_quality['Value'] != 0.000000]
air_quality.head()


# In[6]:


for value in air_quality["MeasureName"].unique():
    print(value)


for value in air_quality["Unit"].unique():
    print(value)


# In[54]:


average_air_quality = air_quality[air_quality["MeasureName"] == "Annual average ambient concentrations of PM2.5 in micrograms per cubic meter (based on seasonal averages and daily measurement)"]
average_air_quality_micrograms_per_meters_cubed = average_air_quality[average_air_quality["Unit"] == "µg/m³"]
stripped_average_air_quality = average_air_quality_micrograms_per_meters_cubed[["CountyName","Value","ReportYear"]].sort_values(by="CountyName")
grouped_average_air_qualty = stripped_average_air_quality.groupby(["CountyName", "ReportYear"])["Value"].mean().reset_index()
print(len(grouped_average_air_qualty))
print(grouped_average_air_qualty.head())

# average_air_quality_by_county = average_air_quality_micrograms_per_meters_cubed.groupby("CountyName")
# average_air_quality_by_county.head()


# The air_quality dataframe contains air quality measures across different states/counties in the United States. It contains over 218,000 entries.

# In[8]:


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

#add2_nan =facilities['Address Line 2'].isna().sum()
#add2_nan


# The facilities dataframe contains data about each facility, namely address, location, and IDs (FIPS, NAICS). There are ~77,000 rows.

# # Question 1
# ## How does air quality relate to the number of emitting facilities and and level of emissions in the area?
# We can answer this question using the air_quality and gas_types dataframes. We can group facilities by county. Just for a trial run, let's pick a county that's in both dataframes

# In[9]:


# air_quality rows where Weston is the county
weston_aq = air_quality[(air_quality['CountyName'] == 'WASHINGTON')  & (air_quality['ReportYear'] == 2011)]
weston_aq.head()


# In[10]:


# gas_types rows where Weston is county
weston_gas_2013 = gas_types[(gas_types['County'] == 'WESTON') & (gas_types['Year'] == 2011)]
weston_gas_2013


# In[11]:


air_quality['CountyName'].value_counts()


# In[12]:


gas_types['Year'].value_counts()

