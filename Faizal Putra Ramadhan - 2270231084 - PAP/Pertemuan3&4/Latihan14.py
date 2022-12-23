#Halaman 34 Modul Praktikum Algoritma Pemrograman
#Create by ASLAB ELITS 2022

data="ini adalah string"
print(data)
print(type(data))

#1. Cara Membuat String
#a. dengan mengunakkan single quote '...'
#b. dengan mengunakkan double quote "..."

data='Mengunakkan single quote'
print(data)

data='Mengunakkan double quote'
print(data)

print("Halo, apa kabar?")
print("ini adalah hari Jum'at")

#2. Mengunakkan tanda \

#membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

#Backlash
print("C:\\user\\Ucup")

#tab
print("ucup\t\t\totong, semakin jauhan")

#backspace
print("ucup \botong, jadi deketan")

#newline
print("baris pertama.\nbaris kedua.") #LF-> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") #CR-> carriage return-> commodore, acron, lisp
print("baris pertama.\r\nbaris kedua.") #CRLF-> line feed carriage return-> dipakai oleh windows

#3. String literal atau raw
# Hati-hati
print('C:\new folder') #akan salah pathnya

# Menggunakan raw string
print(r'C:\new folder')

# Multiline literal string
print("""
Nama: Ucup
Kelas: 3 SD
""")

# Multiline literal string dan RAW
print(r"""
Nama: Ucup
Kelas: 3 SD\new normal
Website: www.ucup.com/newID
""")