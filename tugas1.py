print("PROGRAM HITUNG GAJI KARYAWAN")
print("------------------------------------")

nama = input("Nama Karyawan     : ")
jabatan = input("Golongan Jabatan  [1/2/3] : ")
pendidikan = input("Pendidikan [SMA/D1/D3/S1] : ")
jamkerja = int(input("Jumlah Jam Kerja  : "))

# Proses Gaji Pokok berdasarkan Golongan
gaji_pokok = 300000

# Proses Tunjangan Jabatan
if jabatan == "1":
    tj_jabatan = 0.05 * gaji_pokok
elif jabatan == "2":
    tj_jabatan = 0.15 * gaji_pokok
elif jabatan == "3":
    tj_jabatan = 0.30 * gaji_pokok
else:
    tj_jabatan = 0
    print("Golongan tidak dikenal, tunjangan jabatan = 0")

# Proses Tunjangan Pendidikan
if pendidikan.upper() == "SMA":
    tj_pendidikan = 0.025 * gaji_pokok
elif pendidikan.upper() == "D1":
    tj_pendidikan = 0.05 * gaji_pokok
elif pendidikan.upper() == "D3":
    tj_pendidikan = 0.20 * gaji_pokok
elif pendidikan.upper() == "S1":
    tj_pendidikan = 0.30 * gaji_pokok
else:
    tj_pendidikan = 0
    print("Pendidikan tidak dikenal, tunjangan pendidikan = 0")

# Proses Honor Lembur
if jamkerja > 8:
    lembur = (jamkerja - 8) * 3500
else:
    lembur = 0

# Total Gaji
total_gaji = gaji_pokok + tj_jabatan + tj_pendidikan + lembur

# Layar Keluaran
print("\n------------------------------------")
print("Karyawan yang bernama :", nama)
print("Honor yang diterima")
print("Tunjangan Jabatan     : Rp", tj_jabatan)
print("Tunjangan Pendidikan  : Rp", tj_pendidikan)
print("Honor Lembur          : Rp", lembur)
print("------------------------------------")
print("Total Gaji            : Rp", total_gaji)
print("------------------------------------")
