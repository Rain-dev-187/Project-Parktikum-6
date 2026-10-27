"""
Modul service/mahasiswa_service.py

Implementasi CRUD (Create, Read, Update, Delete) entitas Mahasiswa
di atas penyimpanan in-memory (dictionary) dari subpackage model.
Menggunakan relative import untuk mengambil model dan utils.
"""

from ..model.mahasiswa import Mahasiswa, database_mahasiswa
from ..utils.validasi import validasi_nim, validasi_ipk, validasi_teks


def tambah_mahasiswa(nim, nama, jurusan, ipk=0.0):
    """CREATE: menambah mahasiswa baru. NIM tidak boleh duplikat."""
    validasi_nim(nim)
    validasi_teks(nama, "Nama")
    validasi_teks(jurusan, "Jurusan")
    validasi_ipk(ipk)
    if nim in database_mahasiswa:
        raise ValueError(f"Mahasiswa dengan NIM {nim} sudah terdaftar")
    mhs = Mahasiswa(nim, nama, jurusan, float(ipk))
    database_mahasiswa[nim] = mhs
    return mhs.to_dict()


def ambil_mahasiswa(nim):
    """READ (satu): mengambil data mahasiswa berdasarkan NIM."""
    mhs = database_mahasiswa.get(nim)
    return mhs.to_dict() if mhs is not None else None


def semua_mahasiswa():
    """READ (semua): mengembalikan list seluruh data mahasiswa."""
    return [mhs.to_dict() for mhs in database_mahasiswa.values()]


def ubah_mahasiswa(nim, **field_baru):
    """
    UPDATE: mengubah field nama/jurusan/ipk mahasiswa yang sudah ada.
    Field diberikan sebagai keyword argument, contoh:
    ubah_mahasiswa("20241320031", ipk=3.9)
    """
    mhs = database_mahasiswa.get(nim)
    if mhs is None:
        raise ValueError(f"Mahasiswa dengan NIM {nim} tidak ditemukan")
    for field, nilai in field_baru.items():
        if field == "nama":
            validasi_teks(nilai, "Nama")
            mhs.nama = nilai
        elif field == "jurusan":
            validasi_teks(nilai, "Jurusan")
            mhs.jurusan = nilai
        elif field == "ipk":
            validasi_ipk(nilai)
            mhs.ipk = float(nilai)
        else:
            raise ValueError(f"Field '{field}' tidak dapat diubah")
    return mhs.to_dict()


def hapus_mahasiswa(nim):
    """DELETE: menghapus mahasiswa berdasarkan NIM. True jika berhasil."""
    if nim in database_mahasiswa:
        del database_mahasiswa[nim]
        return True
    return False


if __name__ == "__main__":
    # Testing service secara langsung dari dalam package:
    # jalankan dengan: python -m sistem_informasi.service.mahasiswa_service
    print(tambah_mahasiswa("20241320031", "Budi", "Sistem Informasi", 3.75))
    print(semua_mahasiswa())
