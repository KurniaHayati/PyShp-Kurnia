import shapefile
sf = shapefile.Reader("soal1.shp")
sp = sf.shapes()
anu = sp[1].parts
print(anu)