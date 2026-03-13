# Wahyu Prataama
# 09021282429084


# Breadth First Search.
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
# Karena graf bersifat undirected (2 arah), jika kota A terhubung ke B

# Urutan graph tidak mempengaruhi rute yang ditemukan,
# karena BFS selalu menemukan path dengan jumlah hop paling sedikit

def breadth_first_search(graph, awal, tujuan):
    print(f"~ BFS: Mencari rute dari {awal} ke {tujuan}\n")
 
    antrian = [[awal]]  # Antrian menyimpan path lengkap dari awal hingga node saat ini.
    sudah_dikunjungi = [awal] # Daftar node yang sudah dikunjungi agar tidak terjadi perulangan.
    langkah = 1
 
    while len(antrian) > 0:
        path_sekarang = antrian.pop(0) # Mengambil path pertama dari antrian (FIFO).
        node_sekarang = path_sekarang[-1] # Mengambil node terakhir dari path saat ini.
 
        print(f"Langkah {langkah}: Mengunjungi {node_sekarang} ~~~ Path: {' -> '.join(path_sekarang)}")
        langkah += 1
 
        if node_sekarang == tujuan:
            print(f"\nGoal ditemukan")
            print(f"Rute: {' -> '.join(path_sekarang)}")

            # Menghitung total jarak dengan mengiterasi setiap pasangan kota.
            total_jarak = 0
            for i in range(len(path_sekarang) - 1):
                kota_a = path_sekarang[i]
                kota_b = path_sekarang[i + 1]
                for tetangga, jarak in graph[kota_a]: # Mencari jarak kota_a ke kota_b pada daftar tetangga di graph.
                    if tetangga == kota_b:
                        total_jarak += jarak
                        break
            print(f"Total jarak: {total_jarak} km")
            return path_sekarang
        
        # Mencari tetangga yang belum dikunjungi dan menambahkan ke antrian.
        for tetangga, jarak in graph[node_sekarang]:
            if tetangga not in sudah_dikunjungi:
                sudah_dikunjungi.append(tetangga)
                path_baru = path_sekarang + [tetangga] # Membuat path baru dengan menambahkan tetangga ke path saat ini.
                antrian.append(path_baru)
 
    print("Rute tidak ditemukan.")
    return None
 
breadth_first_search(graph, 'Milan', 'Innsbruck')