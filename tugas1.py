Nama_karyawan = input("Masukan Nama Karyawan: ")
Jabatan = input('Pilih Jabatan [1/2/3]: ')
pendidikan = input('Pilih Pendidikan [SMA/D1/D3/S1]: ')
jam_kerja = int(input('Masukan Jam Kerja:'))

gaji_pokok = 300000

if Jabatan == '1':
    tuj_jabatan = 0.05 *    gaji_pokok
elif Jabatan == '2':
    tuj_jabatan = 0.10 * gaji_pokok
elif Jabatan == '3':
    tuj_jabatan = 0.30 * gaji_pokok
else:
    tuj_jabatan = 0
    print('Jabatan Tidak Valid')

if pendidikan == 'SMA' or 'sma':
   tunj_pendidikan =  0.025 * gaji_pokok
elif pendidikan == 'D1':
    tunj_pendidikan = 0.05 * gaji_pokok
elif pendidikan == 'D3':
    tunj_pendidikan = 0.20 * gaji_pokok
elif pendidikan == 'S1':
    tunj_pendidikan = 0.30 * gaji_pokok
else:
    tunj_pendidikan = 0
    print('Pendidikan Tidak Valid')

if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0

total_gaji = gaji_pokok + tuj_jabatan + tunj_pendidikan + lembur
print('============================== test')
print('Nama Karyawan :', Nama_karyawan)
print('Golongan Jabatan :', Jabatan)
print('Pendidikan :', pendidikan)
print('Jam Kerja :', jam_kerja)
print('Gaji Pokok :', gaji_pokok)
print('Tunjungan Jabatan :', tuj_jabatan )
print('Tunjungan Pendidikan :', tunj_pendidikan )
print('Lembur :', lembur)
print('Total Gaji :', total_gaji )