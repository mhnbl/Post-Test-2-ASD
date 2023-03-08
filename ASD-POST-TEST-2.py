import os
os.system('cls')

def fibonacci_search(var, x):
    n = len(var )
    
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    
    offset = -1
    
    while fib > 1:
        i = min(offset+fib2, n-1)
        
        if isinstance(var [i], list):
            result = fibonacci_search(var [i], x)
            if result != -1:
                return [i] + result
        
        if var [i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif var [i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return [i]
        
    if fib1 and var [offset+1] == x:
        return [offset+1]
    return [-1]


def Start():
    var  = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
    x = input("\nNama Aslab: ")

    hasil = fibonacci_search(var , x)
    
    if hasil == -1:
        print(f"{x} Tidak Ditemukan di Dalam List")
    else:
        print(f"{x} Ditemukan Pada Index Ke-{hasil}")

    f = input("\nSelesai [y/t]?: ").lower()
    while f not in ["y","t"]:
        print("Mohon masukan pilihan yang tersedia")
        f = input("Selesai [y/t]?: ").lower()
    if f == "y":
        print("TERIMA KASIH")
        exit()
    elif f == "t":
        Start()
        
Start()