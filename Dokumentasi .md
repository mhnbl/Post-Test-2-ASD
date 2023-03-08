# Post-Test-2-ASD

Nama  : Muhammad Nabil

NIM   : 2209116046

Program di atas merupakan implementasi dari algoritma Fibonacci Search yang digunakan untuk mencari elemen yang terdapat dalam sebuah array. Program tersebut menerima dua input, yaitu array 'var' dan nilai 'x' yang akan dicari pada array 'var'. Program akan mencari nilai 'x' pada 'var' menggunakan algoritma Fibonacci Search, dimana program akan memeriksa elemen-elemen pada array 'var' secara terurut dan mengambil elemen yang memiliki indeks yang merupakan deret bilangan Fibonacci.

 MENU UTAMA
 
 
![Screenshot 2023-03-08 201831](https://user-images.githubusercontent.com/125839542/223711705-0be94bd7-5e90-4f21-bbdd-30b9d5d9af9c.png)

Program ini dimulai dengan menyatakan Array dimana search akan dilakukan, yaitu array 'var' dan juga menanyakan kepada user apa yang ingin dcari dengan mengisi inputan variabel 'x'

![Screenshot 2023-03-08 202244](https://user-images.githubusercontent.com/125839542/223712395-2f4faf4f-400f-4739-afa2-e02dad30db06.png)

Lalu setelah variabel 'x' telah input, maka dilanjutkan ke program fibonacci search dengan array 'var' dan 'x' sebagai variabel yang digunakan. Setelah algoritma searching telah mengembalikan hasil pencarian, maka hasil tersebut akan ditampilkan apakah index telah ditemukan atau tidak.

![Screenshot 2023-03-08 211546](https://user-images.githubusercontent.com/125839542/223722869-7977ef99-4555-4a6d-bcc4-cddb75badf7f.png)

Setelah hasil ada tidaknya pencarian index diberikan, pengguna akan ditanya apakah sudah selesai menggunakan program atau ingin mengulang untuk mencari nama yang lain.

 ALGORITMA SEARCHING
 

![Screenshot 2023-03-08 202958](https://user-images.githubusercontent.com/125839542/223713805-79832d71-87f8-411b-bb76-54ff0cbff6e6.png)

Didalam fungsi Fibonacci Search ini diawali dengan menghitung panjang array menggunakan sintax n = len(var), lalu menyatakan angka-angka fibonacci. Setelah itu program mencari nilai dari fibonacci(n) yang terbesar yang lebih kecil atau sama dengan n, dan menyatakan index atau offset awal untuk pencarian.

![Screenshot 2023-03-08 203734](https://user-images.githubusercontent.com/125839542/223715251-e51fd40c-8194-4c5b-998e-ebac4aa224bd.png)

Lalu program mulai pencarian yang diawali dengan menghitung indeks berikutnya yang akan dicari (i). Fungsi isinstance() pada kode digunakan untuk mengecek apakah suatu objek merupakan sebuah list. Hal ini dilakukan karena pada bagian program utama, setiap elemen pada list arr dicek satu persatu untuk menentukan apakah elemen tersebut terdapat list didalam list, dan ika elemen ditemukan dalam list yang berada dalam list, index list tersebut ditambahakan.

![Screenshot 2023-03-08 204312](https://user-images.githubusercontent.com/125839542/223716325-02005a23-a3ce-4f9f-adf8-721a9937cefd.png)

Jika nilai elemen lebih kecil dari nilai yang dicari, maka lakukan pemindahan fibonnaci ke kanan.

![Screenshot 2023-03-08 204443](https://user-images.githubusercontent.com/125839542/223716587-606ea071-72b4-44be-8bef-6f490e92df49.png)

Jika nilai elemen lebih besar dari nilai yang dicari, maka lakukan pemindahan fibonnaci ke kiri.

![Screenshot 2023-03-08 204621](https://user-images.githubusercontent.com/125839542/223716904-8a4c27ea-ac14-4f8d-ac44-ab00941363ea.png)

Setelah dijalankannya semua pencarian pada fungsi ini, Jika elemen yang dicari ditemukan, kembalikan indeks elemen tersebut.


 OUTPUT PROGRAM
 

![Screenshot 2023-03-08 205325](https://user-images.githubusercontent.com/125839542/223718524-b3e3f074-1962-4fff-81f2-a18292dbf10d.png)

Saat program dijalankan, user diminta untuk memasukan nama aslab yang ingin dicari. Setelah itu user ditanya  apakah penggunaan program selesai atau tidak.

1) Arsel, Avivah, Daiva

![Screenshot 2023-03-08 205606](https://user-images.githubusercontent.com/125839542/223719102-1baa130d-3cf9-4d5f-91ca-ff702bffd0b5.png)

![Screenshot 2023-03-08 205632](https://user-images.githubusercontent.com/125839542/223719125-7f685dda-5fa8-4192-b86c-adc1b7a30693.png)

![Screenshot 2023-03-08 205657](https://user-images.githubusercontent.com/125839542/223719148-c17888df-e827-4799-8ab6-d0b9ceebbdae.png)

2) Wahyu

![Screenshot 2023-03-08 205824](https://user-images.githubusercontent.com/125839542/223719373-77a0c2eb-0c8d-40d7-97ec-60d29c28a4ae.png)

3) Wibi

![Screenshot 2023-03-08 205918](https://user-images.githubusercontent.com/125839542/223719478-1b1b8c8a-baf4-4d9c-8065-80756d6c2045.png)
