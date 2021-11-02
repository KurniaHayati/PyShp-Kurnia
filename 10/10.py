import shapefile
sf = shapefile.Reader("soal1.shp")
isidata = sf.records()
print(isidata)