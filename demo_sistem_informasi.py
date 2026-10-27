"""
Soal Praktik 4 - demo_sistem_informasi.py

Menjalankan skenario CRUD terhadap package sistem_informasi
menggunakan absolute import dari luar package.
"""

from sistem_informasi.service import (
    tambah_mahasiswa,
    ambil_mahasiswa,
    semua_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa,
)


def tampilkan_judul(teks):
    print(f"\n--- {teks} ---")


def main():
    tampilkan_judul("CREATE: tambah 3 mahasiswa")
    tambah_mahasiswa("20241320031", "Ahmad Sahrul Fadhillah",
                      "Sistem Informasi", 3.75)
    tambah_mahasiswa("20241320003", "Dzikri Sagara",
                      "Sistem Informasi", 3.60)
    tambah_mahasiswa("20241320014", "Eka Febryanto",
                      "Sistem Informasi", 3.82)
    for mhs in semua_mahasiswa():
        print(" ", mhs)

    tampilkan_judul("CREATE gagal: NIM duplikat & IPK tidak valid")
    try:
        tambah_mahasiswa("20241320031", "Duplikat", "Sistem Informasi", 3.0)
    except ValueError as e:
        print("  Error:", e)
    try:
        tambah_mahasiswa("20241320099", "Fauzi Akbar",
                         "Sistem Informasi", 4.5)
    except ValueError as e:
        print("  Error:", e)

    tampilkan_judul("READ: ambil NIM 20241320003")
    print(" ", ambil_mahasiswa("20241320003"))
    print("  NIM tidak terdaftar ->", ambil_mahasiswa("9999999999"))

    tampilkan_judul("UPDATE: ubah IPK 20241320003 menjadi 3.85")
    print(" ", ubah_mahasiswa("20241320003", ipk=3.85))

    tampilkan_judul("DELETE: hapus NIM 20241320014")
    print("  Berhasil dihapus:", hapus_mahasiswa("20241320014"))
    print("  Hapus lagi (sudah tidak ada):", hapus_mahasiswa("20241320014"))

    tampilkan_judul("READ: data akhir")
    for mhs in semua_mahasiswa():
        print(" ", mhs)
    print(f"\nTotal mahasiswa tersimpan: {len(semua_mahasiswa())}")


if __name__ == "__main__":
    main()
