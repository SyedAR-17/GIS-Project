#Libraries
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#import the csv file
df = pd.read_csv('google_maps.csv')

#Convert the csv file into a Geo Data Frame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.long, df.lat), crs = "EPSG:4326")

#Print the contents of the file
print(gdf)

#Plot the points
gdf.plot()
plt.show()