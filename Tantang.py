from Prima import is_prima

nilaiAwal = 1
nilaiAkhir = 25

while (nilaiAwal <= nilaiAkhir):
    hasil = "Prima" if is_prima(nilaiAwal) else "Bukan Prima"
    print(nilaiAwal, hasil)
    daftar = [nilaiAwal, hasil]
    nilaiAwal = nilaiAwal + 1

fileHasil = open("hasil.txt", "w")
fileHasil.write(daftar)
fileHasil.close()