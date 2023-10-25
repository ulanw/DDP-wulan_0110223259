kendaraan=["B 1234 EDI","Motor",110,"Hitam"]
print(kendaraan)

kendaraan.append("Rp.17.000.000")
kendaraan.append("2")
kendaraan.insert(2,"beat")
kendaraan.insert(1,"matic")
print("setelah memiliki motor ini saya gunakan untuk berangkat kulyeah")
print(kendaraan)
#nmr2
menghitung = input("memasukan operasi cara menghitung: ")
match menghitung:
    case "persegi":
        sisi=int (input("masukan nilai:"))
        luas=sisi*sisi
        print(luas)
    case "lingkaran":
        jarijari=int(input("masukan nilai"))
        luas=3.14*jarijari*jarijari
        print(luas)
    case "segitiga":
        alas=int(input("masukan nilai:"))
        tinggi=int(input("masukan nilai:"))
        luas=alas*tinggi*1/2
        print(luas)

