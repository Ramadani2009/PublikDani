def soal():
	global soal1,soal2,soal3,soal4,soal5
	print('tolong isi dengan huruf BESAR')
	soal1 = input('1.Siapa namaku?:')
	soal2 = input('2.dimana rumahku?:')
	soal3 = input('3.dimana sekolahku?:')
	soal4 = input('4.kelas berapa aku?:')
	soal5 = input('5.apa kemampuanku?:')

print('Assalamualaikum Wr.Wb')
a = input('Mau isi survey [ya/tidak]:')

if a == 'ya':
	soal()
else:
	print('oke')

score=0
if soal1 == 'RAMADANI':
	score += 20
elif soal1 == 'RAMADANI DWI CAHYONO':
	score += 20
elif soal1 == 'DANI':
	score += 20
else:
	print('no 1 salah')

if soal2 == 'BANYUANYAR':
	score += 20
else:
	print('no 2 salah')

if soal3 == 'SMPN 1 GURAH':
	score += 20
elif soal3 == 'SMP NEGERI 1 GURAH':
	score += 20
else:
	print('no 3 salah')

if soal4 == '9':
	score += 20
else:
	print('no 4 salah')

if soal5 == 'CODING':
	score += 20
else:
	print('no 5 salah')
	
print('Nilai anda',score)

hadiah = input('Masukkan nilaimu:')
if hadiah == '100':
	print('Selamat anda dapat Rp 100.000')
elif hadiah == '80':
	print('Selamat anda dapat Rp 50.000')
elif hadiah == '60':
	print('Selamat anda dapat Rp 25.000')
elif hadiah == '40':
	print('Selamat anda dapat Rp 15.000')