# Praktikum Pertemuan 6 — Function, Module & Package

Modul: Pemrograman Python — Function, Parameter, Return Value, Scope,
Lambda, Module, Package & Library
Program Studi Sistem Informasi

## Struktur File

| File | Keterangan |
|---|---|
| `soal_1_statistik.py` | Soal Praktik 1 — fungsi `hitung_statistik()` |
| `soal_2_validasi.py` | Soal Praktik 2 — fungsi `validasi_data()` dengan `*args` dan `**kwargs` |
| `utilitas_akademik.py` | Soal Praktik 3 — modul berisi `hitung_ipk()`, `konversi_nilai_huruf()`, `generate_transkrip()` |
| `main.py` | Soal Praktik 3 — file utama yang mengimpor `utilitas_akademik` |
| `sistem_informasi/` | Soal Praktik 4 — package dengan subpackage `model`, `service`, `utils` |
| `demo_sistem_informasi.py` | Soal Praktik 4 — menjalankan skenario CRUD Mahasiswa |
| `soal_5_api.py` | Soal Praktik 5 — ambil data JSONPlaceholder dengan `requests`, proses dengan lambda/`map`/`filter`/`sorted`, simpan JSON |
| `hasil_analisis_api.json` | Hasil keluaran Soal Praktik 5 |

## Cara Menjalankan

```powershell
python soal_1_statistik.py
python soal_2_validasi.py
python main.py
python demo_sistem_informasi.py
python soal_5_api.py        # butuh koneksi internet dan library requests
```

Instal library untuk Soal 5 (jika belum ada):

```powershell
pip install requests
```

## Bukti Hasil Run

**Soal Praktik 1 dan 2:**

![Bukti Soal 1-2](bukti_praktikum_soal1-2.png)

**Soal Praktik 3:**

![Bukti Soal 3](bukti_praktikum_soal3.png)

**Soal Praktik 4:**

![Bukti Soal 4](bukti_praktikum_soal4.png)

**Soal Praktik 5:**

![Bukti Soal 5](bukti_praktikum_soal5.png)

---

# Jawaban Soal Teori

## 1. Perbedaan parameter dan argumen

Parameter adalah variabel yang ditulis pada definisi fungsi sebagai
penampung nilai yang akan diterima. Argumen adalah nilai nyata yang
diberikan saat fungsi dipanggil.

Contoh:

```python
def hitung_pajak(harga, tarif):   # harga dan tarif = PARAMETER
    return harga * tarif

pajak = hitung_pajak(100000, 0.11)  # 100000 dan 0.11 = ARGUMEN
```

Analogi sederhananya: parameter adalah kolom kosong pada formulir,
sedangkan argumen adalah data yang diisikan ke kolom tersebut.

## 2. Aturan LEGB dalam scope Python

LEGB adalah urutan pencarian nama variabel oleh Python, dari lingkup
terdalam sampai terluar:

1. **Local (L)** — variabel yang dibuat di dalam fungsi yang sedang
   berjalan. Contoh: variabel `total` di dalam fungsi `hitung()`
   hanya dikenal di fungsi itu.
2. **Enclosing (E)** — variabel pada fungsi luar yang membungkus
   fungsi dalam (nested function). Contoh: fungsi dalam membaca
   variabel `faktor` milik fungsi luarnya pada pola closure.
3. **Global (G)** — variabel yang dibuat di tingkat modul (di luar
   semua fungsi). Contoh: konstanta `PI = 3.14159` di awal file dapat
   dibaca oleh semua fungsi dalam file tersebut.
4. **Built-in (B)** — nama bawaan Python yang selalu tersedia.
   Contoh: `print()`, `len()`, dan `range()` tidak perlu dibuat atau
   diimpor terlebih dahulu.

Python mencari nama mulai dari Local, lalu Enclosing, Global, dan
terakhir Built-in. Jika tidak ditemukan di semua level, terjadi
`NameError`.

## 3. Pitfall objek mutable sebagai default parameter

Nilai default parameter hanya dievaluasi **satu kali**, yaitu saat
fungsi didefinisikan, bukan setiap fungsi dipanggil. Jika nilai
default itu objek mutable (list, dict, set), objek yang sama dipakai
bersama oleh semua pemanggilan. Akibatnya, perubahan pada satu
pemanggilan "bocor" ke pemanggilan berikutnya:

```python
def tambah_item(item, keranjang=[]):   # BERBAHAYA
    keranjang.append(item)
    return keranjang

tambah_item("apel")    # ['apel']
tambah_item("jeruk")   # ['apel', 'jeruk']  <- seharusnya ['jeruk']
```

Solusi yang benar adalah memakai `None` sebagai nilai penanda
(sentinel), lalu membuat objek baru di dalam fungsi:

```python
def tambah_item(item, keranjang=None):   # BENAR
    if keranjang is None:
        keranjang = []
    keranjang.append(item)
    return keranjang
```

## 4. Perbedaan module dan package, serta peran `__init__.py`

Module adalah satu file Python (`.py`) yang berisi fungsi, kelas, dan
variabel yang dapat diimpor, misalnya `utilitas_akademik.py`. Package
adalah direktori yang berisi kumpulan module (dan dapat berisi
subpackage) sehingga impor dapat bertingkat dengan notasi titik,
misalnya `sistem_informasi.service.mahasiswa_service`.

Peran file `__init__.py` dalam package:

1. Menandai bahwa direktori tersebut adalah package Python.
2. Menjalankan kode inisialisasi saat package pertama kali diimpor.
3. Mendefinisikan `__all__` untuk mengatur nama apa saja yang
   diekspor saat `import *`.
4. Dapat mengimpor nama-nama penting dari submodul agar mudah
   diakses langsung dari package.

## 5. Kapan menggunakan lambda dan kapan menggunakan def

Lambda lebih tepat digunakan pada:

1. Fungsi satu ekspresi yang sangat singkat, misalnya
   `lambda x: x ** 2`.
2. Fungsi yang dipakai satu kali sebagai key pada `sorted()`,
   `min()`, atau `max()`, misalnya `key=lambda m: m["ipk"]`.
3. Callback singkat pada `map()` dan `filter()` untuk transformasi
   atau penyaringan sederhana.

Fungsi `def` lebih tepat digunakan pada:

1. Logika yang panjang atau terdiri dari banyak langkah, karena
   lambda hanya boleh berisi satu ekspresi.
2. Fungsi yang dipakai berulang kali di banyak tempat, sehingga
   perlu nama yang jelas dan mudah dipanggil kembali.
3. Fungsi yang membutuhkan dokumentasi (docstring), penanganan
   error (`try/except`), atau pengujian (unit test) secara serius.
