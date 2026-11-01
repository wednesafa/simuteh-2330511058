
# SIMUTEH – Computer Vision

## 1. Deskripsi Proyek

SIMUTEH merupakan proyek praktikum Computer Vision untuk mengolah citra daun teh berdasarkan kondisi visualnya. Proyek ini menjadi dasar pengembangan sistem penyortiran daun teh ke dalam tiga kelas, yaitu Sehat, Bercak Ringan, dan Bercak Berat.

## 2. Dataset

Dataset yang digunakan merupakan dataset sintetis dengan total 60 citra:
- 20 citra kelas Sehat
- 20 citra kelas Bercak Ringan
- 20 citra kelas Bercak Berat

Dataset memiliki lima kondisi pencahayaan:
- Normal
- Gelap
- Terang
- Kontras Rendah
- Bayangan

## 3. Teknologi dan Library

- Python
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Google Colab

Instalasi library:

```bash
pip install -r requirements.txt
```

## 4. SEED yang Digunakan

SEED: [1058]
SEED ditentukan pada notebook B1 menggunakan 4 digit terakhir NIM. 
Nilai SEED tersebut digunakan sesuai instruksi praktikum pada tahap B1.

## 5. Cara Menjalankan Proyek

1. Buka repository SIMUTEH di GitHub.
2. Unduh repository atau lakukan clone:

```bash
git clone https://github.com/wednesafa/simuteh-2330511058.git
```

3. Buka Google Colab.
4. Upload atau buka notebook dari folder `notebook`.
5. Hubungkan Google Drive jika dataset disimpan di Google Drive.
6. Pastikan direktori kerja mengarah ke folder utama proyek.
7. Jalankan notebook secara berurutan:
   - B1_lingkungan.ipynb
   - B2_citra_warna.ipynb
   - B3_histogram.ipynb
   - B4_penapisan.ipynb
   - B5_praproses.ipynb

## 6. Ringkasan Hasil Praktikum

Berdasarkan hasil pengujian:

1. **Analisis warna:** Kanal R menghasilkan nilai KB tertinggi secara konsisten pada pengujian kelas bercak berat di berbagai kondisi cahaya.
2. **Histogram:** CLAHE menghasilkan KB 2,09, lebih tinggi dibandingkan ekualisasi global sebesar 1,15 pada citra `teh_045.png`.
3. **Penapisan:** Median filter efektif mengurangi derau garam dan merica. Kernel terlalu besar dapat menghilangkan detail bercak kecil.
4. **Praproses:** KB meningkat pada empat dari lima kondisi pencahayaan. Pada kondisi terang, KB turun dari 7,15 menjadi 6,45.

Parameter praproses final disimpan dalam `hasil/param_praproses.json`.

## 7. Parameter Praproses

| Parameter | Nilai |
|---|---|
| Lebar citra | 640 |
| Gamma | 1.0 |
| CLAHE Clip Limit | 2.0 |
| CLAHE Tile | 8 × 8 |
| Penapis | Median |
| Kernel | 3 × 3 |
| Sigma | 1.0 |
| Sharpen | 0.0 (nonaktif) |

## 8. Pengembangan Selanjutnya

Pengujian selanjutnya direncanakan menggunakan deteksi tepi untuk mengetahui apakah informasi tepi dapat membantu menemukan batas daun dan bercak.

