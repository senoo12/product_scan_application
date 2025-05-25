from django.contrib import admin
from rest_framework import routers
from api import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'register', views.RegisterViewSet)
router.register(r'profile', views.ProfileViewSet, basename='profile')
router.register(r'merk', views.MerkViewSet)
router.register(r'seri', views.SeriViewSet)
router.register(r'jenisbahan', views.JenisBahanViewSet)
router.register(r'baterai', views.BateraiViewSet)
router.register(r'layar', views.LayarViewSet)
router.register(r'casing', views.CasingViewSet)
router.register(r'prosesor', views.ProsesorViewSet)
router.register(r'gpu', views.GPUViewSet)
router.register(r'ram', views.RAMViewSet)
router.register(r'penyimpanan', views.PenyimpananViewSet)
router.register(r'kamera', views.KameraViewSet)
router.register(r'charger', views.ChargerViewSet)
router.register(r'laptop', views.LaptopViewSet)
router.register(r'komentar', views.KomentarViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
     path('api-auth/', include([
        path('', include('rest_framework.urls', namespace='rest_framework')), 
        path('change-password/', views.ChangePasswordView.as_view(), name='change-password'), 
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
