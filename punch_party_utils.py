import pandas as pd

def make_air_quality_df(filename='us_air_quality_measures.csv', silent=True):
    air_quality = pd.read_csv(filename)
    # MAKE STATE AND COUNTY NAMES UPPERCASE
    air_quality['StateName'] = air_quality['StateName'].str.upper()
    air_quality['CountyName'] = air_quality['CountyName'].str.upper()

    # DROP COLUMNS WHERE THE 'Value' COLUMN IS 0.000000
    #air_quality = air_quality[air_quality['Value'] != 0.000000]

    if not silent:
        print("air_quality.head():")
        air_quality.head()

    return air_quality

def make_facilities_df(filename='us_greenhouse_gas_emissions_direct_emitter_facilities.csv', silent=True):
    facilities_df = pd.read_csv(filename)

    # RENAME ALL COLUMNS SO IT'S NOT SUCH AN EYESORE
    columns_and_renames = {
        'V_GHG_EMITTER_FACILITIES.ADDRESS1': 'Address Line 1',
        'V_GHG_EMITTER_FACILITIES.ADDRESS2': 'Address Line 2',
        'V_GHG_EMITTER_FACILITIES.CEMS_USED': 'CEMS Used',
        'V_GHG_EMITTER_FACILITIES.CITY': 'City',
        'V_GHG_EMITTER_FACILITIES.COUNTY': 'County',
        'V_GHG_EMITTER_FACILITIES.COUNTY_FIPS': 'FIPS',
        'V_GHG_EMITTER_FACILITIES.FACILITY_ID': 'Facilities ID',
        'V_GHG_EMITTER_FACILITIES.LATITUDE': 'Latitude',
        'V_GHG_EMITTER_FACILITIES.LONGITUDE': 'Longitude',
        'V_GHG_EMITTER_FACILITIES.PRIMARY_NAICS_CODE': 'NAICS Code',
        'V_GHG_EMITTER_FACILITIES.STATE': 'State',
        'V_GHG_EMITTER_FACILITIES.STATE_NAME': 'State Name',
        'V_GHG_EMITTER_FACILITIES.YEAR': 'Year',
        'V_GHG_EMITTER_FACILITIES.ZIP': 'Zip Code',
        'V_GHG_EMITTER_FACILITIES.FACILITY_NAME': 'Facility Name',
        'V_GHG_EMITTER_FACILITIES.SECONDARY_NAICS_CODE': 'Secondary NAICS Code',
        'V_GHG_EMITTER_FACILITIES.ADDITIONAL_NAICS_CODES': 'Additional NAICS Codes',
        'V_GHG_EMITTER_FACILITIES.COGENERATION_UNIT_EMISS_IND': 'Cogeneration Unit Emission Index(?)',
        'V_GHG_EMITTER_FACILITIES.EPA_VERIFIED': 'EPA Verified',
        'V_GHG_EMITTER_FACILITIES.PARENT_COMPANY': 'Parent Company',
        'V_GHG_EMITTER_FACILITIES.PLANT_CODE_INDICATOR': 'Plant Code Indicator',
    }
    facilities_df = facilities_df.rename(columns=columns_and_renames)

    # MAKE ADDRESSES ALL UPPERCASE, THEN DROP ROWS WITH NO ADDRESS
    facilities_df['Address Line 1'] = facilities_df['Address Line 1'].str.upper()
    facilities_df = facilities_df.dropna(subset=['Address Line 1'] )

    #add2_nan = facilities['Address Line 2'].isna().sum()
    #add2_nan

    if not silent:
        print("facilities_df.head():")
        facilities_df.head()

    return facilities_df


def make_gas_types_df(filename='us_greenhouse_gas_emission_direct_emitter_gas_type.csv', silent=True):
    gas_types = pd.read_csv(filename)

    # RENAME ALL COLUMNS SO IT'S NOT SUCH AN EYESORE
    gas_type_renames = { 
        'V_GHG_EMITTER_GAS.ADDRESS1': 'Address Line 1',
        'V_GHG_EMITTER_GAS.ADDRESS2': 'Address Line 2',
        'V_GHG_EMITTER_GAS.CITY': 'City',
        'V_GHG_EMITTER_GAS.CO2E_EMISSION': 'CO2 Emission',
        'V_GHG_EMITTER_GAS.COUNTY': 'County',
        'V_GHG_EMITTER_GAS.FACILITY_ID': 'Facility ID',
        'V_GHG_EMITTER_GAS.GAS_CODE': 'Gas Code',
        'V_GHG_EMITTER_GAS.GAS_NAME': 'Gas Name',
        'V_GHG_EMITTER_GAS.LATITUDE': 'Latitude',
        'V_GHG_EMITTER_GAS.LONGITUDE': 'Longitude',
        'V_GHG_EMITTER_GAS.STATE': 'State',
        'V_GHG_EMITTER_GAS.STATE_NAME': 'State Name',
        'V_GHG_EMITTER_GAS.YEAR': 'Year',
        'V_GHG_EMITTER_GAS.ZIP': 'Zip Code',
        'V_GHG_EMITTER_GAS.FACILITY_NAME': 'Facility Name',
        'V_GHG_EMITTER_GAS.COUNTY_FIPS': 'FIPS',
    }
    gas_types = gas_types.rename(columns = gas_type_renames)

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

    if not silent:
        print("gas_types.head():")
        print(gas_types.head())