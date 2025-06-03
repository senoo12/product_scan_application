from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import viewsets, permissions
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse
from .models import *
from .serializers import *
from rest_framework.response import Response

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

@method_decorator(csrf_exempt, name='dispatch')
class PasswordResetRequestView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print("Masuk ke passwordresetRequestView")
        serializer = PasswordResetRequestSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Email tidak ditemukan"}, status=status.HTTP_400_BAD_REQUEST)

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

        # URL verifikasi reset password
        reset_url = request.build_absolute_uri(
            reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
        )

        subject = "Permintaan Reset Password"
        message = f"Klik link ini untuk reset password Anda: {reset_url}"
        from_email = 'yourgmail@gmail.com'
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return Response({"message": "Link reset password sudah dikirim ke email Anda."})

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        serializer = SetNewPasswordSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error": "Token tidak valid"}, status=status.HTTP_400_BAD_REQUEST)

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            return Response({"error": "Token tidak valid atau sudah expired"}, status=status.HTTP_400_BAD_REQUEST)

        password = serializer.validated_data['password']
        user.set_password(password)
        user.save()

        return Response({"message": "Password berhasil direset."})

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
