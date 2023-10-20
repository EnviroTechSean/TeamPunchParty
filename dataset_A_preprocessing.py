#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import urllib


# # Download the data
# 
# If `wget` is not installed on your machine, you may want to try `curl URL > file.txt` or the `urllib` package in python.

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'mkdir data_ghcn\ncd data_ghcn\nwget https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt\nwget https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2021.csv.gz\ngzip -d 2021.csv.gz\n')


# # Data Preprocessing

# In[ ]:


def get_vals(line):
    ls = line.split(',')
    station = ls[0]
    time = ls[1]
    val = float(ls[3])
    return [station, time, val]

def get_stations(filename='data_ghcn/ghcnd-stations.txt'):
    df = pd.read_csv(filename, '/t', header=None)
    df = df[0].str.split(expand=True)[[0, 1, 2, 3]]
    df.columns = ['Station', 'Latitude', 'Longitude', 'Elevation']
    return df

def process_year(year, stations, col='TAVG', basedir='data_ghcn'):
    tavg = []
    with open(os.path.join(basedir, "%s.csv" % year)) as h:
        l = h.readline()
        while l:
            if col in l:
                v = get_vals(l)
                if stations['Station'].str.contains(v[0]).any():
                    tavg.append(get_vals(l))
            l = h.readline()
    df_tavg = pd.DataFrame(tavg, columns=['Station', 'Date', col])
    df_merged = df_tavg.merge(stations, left_on='Station', right_on='Station', how='left')
    df_merged['Date'] = df_merged['Date'].apply(pd.Timestamp)
    for c in ['Latitude', 'Longitude', col, 'Elevation']:
        df_merged[c] = df_merged[c].astype(float)
    return df_merged[['Station', 'Date', col, 'Latitude', 'Longitude', 'Elevation']]


# In[ ]:


stations = get_stations()
df1 = process_year('2021', stations, col='TAVG')
stations = stations[stations.Station.isin(df1.Station)]


# In[ ]:


df2 = process_year('2021', stations, col='PRCP')


# In[ ]:


df = df1.merge(df2[['Station', 'Date', 'PRCP']], on=['Station', 'Date'])
# df.to_csv('data_ghcn/daily_global_weather_2020.csv')
df

