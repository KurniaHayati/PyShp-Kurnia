import shapefile
sf = shapefile.Reader("soal1.shp")
namakolom = sf.fields
print(namakolom)