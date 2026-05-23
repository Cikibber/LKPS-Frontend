from django.apps import AppConfig
from django.db.models.signals import post_migrate


def buat_kriteria_default(sender, **kwargs):
    """
    Dipanggil otomatis setelah `python manage.py migrate` selesai.
    Mengecek KODE_FITUR_CHOICES dan membuat baris di database untuk
    setiap kriteria yang belum ada — tanpa menimpa data yang sudah ada.
    """
    from .models import PengaturanFitur
    for kode, nama in PengaturanFitur.KODE_FITUR_CHOICES:
        PengaturanFitur.objects.get_or_create(
            kode_fitur=kode,
            defaults={
                'nama_fitur': nama,
                'bisa_dilihat_user': True,
                'bisa_diedit_user': False,
                'tampilkan_pengaturan_ke_user': False,
            }
        )


class LkpsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lkps_app'

    def ready(self):
        # Hubungkan fungsi otomatisasi saat perintah migrate selesai dijalankan
        post_migrate.connect(buat_kriteria_default, sender=self)
