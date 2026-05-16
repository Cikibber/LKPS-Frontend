import pandas as pd

# Data Visi Misi lengkap yang sudah dirapikan
data = {
    'visi_pt': ['Menjadi perguruan tinggi yang berfokus pada industri dengan mengintegrasikan keilmuan dan aplikasi dalam pembelajaran untuk menghasilkan lulusan yang kompeten dan berintegritas.'],
    'misi_pt': ['1. Menyelenggarakan pendidikan tinggi yang relevan dengan kebutuhan industri.\n2. Melaksanakan penelitian yang berkontribusi pada pengembangan IPTEK.\n3. Melaksanakan pengabdian masyarakat yang berdampak positif.'],
    'visi_upps': ['Menjadi Fakultas Sains dan Teknologi yang unggul dalam pengembangan sains dan teknologi yang terintegrasi dengan industri untuk kesejahteraan masyarakat pada tahun 2045.'],
    'misi_upps': ['Menyelenggarakan pendidikan, penelitian, dan pengabdian masyarakat di bidang sains dan teknologi yang inovatif dan relevan dengan tantangan global.'],
    'visi_ps': ['Menjadi Program Studi Magister Teknologi Informasi yang unggul dalam pengembangan teknologi informasi di Indonesia dengan fokus pada Smart City, Smart Community, dan Smart Technology pada tahun 2045.'],
    'misi_ps': ['1. Menyelenggarakan pendidikan Magister TI yang inovatif.\n2. Melaksanakan penelitian bertaraf nasional dan internasional di bidang Smart Technology.\n3. Melaksanakan pengabdian masyarakat berbasis teknologi informasi.'],
    'tujuan_ps': ['Menghasilkan lulusan Magister Teknologi Informasi yang mampu memecahkan masalah kompleks di industri dan masyarakat melalui inovasi teknologi informasi.'],
    'sasaran_ps': ['1. Pengembangan kurikulum Industri 4.0.\n2. Peningkatan penelitian dosen dan mahasiswa.\n3. Penguatan jaringan kerjasama.\n4. Tata kelola yang transparan dan akuntabel.\n5. Pembentukan pusat studi unggulan.']
}

# URUTAN WAJIB SESUAI DENGAN VIEWS.PY (Jangan diubah)
urutan_kolom = ['visi_pt', 'misi_pt', 'visi_upps', 'misi_upps', 'visi_ps', 'misi_ps', 'tujuan_ps', 'sasaran_ps']

# Buat Dataframe
df = pd.DataFrame(data, columns=urutan_kolom)

# Export ke Excel
nama_file = 'Perbaikan_Tabel_6.xlsx'
df.to_excel(nama_file, sheet_name='Tabel_6_VisiMisi', index=False)

print(f"✅ Berhasil! File '{nama_file}' sudah jadi dan siap di-upload ke Dashboard.")