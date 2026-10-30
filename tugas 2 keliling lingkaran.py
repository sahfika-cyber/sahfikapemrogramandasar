print("===PROGRAM LINGKARAN===")
print("1.Menghitung Keliling Lingkaran")
print("2.Masukan Luas Lingkaran")

pilihan= int(input("Masukan pilihan(1/2):"))
r= float(input("Masukan jari-jari:"))

phi=3.14

if pilihan ==1:
   keliling=2*phi*r
   print("Keliling lingkaran=",keliling)
elif pilihan==2:
   luas=phi*r*r
   print("Luas lingkaran=",luas)

else:
   print("Pilihan tidak tersedia")



