from .models import AksesKriteriaUser

def hak_akses_user(request):
    # Default awal: semua kriteria dikunci (False)
    hak_akses = {f'k{i}': False for i in range(1, 10)}
    
    # 🚨 LOG UTAMA DETEKTIF (Akan tercetak di terminal VS Code setiap kali refresh)
    print("\n🕵️‍♂️ === INSPEKSI UTAMA RBAC ===")
    print(f"1. Apakah User Sudah Terautentikasi (Login)?: {request.user.is_authenticated}")
    print(f"2. Username yang Terbaca oleh Django: '{request.user.username}'")
    print(f"3. Apakah User ini Statusnya Staff/Admin?: {request.user.is_staff}")
    
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            hak_akses = {f'k{i}': True for i in range(1, 10)}
            print("Status: User adalah STAFF. Semua kriteria otomatis dibuka (True).")
        else:
            try:
                akses = AksesKriteriaUser.objects.get(user=request.user)
                hak_akses = {
                    'k1': akses.akses_kriteria_1,
                    'k2': akses.akses_kriteria_2,
                    'k3': akses.akses_kriteria_3,
                    'k4': akses.akses_kriteria_4,
                    'k5': akses.akses_kriteria_5,
                    'k6': akses.akses_kriteria_6,
                    'k7': akses.akses_kriteria_7,
                    'k8': akses.akses_kriteria_8,
                    'k9': akses.akses_kriteria_9,
                }
                print(f"Status Database Kriteria 1 untuk {request.user.username}: {akses.akses_kriteria_1}")
            except AksesKriteriaUser.DoesNotExist:
                print(f"❌ PERINGATAN: Baris data untuk user '{request.user.username}' BELUM ADA di tabel AksesKriteriaUser!")
    else:
        print("❌ PERINGATAN: Django mendeteksi user ini BELUM LOGIN (AnonymousUser)!")
        
    print("=================================\n")
    return {'hak_akses': hak_akses}
