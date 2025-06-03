from django.contrib.auth.models import Group, User
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class RegisterSerializers(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class ChangePasswordSerializers(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
class PasswordResetRequestSerializers(serializers.Serializer):
    email = serializers.EmailField()

class SetNewPasswordSerializers(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=128)
    token = serializers.CharField()
    uidb64 = serializers.CharField()

class ProfileSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']


class MerkSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merk
        fields = '__all__'

class SeriSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seri
        fields = ['judul_seri', 'nama_seri', 'tahun_seri', 'merk']

class JenisBahanSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JenisBahan
        fields = '__all__'

class BateraiSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Baterai
        fields = '__all__'

class LayarSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layar
        fields = '__all__'

class CasingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Casing
        fields = '__all__'

class ProsesorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prosesor
        fields = '__all__'

class GPUSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'

class RAMSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RAM
        fields = '__all__'

class PenyimpananSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Penyimpanan
        fields = '__all__'

class KameraSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kamera
        fields = '__all__'

class ChargerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charger
        fields = '__all__'

class LaptopSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'

class KomentarSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Komentar
        fields = '__all__'