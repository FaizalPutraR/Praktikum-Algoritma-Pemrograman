def main():
    
    
    print("""
=====================================
    
             Isal Food
         List Menu Makanan 
 
=====================================
   
     A. Ayam Penyet   : Rp 20.000
     B. Somay Batagor : Rp 10.000
     C. Nasi Gila     : Rp 10.000
     D. Nasi Goreng   : Rp 15.000

=====================================
   """"")
    nama=str(input("Masukan nama pelanggan = ")) 
    alamat=str(input("Masukkan alamat pelanggan = "))
    telpon=int(input("Masukkan Nomor Telepon +62 = "))
    # tanggal=str(input("Masukkan tanggal = "))
    pesan=str(input("masukkan list abjad menu makanan = "))
    jumlahpesan=int(input("masukkan jumlah pesanan = "))
   
    if pesan == "a":
        listnama= "Ayam Penyet"
        HargaBarang = 20000
        harga=(HargaBarang*jumlahpesan)
        ppn= int(harga * 0.1)
       
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    
    elif pesan == "b":
        listnama= "Somay Batagor"
        HargaBarang = 10000
        harga = (HargaBarang*jumlahpesan)
        ppn = int(harga * 0.1)
        
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    
    elif pesan == "c":
        listnama= "Nasi Gila"
        HargaBarang = 10000
        harga=int(HargaBarang*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
   
    elif pesan == "d":
        listnama= "Nasi Goreng"
        HargaBarang = 15000
        harga=int(HargaBarang*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    
    print("=========================")
    print("=======Isal Food=========")
    print("=========================")
    print("Nama Pelanggan :", nama)
    print("Masukkan Alamat :", alamat)
    print("Masukkan Telpon +62 :", telpon)
    import datetime
 
    x = datetime.datetime.now()
    print(x.strftime("%c"))

    # print("Masukkan tanggal :", tanggal)
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga Barang : ", HargaBarang)
    print("Harga Total :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    
    pilihan=input("apakah anda ingin order kembali Y/N =")
    if(pilihan == 'y'or pilihan == 'Y'):
        main()
    else:
        exit
main()