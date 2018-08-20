# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:43:42 2018

@author: Raymond
"""
import numpy.ma as ma
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import dascutils.io as dio
import pymap3d.aer as pm
thefile=dio.load('tests','cal/PKR_DASC_20110112')
thepicture=thefile[428]
picture=thepicture.isel(time=1)
alt=100000
srange=alt/np.sin(np.radians(thefile.el))
lat,lon,alt=pm.aer2geodetic(thefile.az,thefile.el,srange,thefile.lat,thefile.lon,0)
p = ccrs.PlateCarree()
ax = plt.axes(projection=p)
ax.set_extent((-180,-120,50,75))
ax.gridlines()
ax.coastlines()
ax.pcolor(lon,lat,picture)
plt.show()#goes
