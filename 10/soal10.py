import shapefile #mengimpor modul shapefile
w=shapefile.Writer("soal10", shapeType=5) #untuk membuat shapefile baru
w.shapeType=5 #menyeting menggunakan jenis shape apa (point,polygon)

#mem#membuat dbs dengan 1 field, berupa kolom
w.field("Nama Bangun","C") 
 
w.record("Segitiga sama sisi","Ida") #membuat record dengan isi kolom 1 "Segitiga sama sisi" dan kolom dua "satu"

#membuat 1 row karena menggunakan 1 record
w.poly([[[-3,1],[0,6], [3,1],[-1,1]]]) #membuat polygon


w.close()#melakukan save dengan nama (soal10)