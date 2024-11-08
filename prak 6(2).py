# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:17:33 2024

@author: Lenovo
"""

def cek_tahun_kabisat(tahun):
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

def jumlah_hari(bulan, tahun):
    if bulan < 1 or bulan > 12:
        return "Bulan tidak valid. Masukkan angka antara 1 dan 12."
    
    hari_setiap_bulan = {1: 31, 2: 29 if cek_tahun_kabisat(tahun) else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }
    return hari_setiap_bulan[bulan]

while True:
    try:
        bulan = int(input("Masukkan bulan (1-12, atau 0 untuk menghentikan program): "))
        tahun = int(input("Masukkan tahun (atau 0 untuk menghentikan program): "))

        if bulan == 0 or tahun == 0:
            print("Terimakasih sudah menggunakan program, sampai berjumpa lagi.")
            break 
        
        print(f"Jumlah hari di bulan {bulan} tahun {tahun} adalah {jumlah_hari(bulan, tahun)} hari.")
    except ValueError:
        print("Input tidak valid. Masukkan angka yang sesuai untuk bulan dan tahun.")        