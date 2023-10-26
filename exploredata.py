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
# MAKE STRINGS UPPERCASE SO SEARCHING IS EASIER IN THE FUTURE
gas_types['City'] = gas_types['City'].str.upper()
gas_types['County'] = gas_types['County'].str.upper()
gas_types['Gas Code'] = gas_types['Gas Code'].str.upper()
gas_types['Gas Name'] = gas_types['Gas Name'].str.upper()
gas_types['Facility Name'] = gas_types['Facility Name'].str.upper()

# DROPPED COLUMNS WITH NO DATA
gas_types = gas_types.dropna(subset =['Address Line 1'] )

# DROPPED COLUMNS WITH MANY MISSING VALUES OR DATA THAT IS NOT IDENTIFYING
gas_types = gas_types.drop(columns = ['State', 'Address Line 2', 'FIPS'])

gas_types.head()


# The gas_type dataframe contains data about the location of emitter facilities and gas types emitted from each one. There are ~220,000 entries.

# In[4]:


air_quality = pd.read_csv('us_air_quality_measures.csv')
air_quality.tail()


# In[27]:


import matplotlib.pyplot as plt


# In[36]:


display(air_quality["MeasureName"].unique())

annual_avg = air_quality[air_quality["MeasureName"] == "Annual average ambient concentrations of PM2.5 in micrograms per cubic meter (based on seasonal averages and daily measurement)"]

plt.figure(figsize=(12, 8))

for state, group in grouped_averages.groupby("StateName"):
    plt.plot(group["ReportYear"], group["Value"], label=state, marker="o")

plt.title('Mean Value of PM2.5 Over Years by State')
plt.ylabel('Mean Value of PM2.5')
plt.xlabel('Year')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', ncol=2) # Placing legend outside the plot for better visibility
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[37]:


display(air_quality["MeasureName"].unique())

annual_avg = air_quality[air_quality["MeasureName"] == "Annual average ambient concentrations of PM 2.5 in micrograms per cubic meter, based on seasonal averages and daily measurement (monitor and modeled data)"]

plt.figure(figsize=(12, 8))

for state, group in grouped_averages.groupby("StateName"):
    plt.plot(group["ReportYear"], group["Value"], label=state, marker="o")

plt.title('Mean Value of PM2.5 Over Years by State')
plt.ylabel('Mean Value of PM2.5')
plt.xlabel('Year')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', ncol=2) # Placing legend outside the plot for better visibility
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# The air_quality dataframe contains air quality measures across different states/counties in the United States. It contains over 218,000 entries.

# In[6]:


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

#add2_nan =facilities['Address Line 2'].isna().sum()
#add2_nan


# The facilities dataframe contains data about each facility, namely address, location, and IDs (FIPS, NAICS). There are ~77,000 rows.
