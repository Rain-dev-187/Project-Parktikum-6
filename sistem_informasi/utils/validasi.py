"""
Modul utils/validasi.py

Fungsi-fungsi validasi data mahasiswa. Setiap fungsi melempar
ValueError dengan pesan yang jelas jika data tidak valid.
"""


def validasi_nim(nim):
    """NIM harus string berisi 10-12 digit angka."""
    if not isinstance(nim, str) or not nim.isdigit():
        raise ValueError("NIM harus string berisi angka saja")
    if not 10 <= len(nim) <= 12:
        raise ValueError("NIM harus terdiri dari 10-12 digit")
    return True


def validasi_ipk(ipk):
    """IPK harus angka pada rentang 0.0 - 4.0."""
    if isinstance(ipk, bool) or not isinstance(ipk, (int, float)):
        raise ValueError("IPK harus berupa angka")
    if not 0.0 <= float(ipk) <= 4.0:
        raise ValueError("IPK harus berada pada rentang 0.0 - 4.0")
    return True


def validasi_teks(teks, nama_field="Field"):
    """Teks tidak boleh kosong setelah spasi dihilangkan."""
    if not isinstance(teks, str) or not teks.strip():
        raise ValueError(f"{nama_field} tidak boleh kosong")
    return True


if __name__ == "__main__":
    print(validasi_nim("20241320031"))
    print(validasi_ipk(3.75))
    print(validasi_teks("Budi", "Nama"))
    try:
        validasi_ipk(4.5)
    except ValueError as e:
        print("Error tertangkap:", e)
