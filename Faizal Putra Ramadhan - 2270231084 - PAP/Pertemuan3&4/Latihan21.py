# Latihan Percabangan

# Kalkulator sederhana
print(20*"=")
print("kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukkan angka 1="))
operator = input("operator(+,-,x,/):")
angka_2 = float(input("masukkan amgka 2 ="))

# Percabangannya
if operator =="+":
  hasil = angka_1 + angka_2
  print(f"hasilnya adalah {hasil}")
elif operator =="-":
  hasil = angka_1 - angka_2
  print(f"hasilnya adalah {hasil}")
elif operator =="x" or operator =="*":
  hasil = angka_1 * angka_2 
  print(f"hasilnya adalah {hasil}")
elif operator =="/":
  hasil = angka_1 / angka_2
  print(f"hasilnya adalah {hasil}")
else:
  print("masukkan yang benar dong!, aku pusying")
  print("Akhir dari program, terima gajih!")