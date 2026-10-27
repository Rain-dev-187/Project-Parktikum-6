"""
Soal Praktik 3 - Module utilitas_akademik.py

Modul utilitas akademik berisi fungsi:
- konversi_nilai_huruf(): mengubah nilai angka (0-100) menjadi huruf & bobot
- hitung_ipk()          : menghitung IPK berbobot SKS dari daftar mata kuliah
- generate_transkrip()  : membuat transkrip nilai dalam bentuk teks

Setiap file dilengkapi blok if __name__ == "__main__" untuk testing.
"""

# Tabel konversi: (batas bawah nilai, huruf, bobot)
_TABEL_NILAI = [
    (85, "A", 4.0),
    (80, "AB", 3.5),
    (75, "B", 3.0),
    (70, "BC", 2.5),
    (65, "C", 2.0),
    (60, "CD", 1.5),
    (55, "D", 1.0),
    (0, "E", 0.0),
]


def konversi_nilai_huruf(nilai):
    """
    Mengonversi nilai angka (0-100) menjadi (huruf, bobot).

    Args:
        nilai (float): Nilai angka 0-100.

    Returns:
        tuple: (huruf: str, bobot: float), contoh (85) -> ("A", 4.0)

    Raises:
        ValueError: Jika nilai di luar rentang 0-100.
    """
    if not 0 <= nilai <= 100:
        raise ValueError("Nilai harus berada pada rentang 0-100")
    for batas, huruf, bobot in _TABEL_NILAI:
        if nilai >= batas:
            return huruf, bobot
    return "E", 0.0  # tidak akan tercapai karena batas terakhir 0


def hitung_ipk(daftar_mk):
    """
    Menghitung IPK berbobot SKS.

    Args:
        daftar_mk (list): List dictionary dengan kunci
            "matakuliah" (str), "sks" (int), "nilai" (float 0-100).

    Returns:
        float: IPK = sum(bobot x sks) / total sks, dibulatkan 2 desimal.
               Mengembalikan 0.0 jika daftar kosong.
    """
    if not daftar_mk:
        return 0.0
    total_bobot = 0.0
    total_sks = 0
    for mk in daftar_mk:
        _, bobot = konversi_nilai_huruf(mk["nilai"])
        total_bobot += bobot * mk["sks"]
        total_sks += mk["sks"]
    if total_sks == 0:
        return 0.0
    return round(total_bobot / total_sks, 2)


def generate_transkrip(nama, nim, daftar_mk):
    """
    Membuat transkrip nilai mahasiswa dalam bentuk string teks.

    Args:
        nama (str): Nama mahasiswa.
        nim (str): Nomor induk mahasiswa.
        daftar_mk (list): Format sama seperti pada hitung_ipk().

    Returns:
        str: Transkrip lengkap berisi tabel nilai dan IPK akhir.
    """
    garis = "=" * 56
    baris = [
        garis,
        "TRANSKRIP NILAI MAHASISWA",
        garis,
        f"Nama : {nama}",
        f"NIM  : {nim}",
        "-" * 56,
        f"{'Mata Kuliah':<32}{'SKS':>5}{'Nilai':>8}{'Huruf':>7}",
        "-" * 56,
    ]
    for mk in daftar_mk:
        huruf, _ = konversi_nilai_huruf(mk["nilai"])
        baris.append(
            f"{mk['matakuliah']:<32}{mk['sks']:>5}"
            f"{mk['nilai']:>8}{huruf:>7}"
        )
    total_sks = sum(mk["sks"] for mk in daftar_mk)
    baris += [
        "-" * 56,
        f"Total SKS : {total_sks}",
        f"IPK       : {hitung_ipk(daftar_mk):.2f}",
        garis,
    ]
    return "\n".join(baris)


if __name__ == "__main__":
    # Testing modul secara langsung (tidak jalan saat di-import)
    print("Testing konversi_nilai_huruf:")
    for n in (92, 83, 77, 68, 50):
        print(f"  Nilai {n} -> {konversi_nilai_huruf(n)}")

    contoh = [
        {"matakuliah": "Pemrograman Python", "sks": 3, "nilai": 88},
        {"matakuliah": "Basis Data", "sks": 3, "nilai": 79},
        {"matakuliah": "Sistem Informasi", "sks": 2, "nilai": 91},
    ]
    print("\nTesting hitung_ipk:", hitung_ipk(contoh))
    print("\nTesting generate_transkrip:")
    print(generate_transkrip("Budi Santoso", "20241320031", contoh))
