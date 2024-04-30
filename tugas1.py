print("Selamat Datang di Aplikasi Perhitungan Nilai Akhir Mahasiswa")

tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = 0.25 * tugas + 0.35 * uts + 0.40 * uas

if nilai_akhir > 85:
    nilai_huruf = "A"
elif nilai_akhir > 80:
    nilai_huruf = "A-"
elif nilai_akhir > 75:
    nilai_huruf = "B+"
elif nilai_akhir > 70:
    nilai_huruf = "B"
elif nilai_akhir > 65:
    nilai_huruf = "B-"
elif nilai_akhir > 60:
    nilai_huruf = "C+"
elif nilai_akhir > 55:
    nilai_huruf = "C"
elif nilai_akhir > 50:
    nilai_huruf = "C-"
elif nilai_akhir > 30:
    nilai_huruf = "D"
else:
    nilai_huruf = "E"

print("\nNilai akhir:", nilai_akhir)
print("Nilai huruf:", nilai_huruf)