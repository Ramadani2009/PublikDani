saldo = 0
saldos = str(saldo)

nama_file = "saldo.txt"
with open(nama_file, 'w') as file:
	file.write(saldos)

def menu():
    datar = ["1. Tarik Saldo", "2. Cek saldo", "3.Keluar"]
    for i in datar:
        print(i)

def menu_input():
    global saldo
    user = int(input("Masukkan no Menu: "))
    
    if user == 1:
       tarik_saldo = int(input("Masukkan jumlah saldo: "))
       if tarik_saldo > saldo:
            print("Saldo tidak cukup!")
       else:
            saldo -= tarik_saldo
            print("Saldo anda berhasil ditarik")
        
    elif user == 2:
        print(f"Saldo Anda: Rp {saldo}")
            
    elif user == 3:
        print("Terima kasih! Program diakhiri.")
        exit()
        
    else:
        print("Menu tidak valid!")
        user = int(input("Masukkan no Menu: "))

# Program utama
while True:
    menu()
    menu_input()
    print()  # Baris kosong untuk pemisah