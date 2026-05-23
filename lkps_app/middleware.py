from django.shortcuts import render
from .models import AksesKriteriaUser

class KriteriaAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Jika user belum login, atau merupakan staff/superuser, langsung loloskan
        if not request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
            return self.get_response(request)

        path = request.path.lower()

        # 2. Peta Deteksi: Tentukan nomor kriteria berdasarkan kata kunci unik di URL
        nomor_kriteria = None

        # Cek pola berbasis teks kriteria eksplisit (/kriteria-X/...)
        if 'kriteria-1/' in path:
            nomor_kriteria = 1
        elif 'kriteria-2/' in path:
            nomor_kriteria = 2
        elif 'kriteria-3/' in path:
            nomor_kriteria = 3
        elif 'kriteria-4/' in path:
            nomor_kriteria = 4
        elif 'kriteria-5/' in path:
            nomor_kriteria = 5
        elif 'kriteria-6/' in path:
            nomor_kriteria = 6
        
        # Cek pola berbasis dynamic routing (/tabel/kode_tabel/)
        elif '/tabel/' in path:
            if '1a1' in path or '1b' in path:
                nomor_kriteria = 1
            elif any(x in path for x in ['2b1', '2b2', '2b3', '2c', '2d']):
                nomor_kriteria = 2
            elif '3a3' in path:
                nomor_kriteria = 3

        # 3. Jalankan Proteksi jika URL yang dibuka terdeteksi sebagai halaman kriteria
        if nomor_kriteria:
            field_name = f'akses_kriteria_{nomor_kriteria}'
            try:
                # Ambil record hak akses user
                akses = AksesKriteriaUser.objects.get(user=request.user)
                boleh_akses = getattr(akses, field_name, False)
                
                # Jika status di matriks admin aplikasi adalah uncheck (False), BLOKIR SEGERA!
                if not boleh_akses:
                    return render(request, 'lkps_app/akses_ditolak.html', status=403)
                    
            except AksesKriteriaUser.DoesNotExist:
                # Demi keamanan, jika data belum di-set, default ditolak
                return render(request, 'lkps_app/akses_ditolak.html', status=403)

        return self.get_response(request)
