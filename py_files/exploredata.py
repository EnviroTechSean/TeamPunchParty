#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import csv


# Let's view the first few columns of each dataframe to see what we are working with

# In[19]:


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

# In[22]:


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


air_quality = pd.read_csv('us_air_quality_measures.csv')
air_quality.tail()


# The air_quality dataframe contains air quality measures across different states/counties in the United States. It contains over 218,000 entries.

# In[24]:


# Ran out of steam. Next step is to change all addresses to uppercase or lowercase so we can merge

merged_gas_types_and_facilities = gas_types.merge(facilities, on = 'Address Line 1')
merged_gas_types_and_facilities


# In[ ]:




