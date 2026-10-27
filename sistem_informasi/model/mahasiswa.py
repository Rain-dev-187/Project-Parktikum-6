"""
Modul model/mahasiswa.py

Mendefinisikan entitas Mahasiswa dan penyimpanan in-memory
berupa dictionary global: database_mahasiswa = {nim: Mahasiswa}.
"""


class Mahasiswa:
    """Representasi entitas mahasiswa."""

    def __init__(self, nim, nama, jurusan, ipk=0.0):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def to_dict(self):
        """Mengubah objek menjadi dictionary."""
        return {
            "nim": self.nim,
            "nama": self.nama,
            "jurusan": self.jurusan,
            "ipk": self.ipk,
        }

    def __repr__(self):
        return (f"Mahasiswa(nim={self.nim!r}, nama={self.nama!r}, "
                f"jurusan={self.jurusan!r}, ipk={self.ipk})")


# Penyimpanan in-memory: {nim (str): objek Mahasiswa}
database_mahasiswa = {}


if __name__ == "__main__":
    m = Mahasiswa("20241320031", "Budi Santoso", "Sistem Informasi", 3.75)
    print(m)
    print(m.to_dict())
