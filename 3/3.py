import shapefile
sf = shapefile.Reader("soal1.shp")
sb = sf.bbox
print(sb)