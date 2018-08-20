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
# =============================================================================
# from django.contrib.gis.db.models.functions import GeoFunc
# 
# class MyMakeValid(GeoFunc):
#       function='ST_MakeValid'
# 
# AerowayPolygon.objects.all().update(geom=MyMakeValid('geom'))
#
# =============================================================================
# P = ccrs.PlateCarree()
# =============================================================================
# =============================================================================
thefile=dio.load('tests','cal/PKR_DASC_20110112')
thepicture=thefile[428]
picture=thepicture.isel(time=1)
alt=100000
srange=alt/np.sin(np.radians(thefile.el))
lat,lon,alt=pm.aer2geodetic(thefile.az,thefile.el,srange,thefile.lat,thefile.lon,0)
# =============================================================================
# lat=np.resize(lat,(1024,1024))
# lon=np.resize(lon,(1024,1024))
# picture=np.resize(picture,(1024,1024))
# =============================================================================
# =============================================================================
# bad = np.isnan(lat.values) | np.isnan(lon.values)
# latm = lat.values
# latm[bad] = float(0)
# lonm = lon.values
# lonm[bad] = float(0)
# img = ma.masked_where(bad, picture.values)
# =============================================================================
p = ccrs.PlateCarree()
#p = ccrs.Stereographic()
ax = plt.axes(projection=p)
# =============================================================================
# ax = plt.figure().gca(projection=p)
# =============================================================================
ax.set_extent((-180,-120,50,75))
ax.gridlines()
ax.coastlines()
# =============================================================================
# x,y,z=pm.aer2ecef(thefile.az,thefile.el,srange,thefile.lat,thefile.lon,0)
# =============================================================================
#ax.pcolor(lat[::4,::4],lon[::4,::4],picture[::4,::4])
ax.pcolor(lon,lat,picture)
plt.show()#goes
# =============================================================================
# emptylist=[]
# for i in lat:
#     i=ma.masked_values(i,'nan')
#     emptylist.append(i)
# print(emptylist)
# =============================================================================
print(picture)