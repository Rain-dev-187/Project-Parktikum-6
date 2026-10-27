"""Subpackage service: operasi CRUD mahasiswa."""

from .mahasiswa_service import (
    tambah_mahasiswa,
    ambil_mahasiswa,
    semua_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa,
)

__all__ = [
    "tambah_mahasiswa",
    "ambil_mahasiswa",
    "semua_mahasiswa",
    "ubah_mahasiswa",
    "hapus_mahasiswa",
]
