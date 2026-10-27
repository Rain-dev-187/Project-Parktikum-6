"""
Soal Praktik 5 - Mengambil & menganalisis data dari Public REST API

Program mengambil data dari JSONPlaceholder (https://jsonplaceholder.typicode.com)
menggunakan library requests, lalu memprosesnya dengan lambda dan
higher-order function (map, filter, sorted). Hasil analisis disimpan
ke file JSON menggunakan modul json.
"""

import json

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
FILE_HASIL = "hasil_analisis_api.json"


def ambil_data(endpoint):
    """Mengambil data JSON dari endpoint API. None jika gagal."""
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Gagal mengambil data '{endpoint}': {e}")
        return None


def main():
    users = ambil_data("users")
    posts = ambil_data("posts")
    if users is None or posts is None:
        return

    print(f"Data diterima: {len(users)} user, {len(posts)} post")

    # --- map() + lambda: daftar nama dan email semua user ---
    daftar_nama = list(map(lambda u: u["name"], users))
    daftar_email = list(map(lambda u: u["email"], users))

    # --- filter() + lambda: user dengan email berakhiran .biz ---
    user_biz = list(filter(lambda u: u["email"].endswith(".biz"), users))
    nama_user_biz = list(map(lambda u: u["name"], user_biz))

    # --- Hitung jumlah post per user (filter di dalam map) ---
    jumlah_post = list(map(
        lambda u: {
            "id": u["id"],
            "nama": u["name"],
            "kota": u["address"]["city"],
            "jumlah_post": len(list(filter(
                lambda p: p["userId"] == u["id"], posts
            ))),
        },
        users,
    ))

    # --- sorted() + lambda: peringkat user berdasarkan jumlah post ---
    peringkat = sorted(
        jumlah_post,
        key=lambda d: (-d["jumlah_post"], d["nama"]),
    )

    # --- filter() + map(): judul post milik user peringkat pertama ---
    id_teratas = peringkat[0]["id"]
    judul_teratas = list(map(
        lambda p: p["title"],
        filter(lambda p: p["userId"] == id_teratas, posts),
    ))

    hasil = {
        "total_user": len(users),
        "total_post": len(posts),
        "rata_rata_post_per_user": len(posts) / len(users),
        "daftar_nama_user": daftar_nama,
        "daftar_email_user": daftar_email,
        "user_email_biz": nama_user_biz,
        "peringkat_user_berdasarkan_jumlah_post": peringkat,
        "user_paling_produktif": peringkat[0]["nama"],
        "judul_post_user_paling_produktif": judul_teratas,
    }

    # --- Simpan hasil ke file JSON ---
    with open(FILE_HASIL, "w", encoding="utf-8") as f:
        json.dump(hasil, f, indent=2, ensure_ascii=False)

    # --- Tampilkan ringkasan ---
    print(f"\nTotal user : {hasil['total_user']}")
    print(f"Total post : {hasil['total_post']}")
    print(f"Rata-rata post per user: "
          f"{hasil['rata_rata_post_per_user']:.1f}")
    print(f"User dengan email .biz ({len(nama_user_biz)}): "
          f"{', '.join(nama_user_biz)}")
    print("\nPeringkat jumlah post per user:")
    for d in peringkat:
        print(f"  {d['nama']:<25} ({d['kota']:<15}) : "
              f"{d['jumlah_post']} post")
    print(f"\nUser paling produktif: {hasil['user_paling_produktif']}")
    print(f"Hasil lengkap disimpan ke: {FILE_HASIL}")


if __name__ == "__main__":
    main()
