import pandas as pd

# Load data mentah
df_raw = pd.read_csv('Rekapitulasi Hasil Penelitian DTPS MTI 2024.xlsx - Final Data S2.csv', skiprows=2)

# Bersihkan baris kosong
df_raw = df_raw.dropna(subset=['Nama Dosen', 'Judul Penelitian'])

# Transformasi ke format Tabel_3C2_Publikasi
TAHUN_SKRG = 2024
df_final = pd.DataFrame()
df_final['nama_dtpr'] = df_raw['Nama Dosen']
df_final['judul'] = df_raw['Judul Penelitian']
df_final['jenis_pub'] = 'Jurnal Ilmiah'

# Konversi tahun ke TS (Tahun Sekarang)
df_final['ts2'] = df_raw['Tahun'].apply(lambda x: 1 if str(x) == str(TAHUN_SKRG-2) else 0)
df_final['ts1'] = df_raw['Tahun'].apply(lambda x: 1 if str(x) == str(TAHUN_SKRG-1) else 0)
df_final['ts'] = df_raw['Tahun'].apply(lambda x: 1 if str(x) == str(TAHUN_SKRG) else 0)

# Simpan hasil untuk di-copy ke Master Template
df_final.to_excel('siap_copy_ke_tabel_3c2.xlsx', index=False)
print("Transformasi Selesai! Buka file 'siap_copy_ke_tabel_3c2.xlsx'")