#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


import punch_party_utils


# In[2]:


air_quality_df = punch_party_utils.make_average_aq_df()
average_air_quality = air_quality_df[air_quality_df["MeasureName"] == "Annual average ambient concentrations of PM2.5 in micrograms per cubic meter (based on seasonal averages and daily measurement)"]


# For the first model, just CO2 emmisions in a given year -> air quality in a given year
air_quality_df = air_quality_df.drop(
    columns=["MeasureId", "MeasureName", "MeasureType", "StratificationLevel",
             "StateFips", "StateName", "CountyFips", "Unit",
             "UnitName", "DataOrigin", "MonitorOnly"])

# air_quality_df = air_quality_df.drop("CountyName")


# In[3]:


air_quality_df["County_Year"] = air_quality_df["CountyName"] + "_" + air_quality_df["ReportYear"].astype(str)


# In[4]:


print(len(air_quality_df))

aq_year_only = air_quality_df.drop(columns=["CountyName", "County_Year"])
display(aq_year_only.columns)
aq_by_year = aq_year_only.groupby("ReportYear")

print ("\n")

air_quality_yearly_averages = aq_by_year.agg("mean")
print(air_quality_yearly_averages)


# In[5]:


gas_types = punch_party_utils.make_gas_types_df()

gas_types = gas_types.drop(
    columns=["Address Line 1", "City", 
             "Facility ID", "Gas Code", "Latitude", "Longitude", 
             "State Name", "Zip Code", "Facility Name"])

gas_types["County_Year"] = gas_types["County"] + "_" + gas_types["Year"].astype(str)

display(gas_types.head())


# 

# In[6]:


raw_emmisions_year_only = gas_types.drop(columns=["Gas Name", "County", "County_Year"])
yearly_raw_emmisions = raw_emmisions_year_only.groupby("Year").agg("sum")
print(yearly_raw_emmisions)


# In[7]:


co2_emmisions_with_aq = yearly_raw_emmisions.merge(
    air_quality_yearly_averages, left_index=True, right_index=True, how="inner")
print(co2_emmisions_with_aq)


# In[8]:


# Normalize
max_co2_emission = np.max(co2_emmisions_with_aq["CO2 Emission"])
max_co2_emission
co2_emmisions_with_aq["CO2 Emission"] = co2_emmisions_with_aq["CO2 Emission"] / max_co2_emission

display(co2_emmisions_with_aq)


# In[9]:


co2_aq_model = LinearRegression(fit_intercept=True)

independent_var = co2_emmisions_with_aq[["CO2 Emission"]]
dependent_var = co2_emmisions_with_aq["Value"]

display(independent_var)
display(dependent_var)

co2_aq_model.fit(independent_var, dependent_var)


# In[10]:


# Divide value to predict by max emission from training for normalization consistency
value_to_predict = (3.2 * 10**9) / max_co2_emission

print(co2_aq_model.predict(np.array([value_to_predict]).reshape(-1, 1)))


# In[11]:


emissions_per_year_per_gas = gas_types.drop(columns=["County", "County_Year"]).groupby(['Year', 'Gas Name']).mean()

emissions_per_year_per_gas = emissions_per_year_per_gas.reset_index()

emissions_per_year_per_gas = emissions_per_year_per_gas.pivot(index='Year', columns='Gas Name', values='CO2 Emission').dropna()

display(emissions_per_year_per_gas.head())


# In[12]:


all_gasses_with_air_quality = emissions_per_year_per_gas.merge(
    air_quality_yearly_averages, left_index=True, right_index=True, how="inner")
display(all_gasses_with_air_quality) 


# In[13]:


def model_air_quality_from_multiple_gasses(gasses, aq_values):
    """ArithmeticError
    parameters
    ----------
    df : Dataframe
        A dataframe with an independent variable for each gas type we wish to use as a feature for air quality prediction.
    aq_values : Series
        A series representing the dependent variable to train on.

    returns
    -------
    A model that can predict air quality from a given input of gas types

    """
    model_with_gas_types = LinearRegression(fit_intercept=True)
    assert len(gasses) == len(aq_values), "Length of input dataframe does not equal length of output dataframe"

    model_with_gas_types.fit(gasses, aq_values)

    print("Intercept of the model:")
    print(model_with_gas_types.intercept_)
    print("\n")
    print("Features of the model:")
    print(gasses.columns.tolist())
    print("\n")
    print("Coefficients of the model:")
    print(model_with_gas_types.coef_)

    return model_with_gas_types


# In[14]:


all_gasses_per_year = all_gasses_with_air_quality.drop(columns=["Value"])
air_qualities_by_year = all_gasses_with_air_quality["Value"]
max_gas_emissions_per_year = all_gasses_per_year.max()
normalized_max_gas_emissions = all_gasses_per_year / max_gas_emissions_per_year
air_qualities_by_year = all_gasses_with_air_quality["Value"]

model_with_gas_types = model_air_quality_from_multiple_gasses(normalized_max_gas_emissions, air_qualities_by_year)


# In[15]:


example_value_to_predict = np.array([215409.963821, 427731.424518, 129820.451666, 623.485861, 29092.144228, 16215.268148, 4291.312665, 5294.825375, 32481.755893, 103245.245113, 27478.328136, 8.221518]).reshape(-1, 1)
max_gas_emissions = all_gasses_with_air_quality.drop(columns=["Value"]).max()
normalized_values_to_predict = example_value_to_predict / np.array(max_gas_emissions).reshape(-1, 1)
normalized_values_to_predict = normalized_values_to_predict.T

prediction = model_with_gas_types.predict(normalized_values_to_predict)
print(prediction)


# In[16]:


aq_county_year = air_quality_df.drop(columns=["CountyName", "ReportYear"])
display(aq_county_year.columns)
aq_county_year = aq_county_year.groupby("County_Year")

print ("\n")

air_quality_county_yearly_averages = aq_county_year.agg("mean")
print(air_quality_county_yearly_averages)


# In[17]:


print(gas_types)
raw_emmisions_county_year = gas_types.drop(columns=["Gas Name", "County", "Year"])
county_yearly_raw_emmisions = raw_emmisions_county_year.groupby("County_Year").agg("sum")
print(county_yearly_raw_emmisions)


# In[18]:


county_year_only = gas_types.drop(columns=["Year", "County"])


# In[19]:


emissions_per_county_year_per_gas = county_year_only.groupby(['County_Year', 'Gas Name']).mean()

emissions_per_county_year_per_gas = emissions_per_county_year_per_gas.reset_index()

emissions_per_county_year_per_gas = emissions_per_county_year_per_gas.pivot(index='County_Year', columns='Gas Name', values='CO2 Emission')

# Counting NaNs per column
# nan_count = emissions_per_county_year_per_gas.isna().sum()

# print(nan_count)

# The following gasses have NaN in over 10000 of the ~12000 rows of the emissions_per_county_year_per_gas dataframe, dropping these columns before modelling.
gasses_with_insufficient_measurements = ["HFCS", "HFES", "NITROGEN TRIFLOURIDE", "OTHER", "OTHER FULLY FLUORINATED GHGS", "PFCS", "SULFUR HEXAFLUORIDE", "VERY SHORT-LIVED COMPOUNDS"]

display(len(emissions_per_county_year_per_gas))
emissions_per_county_year_per_gas = emissions_per_county_year_per_gas.drop(columns=gasses_with_insufficient_measurements).dropna()
display(len(emissions_per_county_year_per_gas))

display(emissions_per_county_year_per_gas.head())


# In[20]:


gasses_with_air_quality_and_counties = emissions_per_county_year_per_gas.merge(
    air_quality_county_yearly_averages, left_index=True, right_index=True, how="inner")
display(gasses_with_air_quality_and_counties) 
display(len(gasses_with_air_quality_and_counties)) 


# In[21]:


gasses_with_air_quality_per_year_and_county = gasses_with_air_quality_and_counties.drop(columns=["Value"])
max_gas_emissions_by_county = gasses_with_air_quality_per_year_and_county.max()
normalized_max_gas_emissions_by_county = gasses_with_air_quality_per_year_and_county / max_gas_emissions_by_county
air_qualities_by_year_and_county = gasses_with_air_quality_and_counties["Value"]

x_train, x_test, y_train, y_test = train_test_split(normalized_max_gas_emissions_by_county, air_qualities_by_year_and_county)

model_with_counties_and_gas_types = model_air_quality_from_multiple_gasses(x_train, y_train)


# In[22]:


example_point_to_predict = np.array([16171.000000, 444627.100000, 18422.875000, 1329.974000]).reshape(-1, 1)

max_gas_emissions_per_county_per_year = gasses_with_air_quality_and_counties.drop(columns=["Value"]).max()
normalized_values_to_predict = example_point_to_predict / np.array(max_gas_emissions_by_county).reshape(-1, 1)
normalized_values_to_predict = normalized_values_to_predict.T

prediction = model_with_counties_and_gas_types.predict(normalized_values_to_predict)
print(prediction)


# In[23]:


y_train_pred_county_year =  model_with_counties_and_gas_types.predict(x_train)
y_test_pred_county_year =  model_with_counties_and_gas_types.predict(x_test)

rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred_county_year))
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred_county_year))

plt.figure(figsize=(8, 5))
plt.bar(['Train RMSE', 'Test RMSE'], [rmse_train, rmse_test], color=['blue', 'red'])
plt.ylabel('RMSE')
plt.title('Training and Test RMSE: air quality vs gas types prediction (no location version)')
plt.show()
plt.savefig("rmse_quality_vs_gas_county_predictions.png")

plt.figure()

