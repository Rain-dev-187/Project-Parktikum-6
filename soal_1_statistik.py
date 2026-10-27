"""
Soal Praktik 1 - Fungsi hitung_statistik()

Membuat fungsi yang menerima list angka dan mengembalikan dictionary
berisi mean, median, modus, range (max-min), dan standard deviation.
Hanya menggunakan standard library (statistics dan math).
"""

import math
import statistics


def hitung_statistik(data):
    """
    Menghitung statistik deskriptif dari sebuah list angka.

    Args:
        data (list): Daftar angka (int/float), minimal 1 elemen.

    Returns:
        dict: Berisi kunci 'mean', 'median', 'modus', 'range',
              dan 'standar_deviasi'.

    Raises:
        ValueError: Jika data kosong.
    """
    if not data:
        raise ValueError("Data tidak boleh kosong")

    mean = statistics.mean(data)
    median = statistics.median(data)

    # Modus: nilai yang paling sering muncul.
    # Jika semua nilai unik, statistics.mode mengembalikan nilai pertama.
    try:
        modus = statistics.mode(data)
    except statistics.StatisticsError:
        modus = None

    rentang = max(data) - min(data)

    # Standar deviasi populasi (dibagi n), sesuai contoh statistik
    # deskriptif pada modul. Dihitung manual dengan math.sqrt dan
    # dicek silang dengan statistics.pstdev.
    varians = sum((x - mean) ** 2 for x in data) / len(data)
    standar_deviasi = math.sqrt(varians)
    assert math.isclose(standar_deviasi, statistics.pstdev(data))

    return {
        "mean": mean,
        "median": median,
        "modus": modus,
        "range": rentang,
        "standar_deviasi": standar_deviasi,
    }


if __name__ == "__main__":
    nilai = [85, 90, 78, 92, 88, 90, 76, 90, 84, 95]
    hasil = hitung_statistik(nilai)

    print("Data nilai:", nilai)
    print("Hasil statistik:")
    for kunci, nilai_hasil in hasil.items():
        if isinstance(nilai_hasil, float):
            print(f"  {kunci:<16}: {nilai_hasil:.2f}")
        else:
            print(f"  {kunci:<16}: {nilai_hasil}")

    # Contoh data genap (median = rata-rata dua nilai tengah)
    data_genap = [70, 80, 90, 100]
    print("\nData genap:", data_genap)
    print("Hasil statistik:", hitung_statistik(data_genap))
