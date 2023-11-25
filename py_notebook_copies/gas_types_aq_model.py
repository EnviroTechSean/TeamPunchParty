#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import punch_party_utils


# In[2]:


average_air_quality = punch_party_utils.make_average_aq_df()
average_air_quality = average_air_quality[average_air_quality["MeasureName"] == "Annual average ambient concentrations of PM2.5 in micrograms per cubic meter (based on seasonal averages and daily measurement)"]


# In[3]:


# For the first model, just CO2 emmisions in a given year -> air quality in a given year
average_air_quality = average_air_quality.drop(
    columns=["MeasureId", "MeasureName", "MeasureType", "StratificationLevel",
             "StateFips", "StateName", "CountyFips", "CountyName", "Unit",
             "UnitName", "DataOrigin", "MonitorOnly"])

display(average_air_quality.columns)


# In[4]:


print(len(average_air_quality))

aq_by_year = average_air_quality.groupby("ReportYear")


# In[5]:


air_quality_yearly_averages = aq_by_year.agg("mean")
print(air_quality_yearly_averages)


# In[6]:


gas_types = punch_party_utils.make_gas_types_df()


# In[7]:


display(gas_types.columns)

gas_types = gas_types.drop(
    columns=["Address Line 1", "City", "County", 
             "Facility ID", "Gas Code", "Latitude", "Longitude", 
             "State Name", "Zip Code", "Facility Name"])


# In[8]:


display(gas_types.head())


# In[10]:


raw_emmisions_only = gas_types.drop(columns=["Gas Name"])
yearly_raw_emmisions = raw_emmisions_only.groupby("Year").agg("sum")


# In[11]:


print(yearly_raw_emmisions)


# In[12]:


co2_emmisions_with_aq = yearly_raw_emmisions.merge(
    air_quality_yearly_averages, left_index=True, right_index=True, how="inner")
print(co2_emmisions_with_aq)


# In[13]:


# Normalize
max_co2_emission = np.max(co2_emmisions_with_aq["CO2 Emission"])
max_co2_emission
co2_emmisions_with_aq["CO2 Emission"] = co2_emmisions_with_aq["CO2 Emission"] / max_co2_emission

display(co2_emmisions_with_aq)


# In[14]:


co2_aq_model = LinearRegression(fit_intercept=True)

independent_var = co2_emmisions_with_aq[["CO2 Emission"]]
dependent_var = co2_emmisions_with_aq["Value"]

display(independent_var)
display(dependent_var)

co2_aq_model.fit(independent_var, dependent_var)


# In[15]:


# Divide value to predict by max emission from training for normalization consistency
value_to_predict = (3.2 * 10**9) / max_co2_emission

print(co2_aq_model.predict(np.array([value_to_predict]).reshape(-1, 1)))


# In[35]:


emissions_per_year_per_gas = gas_types.groupby(['Year', 'Gas Name']).mean()

emissions_per_year_per_gas = emissions_per_year_per_gas.reset_index()

emissions_per_year_per_gas = emissions_per_year_per_gas.pivot(index='Year', columns='Gas Name', values='CO2 Emission').dropna()

display(emissions_per_year_per_gas)


# In[37]:


all_gasses_with_air_quality = emissions_per_year_per_gas.merge(
    air_quality_yearly_averages, left_index=True, right_index=True, how="inner")
display(all_gasses_with_air_quality) 


# In[67]:


independent_variables = all_gasses_with_air_quality.drop(columns=["Value"])
dependedent_variables = all_gasses_with_air_quality["Value"]
max_gas_emissions = independent_variables.max()

normalized_max_gas_emmisions = independent_variables / max_gas_emissions
display(normalized_max_gas_emmisions)


# In[62]:


model_with_gas_types = LinearRegression(fit_intercept=True)

model_with_gas_types.fit(normalized_max_gas_emmisions, dependedent_variables)

print(model_with_gas_types.coef_)


# In[72]:


example_value_to_predict = np.array([215409.963821, 427731.424518, 129820.451666, 623.485861, 29092.144228, 16215.268148, 4291.312665, 5294.825375, 32481.755893, 103245.245113, 27478.328136, 8.221518]).reshape(-1, 1)

normalized_values_to_predict = example_value_to_predict / np.array(max_gas_emissions).reshape(-1, 1)
normalized_values_to_predict = normalized_values_to_predict.T

prediction = model_with_gas_types.predict(normalized_values_to_predict)
print(prediction)
print(model_with_gas_types.coef_)


# In[ ]:




