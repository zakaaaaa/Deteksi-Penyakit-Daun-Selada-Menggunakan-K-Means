Deeteksi Penyakit pada Daun Selada Menggunakan Algoritma K-Means

Deskripsi Proyek:
Project ini merupakan tugas mata kuliah Artificial Intelligence (AI) pada semester 4 yang berfokus pada penerapan unsupervised learning untuk mendeteksi penyakit pada daun selada (lettuce leaf disease detection).
Melalui metode K-Means Clustering, sistem ini mencoba mengelompokkan piksel citra daun berdasarkan kemiripan warna sehingga area yang terinfeksi penyakit dapat teridentifikasi secara visual tanpa memerlukan data label (unsupervised approach).

Konsep dan Tujuan:
Pendekatan ini bertujuan untuk:
Menggunakan machine learning berbasis clustering untuk analisis citra daun selada.
Melakukan segmentasi warna piksel (RGB) untuk membedakan area daun yang sehat dan yang menunjukkan gejala penyakit seperti bercak atau busuk.
Memberikan gambaran awal tentang bagaimana AI dapat membantu bidang pertanian melalui image-based analysis.

Cara Kerja
Input: Gambar daun selada dalam format RGB.
Preprocessing: Gambar diubah menjadi array numerik menggunakan NumPy.
Clustering: Algoritma K-Means membagi piksel ke dalam k kelompok berdasarkan kemiripan warna.
Output:
Gambar hasil segmentasi (clustered image)
Label klaster untuk setiap piksel (mask matrix)
Interpretasi:
Klaster dengan warna tertentu mengindikasikan area berbeda pada daun — misalnya, warna lebih gelap atau kekuningan dapat menandakan infeksi penyakit.
