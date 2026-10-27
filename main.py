"""
Soal Praktik 3 - main.py

File utama yang mengimpor dan menggunakan modul utilitas_akademik.
Menunjukkan tiga cara import: import modul, from-import, dan alias.
"""

# Cara 1: import seluruh modul
import utilitas_akademik

# Cara 2: from-import nama tertentu
from utilitas_akademik import generate_transkrip

# Cara 3: import dengan alias
from utilitas_akademik import konversi_nilai_huruf as konversi


def main():
    daftar_mk = [
        {"matakuliah": "Pemrograman Python", "sks": 3, "nilai": 88},
        {"matakuliah": "Business Intelligence", "sks": 3, "nilai": 85},
        {"matakuliah": "Basis Data", "sks": 3, "nilai": 79},
        {"matakuliah": "Sistem Pendukung Keputusan", "sks": 2,
         "nilai": 91},
        {"matakuliah": "Statistika", "sks": 2, "nilai": 74},
    ]

    # Menggunakan modul lewat nama modul (cara 1)
    ipk = utilitas_akademik.hitung_ipk(daftar_mk)
    print(f"IPK mahasiswa: {ipk:.2f}")

    # Menggunakan fungsi hasil from-import (cara 2)
    print()
    print(generate_transkrip("Ahmad Sahrul Fadhillah", "20241320031",
                             daftar_mk))

    # Menggunakan alias (cara 3)
    print("\nContoh konversi nilai:")
    for nilai in (95, 82, 66, 45):
        huruf, bobot = konversi(nilai)
        print(f"  Nilai {nilai} -> huruf {huruf} (bobot {bobot})")


if __name__ == "__main__":
    main()
