"""
Soal Praktik 2 - Fungsi validasi_data()

Membuat fungsi yang menerima dictionary data dan schema validasi
(aturan tipe dan rentang), lalu mengembalikan tuple
(is_valid: bool, errors: list).

*args  : nama field tambahan yang wajib ada (di luar schema).
**kwargs: opsi tambahan, misalnya strict=True untuk menolak field
          yang tidak dikenal, atau label="..." untuk pesan error.
"""


def validasi_data(data, schema, *field_wajib, **opsi):
    """
    Memvalidasi data berdasarkan schema.

    Args:
        data (dict): Data yang akan divalidasi.
        schema (dict): Aturan per field, contoh:
            {
                "nama": {"tipe": str, "wajib": True, "min_panjang": 3},
                "umur": {"tipe": int, "min": 0, "max": 120},
                "ipk":  {"tipe": float, "min": 0.0, "max": 4.0},
            }
        *field_wajib: Nama field lain yang juga wajib ada.
        **opsi: strict=True -> field di luar schema dianggap error.

    Returns:
        tuple: (is_valid: bool, errors: list[str])
    """
    errors = []
    strict = opsi.get("strict", False)

    # Gabungkan field wajib dari schema dan dari *args
    wajib = {f for f, aturan in schema.items() if aturan.get("wajib", False)}
    wajib.update(field_wajib)

    # 1) Cek field wajib yang tidak ada / kosong
    for field in wajib:
        if field not in data or data[field] in (None, ""):
            errors.append(f"Field '{field}' wajib diisi")

    # 2) Cek setiap field yang ada di data terhadap aturan schema
    for field, nilai in data.items():
        if field not in schema:
            if strict:
                errors.append(f"Field '{field}' tidak dikenal dalam schema")
            continue

        aturan = schema[field]
        if nilai in (None, ""):
            continue  # kekosongan sudah dilaporkan pada langkah 1

        # Cek tipe data (bool adalah subclass int, harus ditolak untuk int)
        tipe = aturan.get("tipe")
        if tipe is not None:
            if tipe is int and isinstance(nilai, bool):
                errors.append(f"Field '{field}' harus bertipe int")
                continue
            if tipe is float and isinstance(nilai, (int, float)) \
                    and not isinstance(nilai, bool):
                nilai = float(nilai)  # int diterima sebagai float
            elif not isinstance(nilai, tipe):
                errors.append(
                    f"Field '{field}' harus bertipe {tipe.__name__}, "
                    f"didapat {type(nilai).__name__}"
                )
                continue

        # Cek rentang untuk angka
        if isinstance(nilai, (int, float)) and not isinstance(nilai, bool):
            if "min" in aturan and nilai < aturan["min"]:
                errors.append(
                    f"Field '{field}' bernilai {nilai}, "
                    f"di bawah minimum {aturan['min']}"
                )
            if "max" in aturan and nilai > aturan["max"]:
                errors.append(
                    f"Field '{field}' bernilai {nilai}, "
                    f"melebihi maksimum {aturan['max']}"
                )

        # Cek panjang untuk string
        if isinstance(nilai, str):
            if "min_panjang" in aturan and len(nilai) < aturan["min_panjang"]:
                errors.append(
                    f"Field '{field}' terlalu pendek "
                    f"(min {aturan['min_panjang']} karakter)"
                )
            if "max_panjang" in aturan and len(nilai) > aturan["max_panjang"]:
                errors.append(
                    f"Field '{field}' terlalu panjang "
                    f"(maks {aturan['max_panjang']} karakter)"
                )

    return (len(errors) == 0, errors)


if __name__ == "__main__":
    schema_mahasiswa = {
        "nama": {"tipe": str, "wajib": True, "min_panjang": 3},
        "nim": {"tipe": str, "wajib": True, "min_panjang": 10,
                "max_panjang": 12},
        "umur": {"tipe": int, "min": 15, "max": 60},
        "ipk": {"tipe": float, "min": 0.0, "max": 4.0},
    }

    # Contoh 1: data valid
    data_valid = {"nama": "Budi Santoso", "nim": "20241320031",
                  "umur": 20, "ipk": 3.75}
    valid, errors = validasi_data(data_valid, schema_mahasiswa)
    print("Data valid  :", data_valid)
    print("  -> is_valid:", valid, "| errors:", errors)

    # Contoh 2: data tidak valid (nama pendek, umur di bawah min,
    # ipk melebihi max, field wajib 'nim' hilang)
    data_rusak = {"nama": "Bo", "umur": 12, "ipk": 4.5}
    valid, errors = validasi_data(data_rusak, schema_mahasiswa)
    print("\nData rusak  :", data_rusak)
    print("  -> is_valid:", valid)
    for e in errors:
        print("   -", e)

    # Contoh 3: *args (field wajib tambahan 'email') dan
    # **kwargs (strict=True menolak field tak dikenal 'hobi')
    data_lain = {"nama": "Ani Wijaya", "nim": "20241320002",
                 "umur": 21, "ipk": 3.9, "hobi": "membaca"}
    valid, errors = validasi_data(
        data_lain, schema_mahasiswa, "email", strict=True
    )
    print("\nData lain   :", data_lain)
    print("  -> is_valid:", valid)
    for e in errors:
        print("   -", e)
