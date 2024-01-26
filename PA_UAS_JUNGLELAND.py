### IMPORT SYSTEM OS UNTUK INTERAKSI DENGAN SISTEM OS ###
import os

### MENDEFINISIKAN 'cls' SEBAGAI clear() ###
def clear():
    os.system('cls')

    ### MEMASUKKAN HARI UNTUK PENGINPUTAN AWAL ###
def input_hari():
    while True:
        print("""
+====== SELAMAT DATANG ======+
|                            |
|      JADWAL JUNGLELAND     |      
|                            |      
|       Senin - Minggu       |
|                            |
+============================+
""")
        ### Fungsi global digunakan untuk membuat variabel menjadi lingkup global ###
        global hari
        hari = input("\nMasukkan Hari Berkunjung : ")
        if hari.lower() in ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]:
            break
        else:
            clear()
            print("\nMasukkan Hari Yang Benar")

def pilihan_tiket():
    clear()
    print("+====================================================================+")
    if hari.lower() in ["selasa", "jumat"]:
        print("| 1. REGULER                                                         |")
        print("|    Weekday : Rp. 155.000/orang                                     |")
        print("|    Weekend : Rp. 175.000/orang                                     |")
        print("| 2. PROMO MAIN & KELILING JUNGLELAND NAIK BUGGY CAR (PAKET 2 ORANG) |")
        print("|    Weekday : Rp. 250.000                                           |")
        print("|    Weekend : Rp. 300.000                                           |")
        print("| 3. PROMO SELA & JULEHA (PAKET 4 ORANG)                             |")
        print("|    Rp. 350.000                                                     |")
        print("+====================================================================+")
    else:
        print("| 1. REGULER                                                         |")
        print("|    Weekday : Rp. 155.000/orang                                     |")
        print("|    Weekend : Rp. 175.000/orang                                     |")
        print("| 2. PROMO MAIN & KELILING JUNGLELAND NAIK BUGGY CAR (PAKET 2 ORANG) |")
        print("|    Weekday : Rp. 250.000                                           |")
        print("|    Weekend : Rp. 300.000                                           |")
        print("| 3. PROMO SELA & JULEHA (PAKET 4 ORANG)                             |")
        print("|    Rp. 350.000                                                     |")
        print("+====================================================================+")

### INPUT JENIS TIKET ###
def input_jenis_tiket():
    while True:
        jenis_tiket = input("\nPilih jenis tiket : ")
        if jenis_tiket.isdigit() and 1 <= int(jenis_tiket) <= 3:
            if hari.lower() not in ["selasa", "jumat"] and int(jenis_tiket) == 3:
                print("Jenis tiket 3 hanya tersedia pada hari Selasa dan Jumat.")
            else:
                return int(jenis_tiket)
        else:
            print("Masukkan pilihan yang ada.")

### MENGHITUNG HARGA TIKET ###
def hitung_harga_tiket(jenis_tiket):
    global harga_satuan
    if jenis_tiket == 1:
        if hari.lower() in ["senin", "selasa", "rabu", "kamis", "jumat"]:
            harga_satuan = 155000
        else:
            harga_satuan = 175000
    elif jenis_tiket == 2:
        if hari.lower() in ["senin", "selasa", "rabu", "kamis", "jumat"]:
            harga_satuan = 250000
        else:
            harga_satuan = 300000
    elif jenis_tiket == 3:
        harga_satuan = 350000
    return harga_satuan

input_hari()   # MEMANGGIL DEFINISI input_hari()
total_tiket = 0   # VARIABEL TOTAL TIKET
tiket_dibeli = []   # UNTUK MEMBUAT LIST TIKET YANG DIBELI

### INPUT JUMLAH TIKET JIKA MEMILIH JENIS TIKET 1 (REGULER) ###
while True:
    pilihan_tiket()
    jenis_tiket = input_jenis_tiket()
    
    harga_satuan = hitung_harga_tiket(jenis_tiket)

    if jenis_tiket == 1:
        tiket = int(input("Jumlah tiket yang ingin anda beli? "))
    
    ## KONDISI JIKA MEMILIH TIKET 2 ATAU 3 ##
    elif jenis_tiket in [2, 3]:
        tiket = 1

    total_tiket += tiket
    
    ## MEMBUAT AGAR PEMBELIAN TIKET TIDAK TERDUPLIKASI  ##
    tiket_duplikat= False
    for i, (jenis, jumlah) in enumerate(tiket_dibeli):
        if jenis == jenis_tiket:
            tiket_dibeli[i] = (jenis, jumlah + tiket)
            tiket_duplikat= True
            break

    if not tiket_duplikat:
        tiket_dibeli.append((jenis_tiket, tiket))

    ## LOOP UNTUK MEMBELI TIKET LAGI ##
    beli_lagi = input("Apakah anda ingin membeli tiket lagi? (y/n) ")
    if beli_lagi.lower() != "y":
        break

clear()
print("\n=========== KONFIRMASI PEMESANAN ============")

total_biaya = 0 

### MEMANGGIL HASIL PERHITUNGAN ###
for jenis, jumlah in tiket_dibeli:
    if jenis == 1:
        print("\nREGULER")
        print("Hari Kunjungan      :", hari.capitalize())
        print(f"Jumlah              : {jumlah}" )
        if hari.lower() in ["sabtu", "minggu"]:
            harga_satuan = 175000
        else:
            harga_satuan = 155000
    elif jenis == 2:
        print("\nPROMO MAIN & KELILING JUNGLELAND NAIK BUGGY CAR (PAKET 2 ORANG)")
        print("Hari Kunjungan      :", hari.capitalize())
        print(f"Jumlah              : {jumlah}" )
        if hari.lower() in ["sabtu", "minggu"]:
            harga_satuan = 300000
        else:
            harga_satuan = 250000
    else:
        print("\nPROMO SELA & JULEHA (PAKET 4 ORANG)")
        print("Hari Kunjungan      :", hari.capitalize())
        print(f"Jumlah              : {jumlah}" )
        harga_satuan = 350000

    harga_total = jumlah * harga_satuan
    total_biaya += harga_total
    admin_fee = 5000 * total_tiket 
    
    print("Harga Satuan (Rp)   :", harga_satuan)
    print("Harga Total (Rp)    :", harga_total)

total_biaya += admin_fee

print("\nJumlah Pembelian    :", total_tiket)
print("Admin Fee (Rp)      :", admin_fee)
print("TOTAL (Rp)          :", total_biaya)