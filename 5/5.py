import shapefile
sf = shapefile.Reader("soal1.shp")
sp = sf.shapes()
print(dir(sp[0]))
print(dir(sp))