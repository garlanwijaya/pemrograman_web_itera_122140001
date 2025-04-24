import math_operations
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin

# Contoh penggunaan fungsi geometri
print("=== PERHITUNGAN GEOMETRI ===")
sisi_persegi = 12
print(f"Persegi (sisi={sisi_persegi})")
print(f"- Luas      : {math_operations.luas_persegi(sisi_persegi)}")
print(f"- Keliling  : {math_operations.keliling_persegi(sisi_persegi)}")

panjang = 8
lebar = 11
print(f"\nPersegi Panjang ({panjang}x{lebar})")
print(f"- Luas      : {math_operations.luas_persegi_panjang(panjang, lebar)}")
print(f"- Keliling  : {math_operations.keliling_persegi_panjang(panjang, lebar)}")

radius = 11
print(f"\nLingkaran (r={radius})")
print(f"- Luas      : {math_operations.luas_lingkaran(radius):.2f}")
print(f"- Keliling  : {math_operations.keliling_lingkaran(radius):.2f}")

# Contoh penggunaan konversi suhu
suhu_celsius = 23
print("\n=== KONVERSI SUHU ===")
print(f"{suhu_celsius}°C:")
print(f"- Fahrenheit: {celsius_ke_fahrenheit(suhu_celsius)}°F")
print(f"- Kelvin    : {celsius_ke_kelvin(suhu_celsius)}K")