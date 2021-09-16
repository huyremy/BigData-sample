from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import netCDF4

plt.figure()
url='https://nomads.ncep.noaa.gov/dods/wave/nww3/nww320210316/nww320210316_06z'

file = netCDF4.Dataset(url)
lat  = file.variables['lat'][:]
lon  = file.variables['lon'][:]
data = file.variables['htsgwsfc'][1,:,:]
file.close()

m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution='c', lat_1=21.,lat_2=55,lat_0=50,lon_0=105.)
            
x, y = m(*np.meshgrid(lon,lat))

m.pcolormesh(x,y,data,shading='auto',cmap='Blues')
m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()
m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])

plt.title('HuyRemy just said: Very Big Data. ')
plt.show()
