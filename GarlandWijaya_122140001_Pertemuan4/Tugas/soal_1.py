# Program Penghitung BMI (Body Mass Index)
# Masukkan berat badan dalam kg dan tinggi badan dalam meter
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

# Hitung BMI
bmi = berat / (tinggi ** 2)

# Tentukan kategori BMI
if bmi < 18.5:
    kategori = "Berat badan kurang"
elif 18.5 <= bmi < 25:
    kategori = "Berat badan normal"
elif 25 <= bmi < 30:
    kategori = "Berat badan berlebih"
else:
    kategori = "Obesitas"

# Tampilkan hasil
print(f"\nBMI Anda: {bmi:.2f}")
print(f"Kategori: {kategori}")