import pandas as pd

# 1. EXTRACT: Baca file raw data CSV
# Ganti nama file di bawah ini sesuai lokasi aslinya di komputermu
file_path = 'Rekapitulasi Hasil Penelitian DTPS MTI 2024.xlsx - Final Data S2.csv'

# Lewati 2 baris pertama karena itu adalah header judul "HASIL (LUARAN)..."
df_raw = pd.read_csv(file_path, skiprows=2)

# Hapus baris yang kosong atau tidak valid (misal baris pemisah)
df_raw = df_raw.dropna(subset=['Nama Dosen', 'Judul Penelitian'])

# 2. TRANSFORM: Ubah ke struktur tabel Borang LKPS (Tabel 3.C.2 Publikasi)
# Borang butuh: nama_dtpr, judul, jenis_pub, ts2, ts1, ts (Tahun Sekarang)
# Asumsi TS (Tahun Sekarang) = 2024, TS-1 = 2023, TS-2 = 2022

TAHUN_SEKARANG = 2024

df_transform = pd.DataFrame()
df_transform['nama_dtpr'] = df_raw['Nama Dosen']
df_transform['judul'] = df_raw['Judul Penelitian']
df_transform['jenis_pub'] = 'Jurnal Ilmiah / Prosiding' # Asumsi default dari keterangan

# Deteksi tahun publikasi (ubah ke boolean 1 atau 0 untuk TS, TS1, TS2)
df_transform['ts2'] = df_raw['Tahun'].apply(lambda x: 1 if str(x).strip() == str(TAHUN_SEKARANG - 2) else 0)
df_transform['ts1'] = df_raw['Tahun'].apply(lambda x: 1 if str(x).strip() == str(TAHUN_SEKARANG - 1) else 0)
df_transform['ts'] = df_raw['Tahun'].apply(lambda x: 1 if str(x).strip() == str(TAHUN_SEKARANG) else 0)

# Tambahan (Opsional) jika kamu mau menyimpannya ke tabel penelitian (3A2)
# df_transform['link_bukti'] = df_raw['Link']

# 3. LOAD: Simpan menjadi format Excel yang rapi siap Import
output_file = 'Data_Bersih_Tabel_Publikasi.xlsx'
df_transform.to_excel(output_file, index=False, sheet_name='Tabel_3C2_Publikasi')

print(f"✅ ETL Sukses! {len(df_transform)} baris data telah ditransformasi dan disimpan di {output_file}")