air_quality = pd.read_csv('us_air_quality_measures.csv')
# Below are the datasets in this repository
## us_air_quality_measures.csv
This file contains air quality measures across different states/counties in the United States. There are ~219,000 entries.
Columns are:

    - Measure ID
    - Measure name: name that specifies what type of measure was taken  (eg: "Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard," "Percent of days with PM2.5 levels over the National Ambient Air Quality Standard (monitor and modeled data)")
    - Measure type: eg Counts, Percent
    - StratificationLevel: StatexCounty for all
    - StateFips: ID code associated with each state/county. Ranges 1 - 56
    - StateName
    - CountyName
    - ReportYear: year the report was generated.
    - Value: value of air quality measurement.
    - Unit: unit symbol of air quality measurement.
    - UnitName: unit name of air quality measurement.
    - DataOrigin: how the measurement was taken (eg Monitor Only, Monitor & Modeled, etc)
    - MonitorOnly: boolean value saying if DataOrigin was MonitorOnly (we can drop this)

## us_greenhouse_gas_emission_direct_emitter_gas_type.csv
This file contains data about the location of emitter facilities and gas types emitted from each one. There are ~220,000 entries.
Columns are:

    - V_GHG_EMITTER_GAS.ADDRESS1: Street address of facility
    - V_GHG_EMITTER_GAS.ADDRESS2: Street address line 2
    - V_GHG_EMITTER_GAS.CITY: City of facility
    - V_GHG_EMITTER_GAS.CO2E_EMISSION: measure of CO2 emission from facility
    - V_GHG_EMITTER_GAS.COUNTY: County of facility
    - V_GHG_EMITTER_GAS.FACILITY_ID: Unique ID for each facility.
    - V_GHG_EMITTER_GAS.GAS_CODE: Chemical formula of gas (eg CH4)
    - V_GHG_EMITTER_GAS.GAS_NAME: Gas name (eg Methane)
    - V_GHG_EMITTER_GAS.LATITUDE: Latitude of facility
    - V_GHG_EMITTER_GAS.LONGITUDE: Longitude of facility
    - V_GHG_EMITTER_GAS.STATE: State (eg NY)
    - V_GHG_EMITTER_GAS.STATE_NAME: State name (eg New York)
    - V_GHG_EMITTER_GAS.YEAR: Year the record was taken
    - V_GHG_EMITTER_GAS.ZIP: Facility's zip code
    - V_GHG_EMITTER_GAS.FACILITY_NAME: Name of facility
    - V_GHG_EMITTER_GAS.COUNTY_FIPS: 5-digit code for facility (we should check if these values are unique)

## us_greenhouse_gas_emission_direct_emitter_facilities.csv
This file contains data about each facility, namely address, location, and IDs (FIPS, NAICS). There are ~77,000 entries.
Columns are:

    - V_GHG_EMITTER_FACILITIES.ADDRESS1: Street address of facility
    - V_GHG_EMITTER_FACILITIES.ADDRESS2: Street address line 2
    - V_GHG_EMITTER_FACILITIES.CEMS_USED: this column is empty so I do not know what it is meant to describe
    - V_GHG_EMITTER_FACILITIES.CITY: City of facility
    - V_GHG_EMITTER_FACILITIES.COUNTY: County of facility
    - V_GHG_EMITTER_FACILITIES.COUNTY_FIPS: 5-digit code (we should check if these values are unique and same as gas_types dataset)
    - V_GHG_EMITTER_FACILITIES.FACILITY_ID: 7-digit ID number (we should check if these are unique)
    - V_GHG_EMITTER_FACILITIES.LATITUDE: Latitude of facility
    - V_GHG_EMITTER_FACILITIES.LONGITUDE: Longitude of facility
    - V_GHG_EMITTER_FACILITIES.PRIMARY_NAICS_CODE: North American Industry Classification System (NAICS) code.
    - V_GHG_EMITTER_FACILITIES.STATE: State (eg NY)
    - V_GHG_EMITTER_FACILITIES.STATE_NAME: State name (eg New York)
    - V_GHG_EMITTER_FACILITIES.YEAR: Year the record was taken
    - V_GHG_EMITTER_FACILITIES.ZIP: Facility's zip code
    - V_GHG_EMITTER_FACILITIES.FACILITY_NAME: Name of facility.
    - V_GHG_EMITTER_FACILITIES.SECONDARY_NAICS_CODE: Secondary NAICS code. This column is empty for most entries.
    - V_GHG_EMITTER_FACILITIES.ADDITIONAL_NAICS_CODES: Additional NAICS code. This column is empty for most entries.
    - V_GHG_EMITTER_FACILITIES.COGENERATION_UNIT_EMISS_IND: Not sure what this column means. Most entries have 'N' for this column.
    - V_GHG_EMITTER_FACILITIES.EPA_VERIFIED: This column is empty for most entires, but contains 'Y' for some
    - V_GHG_EMITTER_FACILITIES.PARENT_COMPANY: parent company of the facility.
    - V_GHG_EMITTER_FACILITIES.PLANT_CODE_INDICATOR: This column contains the values Y or N.

## A few things to note:
1. The arrangement of columns is rather awkward. For example, the CO2 emission column is  between city and county columns in the gas_types dataset.
2. There is quite a bit of redundant data between and within datasets. For example, There are two state columns (one containing full state name and the other containing the abbreviation). We can discuss dropping and merging later.
3. If we are looking at air quality at different locations based on gas types and emission levels, the gas_types dataset may be (almost) sufficient, as the facilities dataset has no data about emissions, but may still be useful to add the parent company of each facility (if this is something we choose to explore).
