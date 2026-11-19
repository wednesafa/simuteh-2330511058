
# SIMUTEH – Computer Vision

## 1. Deskripsi Proyek

SIMUTEH merupakan proyek praktikum Computer Vision untuk mengolah citra daun teh berdasarkan kondisi visualnya. Proyek ini dikembangkan sebagai sistem bantu penyortiran daun teh ke dalam tiga kelas, yaitu Sehat, Bercak Ringan, dan Bercak Berat.

Pengembangan SIMUTEH dilakukan melalui beberapa tahapan pengolahan citra, mulai dari analisis warna, perbaikan kualitas citra, penapisan, deteksi tepi, hingga operasi morfologi dan analisis komponen terhubung.

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

Setiap citra memiliki ukuran 640 × 480 piksel dan dilengkapi label serta mask acuan untuk proses evaluasi.

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

SEED: `1058`

SEED ditentukan menggunakan empat digit terakhir NIM dan digunakan secara konsisten sesuai instruksi praktikum.

## 5. Struktur Proyek

```text
simuteh-2330511058/
├── data/
├── hasil/
│   ├── param_praproses.json
│   └── param_bercak.json
├── notebook/
│   ├── B1_lingkungan.ipynb
│   ├── B2_citra_warna.ipynb
│   ├── B3_histogram.ipynb
│   ├── B4_penapisan.ipynb
│   ├── P5_tepi.ipynb
│   └── P6_morfologi.ipynb
├── src/
│   ├── praproses.py
│   ├── utils_tepi.py
│   └── bercak.py
├── requirements.txt
└── README.md
```

## 6. Ringkasan Hasil Praktikum P1–P4

Berdasarkan pengujian sebelumnya:
1. Kanal R menghasilkan nilai KB tertinggi secara konsisten pada pengujian kelas bercak berat di berbagai kondisi cahaya.
2. CLAHE menghasilkan KB 2,09, lebih tinggi dibandingkan ekualisasi global sebesar 1,15 pada citra `teh_045.png`.
3. Median filter efektif mengurangi derau garam dan merica, tetapi kernel yang terlalu besar dapat menghilangkan detail bercak kecil.
4. Praproses meningkatkan KB pada empat dari lima kondisi pencahayaan. Pada kondisi terang, KB turun dari 7,15 menjadi 6,45.

Parameter praproses disimpan dalam `hasil/param_praproses.json`.

## 7. Ringkasan Hasil Praktikum P5–P6

### P5 – Deteksi Tepi

Pada pertemuan 5 dilakukan pengujian deteksi tepi untuk mengetahui kemampuan metode dalam menemukan batas daun dan bercak.

Metode yang diuji meliputi:
- Sobel
- Prewitt
- Laplacian of Gaussian (LoG)
- Canny

Pengujian dilakukan dengan membandingkan hasil deteksi tepi terhadap tepi acuan menggunakan presisi, recall, dan F1. Evaluasi juga memperhatikan pengaruh kanal warna, kondisi pencahayaan, serta parameter deteksi tepi.

Hasil utama pengujian:
- Operator terbaik: [isi sesuai hasil pengujian]
- Kanal terbaik: [isi sesuai hasil pengujian]
- Nilai F1 terbaik: [isi nilai F1]
- Keputusan penggunaan deteksi tepi: [isi keputusan dan alasannya]

### P6 – Operasi Morfologi dan Analisis Komponen Terhubung

Pada pertemuan 6 dilakukan pengolahan citra biner bercak menggunakan operasi morfologi. Tahapan ini bertujuan membersihkan titik derau, menghilangkan bagian yang tidak diperlukan, serta memperbaiki bentuk area bercak.

Operasi yang digunakan meliputi:
- Erosi dan dilasi.
- Opening untuk mengurangi titik derau dan komponen kecil.
- Closing untuk menutup celah pada area bercak.
- Analisis komponen terhubung dengan konektivitas 8.
- Pengukuran luas, keliling, kebulatan, dan rasio aspek setiap komponen.

Komponen bercak disaring berdasarkan luas minimum, kebulatan minimum, dan rasio aspek maksimum.

Hasil utama pengujian:
- Bentuk structuring element: [isi hasil]
- Ukuran SE opening: [isi hasil]
- Ukuran SE closing: [isi hasil]
- Jumlah bercak hasil analisis: [isi hasil evaluasi]
- Galat absolut rerata persen bercak: [isi hasil]
- Akurasi kelas: [isi hasil]
- Kondisi cahaya dengan akurasi terendah: [isi hasil]

### Modul Analisis Bercak

Hasil P5–P6 diintegrasikan ke dalam modul `src/bercak.py`. Modul ini menerima citra BGR yang sudah melalui praproses dan menghasilkan:
- Mask daun.
- Mask bercak yang sudah dibersihkan dan disaring.
- Jumlah bercak.
- Persentase luas bercak.
- Prediksi kelas mutu daun.
- Informasi ukuran setiap komponen bercak.

Parameter analisis disimpan dalam `hasil/param_bercak.json`.

## 8. Cara Menggunakan Modul analisis_daun

Modul analisis bercak dapat digunakan kembali tanpa harus menjalankan seluruh tahapan pengujian secara manual.

Pastikan file berikut tersedia:
- `src/bercak.py`
- `src/praproses.py`
- `src/utils_tepi.py`
- `hasil/param_praproses.json`
- `hasil/param_bercak.json`

Contoh penggunaan di Python atau Google Colab:

```python
import sys
import json
import cv2

sys.path.append("src")

from bercak import analisis_daun

# Muat parameter praproses
with open("hasil/param_praproses.json", "r") as f:
    PARAM = json.load(f)

# Muat parameter analisis bercak
with open("hasil/param_bercak.json", "r") as f:
    PB = json.load(f)

# Baca citra daun teh
img = cv2.imread("data/teh_001.png")

# Lakukan praproses
from praproses import praproses
img_proses = praproses(img, PARAM)

# Analisis bercak
hasil = analisis_daun(img_proses, PB)

# Tampilkan hasil
print("Jumlah bercak:", hasil["jumlah_bercak"])
print("Persen bercak:", hasil["persen_bercak"], "%")
print("Kelas daun:", hasil["kelas"])
```

Fungsi `analisis_daun(img_praproses, p=None)` menerima:
- `img_praproses`: citra daun teh dalam format BGR yang sudah melalui praproses.
- `p`: parameter analisis bercak. Jika tidak diberikan, fungsi menggunakan parameter bawaan.

Hasil fungsi berupa dictionary yang berisi `mask_daun`, `mask_bercak`, `jumlah_bercak`, `persen_bercak`, `kelas`, dan `bercak`.

## 9. Parameter Praproses dan Analisis Bercak

Parameter praproses disimpan pada `hasil/param_praproses.json`, sedangkan parameter analisis bercak disimpan pada `hasil/param_bercak.json`.

Parameter analisis bercak meliputi:
- `kanal`: kanal warna yang digunakan untuk mendeteksi bercak.
- `k`: pengali MAD untuk menentukan ambang bercak.
- `se_bentuk`: bentuk structuring element.
- `se_open`: ukuran kernel opening.
- `se_close`: ukuran kernel closing.
- `luas_min`: luas minimum komponen bercak.
- `bulat_min`: nilai kebulatan minimum.
- `rasio_maks`: rasio aspek maksimum.
- `batas_ringan`: batas minimum persentase bercak untuk kelas Bercak Ringan.
- `batas_berat`: batas minimum persentase bercak untuk kelas Bercak Berat.
- `mm_per_px`: skala ukuran piksel ke milimeter.

Nilai parameter final mengikuti hasil eksperimen dan disimpan dalam file JSON agar pengujian dapat diulang.

## 10. Cara Menjalankan Proyek

1. Clone repository:

```bash
git clone https://github.com/wednesafa/simuteh-2330511058.git
```

2. Buka Google Colab.
3. Upload atau buka repository yang sudah diunduh.
4. Pastikan dataset dan seluruh folder proyek berada pada direktori yang benar.
5. Instal library menggunakan `requirements.txt`.
6. Jalankan notebook secara berurutan:
   - `B1_lingkungan.ipynb`
   - `B2_citra_warna.ipynb`
   - `B3_histogram.ipynb`
   - `B4_penapisan.ipynb`
   - `P5_tepi.ipynb`
   - `P6_morfologi.ipynb`

7. Pastikan seluruh notebook berhasil dijalankan menggunakan Restart & Run All.

## 11. Pengembangan Selanjutnya

Pengembangan SIMUTEH akan dilanjutkan pada pertemuan 7 dengan tahap segmentasi citra. Tahap tersebut bertujuan memperbaiki pembentukan mask daun dan mask bercak agar hasil pengukuran luas serta persentase bercak menjadi lebih baik.

Metode yang direncanakan meliputi ambang global dan adaptif, Otsu, region growing, watershed, serta segmentasi berbasis klaster.
