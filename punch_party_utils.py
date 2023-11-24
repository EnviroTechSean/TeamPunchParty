def make_air_quality_df(filename, silent = True):
    air_quality = pd.read_csv(filename)
    # MAKE STATE AND COUNTY NAMES UPPERCASE
    air_quality['StateName'] = air_quality['StateName'].str.upper()
    air_quality['CountyName'] = air_quality['CountyName'].str.upper()

    if not silent:
        print("air_quality.head():\n")
        air_quality.head()

    return air_quality