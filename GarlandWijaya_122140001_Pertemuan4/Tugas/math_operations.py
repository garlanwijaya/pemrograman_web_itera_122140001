PI = 3.14159

def luas_persegi(sisi):
    return sisi ** 2

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_lingkaran(r):
    return PI * r ** 2

def keliling_lingkaran(r):
    return 2 * PI * r

def celsius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_ke_kelvin(c):
    return c + 273.15