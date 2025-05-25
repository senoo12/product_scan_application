from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    http_method_names = ['post']

class ChangePasswordView(APIView):
    serializer_class = ChangePasswordSerializers
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializers(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Password lama salah."]}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()

            return Response({"detail": "Password berhasil diganti."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this profile.")
        serializer.save()

class MerkViewSet(viewsets.ModelViewSet):
    queryset = Merk.objects.all()
    serializer_class = MerkSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class SeriViewSet(viewsets.ModelViewSet):
    queryset = Seri.objects.all()
    serializer_class = SeriSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class JenisBahanViewSet(viewsets.ModelViewSet):
    queryset = JenisBahan.objects.all()
    serializer_class = JenisBahanSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class BateraiViewSet(viewsets.ModelViewSet):
    queryset = Baterai.objects.all()
    serializer_class = BateraiSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class LayarViewSet(viewsets.ModelViewSet):
    queryset = Layar.objects.all()
    serializer_class = LayarSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class CasingViewSet(viewsets.ModelViewSet):
    queryset = Casing.objects.all()
    serializer_class = CasingSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class ProsesorViewSet(viewsets.ModelViewSet):
    queryset = Prosesor.objects.all()
    serializer_class = ProsesorSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class GPUViewSet(viewsets.ModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class RAMViewSet(viewsets.ModelViewSet):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class PenyimpananViewSet(viewsets.ModelViewSet):
    queryset = Penyimpanan.objects.all()
    serializer_class = PenyimpananSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class KameraViewSet(viewsets.ModelViewSet):
    queryset = Kamera.objects.all()
    serializer_class = KameraSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class ChargerViewSet(viewsets.ModelViewSet):
    queryset = Charger.objects.all()
    serializer_class = ChargerSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

class KomentarViewSet(viewsets.ModelViewSet):
    queryset = Komentar.objects.all()
    serializer_class = KomentarSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
