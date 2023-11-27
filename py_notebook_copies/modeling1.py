#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import punch_party_utils


# Let's view the first few columns of each dataframe to see what we are working with

# In[2]:


gas_types = punch_party_utils.make_gas_types_df(silent=False)


# The gas_type dataframe contains data about the location of emitter facilities and gas types emitted from each one. There are ~220,000 entries.

# In[3]:


air_quality = punch_party_utils.make_air_quality_df(silent=False)


# The air_quality dataframe contains air quality measures across different states/counties in the United States. It contains over 218,000 entries.

# In[4]:


facilities = punch_party_utils.make_facilities_df()


# The facilities dataframe contains data about each facility, namely address, location, and IDs (FIPS, NAICS). There are ~77,000 rows.

# # Question 1
# ## How does air quality relate to the number of emitting facilities and and level of emissions in the area?
# We can answer this question using the air_quality and gas_types dataframes. We can group facilities by county. Just for a trial run, let's pick a county that's in both dataframes

# In[6]:


# air_quality rows where Weston is the county
weston_aq = air_quality[(air_quality['CountyName'] == 'WASHINGTON')  & (air_quality['ReportYear'] == 2011)]
weston_aq.head()


# In[ ]:


gas_types.head()


# In[7]:


# gas_types rows where Weston is county
weston_gas_2013 = gas_types[(gas_types['County'] == 'WESTON') & (gas_types['Year'] == 2011)]
weston_gas_2013


# In[8]:


air_quality['CountyName'].value_counts()


# In[27]:


air_quality["StateName"].value_counts()


# In[15]:


gas_types['Year'].value_counts()


# In[16]:


air_quality['ReportYear'].value_counts()


# In[10]:


gas_types_texas= gas_types[gas_types["State Name"]=="TEXAS"]
air_quality_texas= air_quality[air_quality["StateName"]=="TEXAS"]


# In[11]:


air_quality_texas=air_quality_texas[air_quality_texas["MeasureType"]=="Average"]
air_quality_texas= air_quality_texas[air_quality_texas["ReportYear"]==2011]


gas_types_texas= gas_types[gas_types["Year"]==2011]


# In[5]:


gas_types_2011 = gas_types[gas_types["Year"]==2011]
air_quality_2011 = air_quality[air_quality["ReportYear"]==2011]


# In[6]:


air_quality_2011.to_csv("air_quality_2011.csv")


# In[44]:


gas_types_texas.value_counts()

'Address Line 1' 'City' 


# In[6]:


pivot_df = gas_types_2011.pivot_table(
    index='County',      # Rows (index) will be 'county'
    columns='Gas Code',  # Columns will be the unique values from 'gas_type'
    values='CO2 Emission',  # Values in the cells will be the 'emissions'
    aggfunc='sum'        # Aggregate function to combine emissions, sum in this case
)


# In[7]:


pivot_df.head()


# In[15]:


import geopandas as gpd

coastline = gpd.read_file('ne_10m_coastline/ne_10m_coastline.shp')


# In[16]:


coastline.crs


# In[22]:


gdf= gpd.GeoDataFrame(gas_types_2011, geometry=gpd.points_from_xy(gas_types_2011.Longitude, gas_types_2011.Latitude))


# In[20]:


coastline=coastline.to_crs("EPSG:5070")
coastline.crs


# In[23]:


from shapely.ops import nearest_points

def distance_to_coast(point, coastlines):
    nearest_coast = nearest_points(point, coastlines.unary_union)[1]
    return point.distance(nearest_coast)

# Ensure both dataframes use the same CRS
gdf = gdf.set_crs(coastline.crs)

gdf['distance_to_coast'] = gdf.geometry.apply(lambda x: distance_to_coast(x, coastline))


# In[24]:


gdf.head()


# In[22]:


import geopandas as gpd

coastline = gpd.read_file('ne_10m_coastline/ne_10m_coastline.shp')
gdf= gpd.GeoDataFrame(gas_types_2011, geometry=gpd.points_from_xy(gas_types_2011.Longitude, gas_types_2011.Latitude))
gdf = gdf.set_crs(coastline.crs)
gdf= gdf.to_crs("EPSG:5070")

coastline= coastline.to_crs("EPSG:5070")


# In[21]:


from shapely.ops import nearest_points

def distance_to_coast(point, coastlines):
    nearest_coast = nearest_points(point, coastlines.unary_union)[1]
    return point.distance(nearest_coast)


# In[25]:


gdf['distance_to_coast'] = gdf.geometry.apply(lambda x: distance_to_coast(x, coastline))


# In[26]:


gdf.head()


# In[114]:


gdf.to_csv('distance_from_coast.csv', index= False )


# In[65]:


cities=pd.read_excel("uscities.xlsx", sheet_name='Sheet1', engine='openpyxl')
cities.head()


# In[66]:


cities.columns


# In[67]:


cities['population'] = cities['population'].astype(int)
major_cities= cities[cities['population']>= 1000000]
major_cities.size


# In[68]:


gdf2= gpd.GeoDataFrame(gas_types_2011, geometry=gpd.points_from_xy(gas_types_2011.Longitude, gas_types_2011.Latitude))
gdf2 = gdf2.set_crs("EPSG:4326")
gdf2= gdf2.to_crs("EPSG:5070")

gcities = gpd.GeoDataFrame(major_cities, geometry=gpd.points_from_xy(major_cities.lng, major_cities.lat))
gcities=gcities.set_crs("EPSG:4326")
gcities=gcities.to_crs("EPSG:5070")


# In[69]:


def distance_to_nearest_major_city(point, major_cities):
    # Find the nearest major city to the given point
    nearest_city = nearest_points(point, major_cities.unary_union)[1]
    # Calculate the distance to the nearest major city
    return point.distance(nearest_city)


# In[105]:


gcities['city']= gcities['city'].str.upper()


# In[75]:


gdf2['is_major_city'] = gdf2['City'].apply(lambda x: 'yes' if x in gcities['city'].values else 'no')


# In[76]:


gdf2['distance_to_nearest_major_city'] = gdf2.geometry.apply(lambda x: distance_to_coast(x, gcities))


# In[77]:


gdf2.head()


# In[78]:


gdf2.loc[gdf2['is_major_city'] == 'yes', 'distance_to_nearest_major_city'] = 0


# In[79]:


gdf2.head()


# In[112]:


gdf2.to_csv('is_major_city.csv', index = False)


# In[81]:


gdf.head()


# In[82]:


gdf2.head()


# In[86]:


combined_gdf = gdf.merge(gdf2, left_index=True, right_index=True, how='outer')


# In[87]:


combined_gdf.head()


# In[89]:


combined_gdf = gdf.merge(gdf2, left_index=True, right_index=True, how='outer', suffixes=('', '_y'))
combined_gdf = combined_gdf.drop([col for col in combined_gdf if col.endswith('_y')], axis=1)


# In[90]:


combined_gdf.head()


# In[93]:


pivot_df = combined_gdf.pivot_table(
    index='Facility ID',      # Rows (index) will be 'county'
    columns='Gas Code',  # Columns will be the unique values from 'gas_type'
    values='CO2 Emission',  # Values in the cells will be the 'emissions'
    aggfunc='sum'        # Aggregate function to combine emissions, sum in this case
)


# In[94]:


pivot_df.head()


# In[96]:


pivot_df = combined_gdf.pivot_table(
    index='Facility ID',      # Rows (index) will be 'county'
    columns='Gas Code',  # Columns will be the unique values from 'gas_type'
    values='CO2 Emission',  # Values in the cells will be the 'emissions'
    aggfunc='sum'        # Aggregate function to combine emissions, sum in this case
)


# In[115]:


combined_gdf.head()


# In[97]:


pivot_df


# In[116]:


combined_gdf.columns


# In[119]:


pivot_df2 = combined_gdf.pivot_table(
    index=['Address Line 1', 'City','County','State Name', 'is_major_city', 'distance_to_nearest_major_city', 'distance_to_coast', 'Facility ID'], # Rows (index) will include these three columns
    columns='Gas Code',  # Columns will be the unique values from 'Gas Code'
    values='CO2 Emission',  # Values in the cells will be 'CO2 Emission'
    aggfunc='sum'        # Aggregate function to combine 'CO2 Emission', sum in this case
)


# In[120]:


pivot_df2


# In[121]:


model_df = pivot_df2.reset_index()
model_df = model_df.fillna(0)


# In[122]:


model_df.head()


# In[123]:


model_df.to_csv('modeling1.csv', index = False)


# In[124]:


df= pd.read_csv('modeling1.csv')


# In[125]:


df.head()


# In[126]:


air_quality_2011.head()


# In[127]:


air_quality_2011["MeasureType"].unique


# In[128]:


air_quality_2011.columns


# In[131]:


pivot_df3 = air_quality_2011.pivot_table(
    index=['CountyFips', 'CountyName','StateFips', 'StateName', 'MeasureId', 'MeasureName','StratificationLevel', 'Unit',  'DataOrigin', 'MonitorOnly' ], # Rows (index) will include these three columns
    columns='MeasureType',  
    values='Value',
    aggfunc= 'sum' 
) 


# In[132]:


pivot_df3


# In[ ]:


pivot_df3 = air_quality_2011.pivot_table(
    index=['CountyFips', 'CountyName','StateFips', 'StateName', 'MeasureId', 'MeasureName','StratificationLevel','Value', 'Unit',  'DataOrigin', 'MonitorOnly' ], # Rows (index) will include these three columns
    columns='MeasureType',  
    values='Value',
    aggfunc= 'sum' 
) 

