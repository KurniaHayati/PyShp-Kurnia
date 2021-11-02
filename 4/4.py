import shapefile
sf = shapefile.Reader("soal1.shp")
sp = sf.shapes()
print(len(sp))