# Wahyu Prataama
# 09021282429084


# Depth First Search.
# Mencari rute dari Milan ke Innsbruck.

graph = {
    'Milan':      [('Como', 45), ('Lecco', 50), ('Bergamo', 55), ('Piacenza', 60)],
    'Como':       [('Milan', 45), ('Lugano', 20), ('Lecco', 25)],
    'Lugano':     [('Como', 20), ('Feldkirck', 180), ('Chiavenna', 40)],
    'Lecco':      [('Milan', 50), ('Sondrio', 42), ('Como', 25), ('Chiavenna', 60)],
    'Bergamo':    [('Milan', 55), ('Brescia', 45)],
    'Brescia':    [('Piacenza', 70), ('Verona', 60), ('Bergamo', 45), ('Trento', 90)],
    'Piacenza':   [('Milan', 60), ('Brescia', 70)],
    'Verona':     [('Brescia', 60), ('Trento', 80)],
    'Chiavenna':  [('Lecco', 60), ('Lugano', 40), ('Landeck', 140)],
    'Sondrio':    [('Lecco', 42), ('Merano', 135)],
    'Trento':     [('Brescia', 90), ('Verona', 80), ('Bolzano', 55)],
    'Bolzano':    [('Trento', 55), ('Merano', 25), ('Innsbruck', 90)],
    'Merano':     [('Bolzano', 25), ('Sondrio', 135), ('Landeck', 100)],
    'Landeck':    [('Merano', 100), ('Feldkirck', 70), ('Innsbruck', 63), ('Chiavenna', 140)],
    'Feldkirck':  [('Landeck', 70), ('Lugano', 180)],
    'Innsbruck':  [('Landeck', 63), ('Bolzano', 90)],
}
# Graph merepresentasikan peta kota beserta jarak antar kotanya.
# Setiap kota menyimpan daftar tetangga langsungnya dalam format (nama_kota, jarak).
# Karena graf bersifat undirected (2 arah), jika kota A terhubung ke B.

# Urutan graph mempengaruhi hasil karena DFS selalu mengeksplorasi tetangga pertama.

# Variabel langkah_ke dibuat sebagai list agar nilainya bisa diubah.
# di dalam fungsi rekursif (kalau pakai int biasa tidak bisa diubah dari dalam fungsi).
langkah_ke = [1]

def depth_first_search(graph, node_sekarang, tujuan, sudah_dikunjungi, path_sekarang):
    # Tandai node sekarang sebagai sudah dikunjungi dan tambahkan ke path.
    sudah_dikunjungi.append(node_sekarang)
    path_sekarang.append(node_sekarang)

    print(f"Langkah {langkah_ke[0]}: Mengunjungi {node_sekarang} ~~~ Path: {' -> '.join(path_sekarang)}")
    langkah_ke[0] += 1

    # Jika node sekarang adalah tujuan, langsung return True untuk berhenti.
    if node_sekarang == tujuan:
        return True

    # Ekspansi tetangga satu per satu secara rekursif
    # DFS langsung masuk sedalam mungkin ke tetangga pertama.
    # sebelum mencoba tetangga berikutnya.
    for tetangga, jarak in graph[node_sekarang]:
        if tetangga not in sudah_dikunjungi:
            ketemu = depth_first_search(graph, tetangga, tujuan, sudah_dikunjungi, path_sekarang)
            if ketemu:
                return True

    # Backtrack: jika semua tetangga sudah dicoba dan goal tidak ditemukan, hapus node sekarang dari path dan kembali ke node sebelumnya.
    path_sekarang.pop()
    return False

def jalankan_dfs(awal, tujuan):
    print(f"~ DFS: Mencari rute dari {awal} ke {tujuan}\n")

    sudah_dikunjungi = []
    path_sekarang = []

    ketemu = depth_first_search(graph, awal, tujuan, sudah_dikunjungi, path_sekarang)

    if ketemu:
        print(f"\nGoal ditemukan")
        print(f"Rute: {' -> '.join(path_sekarang)}")

        # Menghitung total jarak dengan mengiterasi setiap pasangan kota pada path
        total_jarak = 0
        for i in range(len(path_sekarang) - 1):
            kota_a = path_sekarang[i]
            kota_b = path_sekarang[i + 1]
            for tetangga, jarak in graph[kota_a]:
                if tetangga == kota_b:
                    total_jarak += jarak
                    break
        print(f"Total jarak: {total_jarak} km")
    else:
        print("Rute tidak ditemukan.")

jalankan_dfs('Milan', 'Innsbruck')