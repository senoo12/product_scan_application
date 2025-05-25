from django.contrib import admin
from api.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ProfileUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileUserAdmin)

class SeriAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Seri, SeriAdmin)

class MerkAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Merk, MerkAdmin)

class JenisBahanAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(JenisBahan, JenisBahanAdmin)

class BateraiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Baterai, BateraiAdmin)

class LayarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Layar, LayarAdmin)

class CasingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Casing, CasingAdmin)

class ProsesorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Prosesor, ProsesorAdmin)

class GPUAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(GPU, GPUAdmin)

class RAMAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(RAM, RAMAdmin)

class PenyimpananAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Penyimpanan, PenyimpananAdmin)

class KameraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Kamera, KameraAdmin)

class ChargerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Charger, ChargerAdmin)

class LaptopAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Laptop, LaptopAdmin)

class KomentarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Komentar, KomentarAdmin)