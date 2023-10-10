def closest_coastline(input_coast_df,input_point):
    """Finds the closest distance from one input point to the lines in an input line dataframe"""
    dist = round( min([input_point.distance(coastline) for coastline in input_coast_df.geometry])/1000, 2)
    return dist