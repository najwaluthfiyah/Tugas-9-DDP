#3. buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang dimasukkan

def bilangan_ganjil(angka):
    for i in range(angka):
        if i % 2 != 0 :
            print(i)

bilangan_ganjil(100)