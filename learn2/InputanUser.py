data = input("masukan nama :")
print(data)

nilai = int(input("Masukan nilai 1 :"))
nilai2 = int(input("Masukan nilai 2 :"))
nilai3 = float(input("Masukan nilai 3 :"))
nilai3 = float(input("Masukan nilai 4 :"))


tambah = nilai + nilai2 + nilai3
kurang = nilai - nilai2 - nilai3
kali = nilai * nilai2 * nilai3
bagi = nilai / nilai2 / nilai3
pangkat = nilai**nilai2
modulus = nilai2%nilai
floor = nilai3//nilai2

print("Hasil pertambahan ",tambah)
print("Hasil pengurangan ",kurang)
print("Hasil perkalian ",kali)
print("Hasil pembagian ",bagi)
print("Hasil pangkat ",pangkat)
print("Hasil modulus ",modulus)
print("Hasil floor ",floor)
