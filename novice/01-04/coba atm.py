user_id = 0
loop = "n"
user =  [
            {   
                "id":"1999",
                "no_rek":"1212121212",
                "username":"Iklimah",
                "pin":"2702",
                "saldo":10000000
            },
            {   
                "id":"1998",
                "no_rek":"1313131313",
                "username":"Iniya",
                "pin":"2020",
                "saldo":20000000
            }
        ]
status_login = False
pake_atm = "y"
 
def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False       
     
def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1
 
def cek_rek(no):
    for i in range(len(user)):
        if str(user[i]['no_rek']) == str(no):
            return int(i)
    return -1
 
def transfer_uang(uang,no_rek):
    index1 = cek_user(user_id)
    index2 = cek_rek(no_rek)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang)
            user[index2]['saldo'] =user[index2]['saldo'] + int(uang)
            print("Selamat anda berhasil mentransfer uang Rp."+str(uang)+" ke nomer rekening "+no_rek)
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Maaf saldo anda tidak cukupi")
             
def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang) 
            print("Anda berhasil menarik uang Rp."+str(uang))
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Maaf saldo anda tidak cukupi")
 
 
while pake_atm == "y":
    while status_login == False:
        print("Welcome,, selamat datang")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")
     
        cl = cek_login(pin)
        if cl != False:
            print("selamat data "+cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ulangi PIN dengan benar")
            print("")
            print("")
     
    while loop == "y" and status_login == True:
        u = user[cek_user(user_id)]
        print("Welcome,,, Ahlan Wa Sahlan")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.",u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk mentransfer silahkan masukan Nomer Rekening tujuan")
            no_rek = input("Masukan Nomer Rekening tujuan : ")
            cnk = cek_rek(no_rek)
             
            if cnk >= 0:
                print("Nomor rekening benar,silahkan masukan nominal yang akan ditransfer")
                nominal = input("Nominal yang akan ditransfer : ")
                tranfer_uang(nominal,no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening ujuan Tidak ditemukan / terdaftar")
                print("")
                loop = "n"
                 
        elif a == 3:
            nominal = input("Nominal yang akan ditarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
             
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan ngga tersedia")
        if status_login == True:
             
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"