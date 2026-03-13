# Wahyu Prataama
# 09021282429084


# Best First Search
# Mencari rute terpendek dari A ke H

graph = {
    'A': [('B', 20), ('D', 80), ('G', 90)],
    'B': [('F', 10)],
    'F': [('C', 10), ('D', 40)],
    'C': [('D', 10), ('F', 50), ('H', 20)],
    'D': [('C', 10), ('G', 20)],
    'E': [('B', 50), ('G', 30)],
    'G': [('A', 20)],
    'H': [],
}
# Graph merepresentasikan peta node beserta bobotnya.
# Karena graf bersifat directed (1 arah), tidak semua node saling terhubung balik. Hanya dari node D ke C yang timbal balik.
# Format setiap edge: (nama_node_tujuan, bobot)

heuristik = {
    'A': 60,
    'B': 80,
    'C': 20,
    'D': 25,
    'E': 70,
    'F': 25,
    'G': 35,
    'H': 0,
}
# Heuristik berisi estimasi waktu (menit) dari setiap node menuju goal (H).
# Semakin kecil nilainya, semakin dekat estimasinya ke goal.
# H = 0 karena H adalah goal itu sendiri.

def ambil_minimum(antrian):
    # Mencari index elemen dengan nilai heuristik terkecil secara manual
    index_min = 0
    for i in range(1, len(antrian)):
        if antrian[i][0] < antrian[index_min][0]:
            index_min = i
    return antrian.pop(index_min)

def best_first_search(graph, heuristik, awal, tujuan):
    print(f"~ Best First Search: Mencari rute dari {awal} ke {tujuan}\n")

    # Antrian menyimpan (nilai_heuristik, node, path)
    # Node dengan heuristik terkecil yang akan diproses duluan
    antrian = [(heuristik[awal], awal, [awal])]
    sudah_dikunjungi = []
    langkah = 1

    while len(antrian) > 0:
        # Ambil node dengan nilai heuristik terkecil dari antrian
        h_nilai, node_sekarang, path_sekarang = ambil_minimum(antrian)

        if node_sekarang in sudah_dikunjungi:
            continue

        sudah_dikunjungi.append(node_sekarang)

        print(f"Langkah {langkah}: Mengunjungi {node_sekarang} (h={h_nilai}) ~~~ Path: {' -> '.join(path_sekarang)}")
        langkah += 1

        # Jika node sekarang adalah tujuan, hitung total jarak lalu berhenti
        if node_sekarang == tujuan:
            print(f"\nGoal ditemukan")
            print(f"Rute: {' -> '.join(path_sekarang)}")

            # Menghitung total jarak dengan mengiterasi setiap pasangan node pada path
            total_jarak = 0
            for i in range(len(path_sekarang) - 1):
                node_a = path_sekarang[i]
                node_b = path_sekarang[i + 1]
                for tetangga, bobot in graph[node_a]:
                    if tetangga == node_b:
                        total_jarak += bobot
                        break
            print(f"Total jarak: {total_jarak}")
            return path_sekarang

        # Ekspansi tetangga, masukkan ke antrian berdasarkan nilai heuristiknya
        info_tetangga = []
        for tetangga, bobot in graph[node_sekarang]:
            if tetangga not in sudah_dikunjungi:
                info_tetangga.append(f"{tetangga}(h={heuristik[tetangga]})")
                path_baru = path_sekarang + [tetangga]
                antrian.append((heuristik[tetangga], tetangga, path_baru))

        if len(info_tetangga) > 0:
            print(f"  Tetangga {node_sekarang}: {', '.join(info_tetangga)}")
        else:
            print(f"  Tetangga {node_sekarang}: tidak ada tetangga baru")

    print("Rute tidak ditemukan.")
    return None

best_first_search(graph, heuristik, 'A', 'H')