# Data mahasiswa (contoh)
mahasiswa = [
    {"nama": "Garland", "nim": "122140001", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 78},
    {"nama": "Billy", "nim": "122140002", "nilai_uts": 70, "nilai_uas": 80, "nilai_tugas": 65},
    {"nama": "Marchel", "nim": "122140067", "nilai_uts": 60, "nilai_uas": 75, "nilai_tugas": 80},
    {"nama": "Ramon", "nim": "122140053", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 50},
    {"nama": "Ashoka", "nim": "122140123", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 85}
]

# Hitung nilai akhir dan tentukan grade
for mhs in mahasiswa:
    uts = mhs["nilai_uts"]
    uas = mhs["nilai_uas"]
    tugas = mhs["nilai_tugas"]
    
    nilai_akhir = (0.3 * uts) + (0.4 * uas) + (0.3 * tugas)
    mhs["nilai_akhir"] = round(nilai_akhir, 2)
    
    if nilai_akhir >= 80:
        mhs["grade"] = "A"
    elif 70 <= nilai_akhir < 80:
        mhs["grade"] = "B"
    elif 60 <= nilai_akhir < 70:
        mhs["grade"] = "C"
    elif 50 <= nilai_akhir < 60:
        mhs["grade"] = "D"
    else:
        mhs["grade"] = "E"

# Tampilkan data dalam tabel
print("="*75)
print(f"{'Nama':<15} | {'NIM':<10} | {'UTS':^5} | {'UAS':^5} | {'Tugas':^6} | {'Akhir':^6} | {'Grade':^5}")
print("="*75)
for mhs in mahasiswa:
    print(f"{mhs['nama']:<15} | {mhs['nim']:<10} | {mhs['nilai_uts']:^5} | {mhs['nilai_uas']:^5} | {mhs['nilai_tugas']:^6} | {mhs['nilai_akhir']:^6} | {mhs['grade']:^5}")

# Cari nilai tertinggi dan terendah
max_nilai = max(mhs["nilai_akhir"] for mhs in mahasiswa)
min_nilai = min(mhs["nilai_akhir"] for mhs in mahasiswa)

tertinggi = [mhs for mhs in mahasiswa if mhs["nilai_akhir"] == max_nilai]
terendah = [mhs for mhs in mahasiswa if mhs["nilai_akhir"] == min_nilai]

# Tampilkan hasil
print("\nMahasiswa dengan Nilai Tertinggi:")
for mhs in tertinggi:
    print(f"- {mhs['nama']} (NIM: {mhs['nim']}) dengan nilai akhir {mhs['nilai_akhir']}")

print("\nMahasiswa dengan Nilai Terendah:")
for mhs in terendah:
    print(f"- {mhs['nama']} (NIM: {mhs['nim']}) dengan nilai akhir {mhs['nilai_akhir']}")