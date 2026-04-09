import pytest
from django.contrib.auth.models import User
from users.serializers import UserSerializer

@pytest.mark.django_db
class TestUserLogicFelipe:

    # TESTE DE SEGURANÇA (verificando se a senha é write-only)
    def test_serializer_password_is_write_only_explicit(self):
        user = User.objects.create_user(username="felipe_test", password="safe_password123")
        serializer = UserSerializer(instance=user)
        assert 'password' not in serializer.data, "A senha vazou no JSON de saída!"

    #TESTE DE INTEGRIDADE DE DADOS
    def test_serializer_fails_without_username(self):
        data = {"email": "felipe@dev.com", "password": "123"}
        serializer = UserSerializer(data=data)
        assert not serializer.is_valid()
        assert 'username' in serializer.errors

    # TESTE UPDATE NOME
    def test_serializer_update_preserves_unmodified_fields(self):
        user = User.objects.create_user(username="felipe_santos", first_name="Original")
        data = {"username": "felipe_souza"}
        serializer = UserSerializer(user, data=data, partial=True)
        assert serializer.is_valid()
        updated_user = serializer.save()
        assert updated_user.username == "felipe_souza"
        assert updated_user.first_name == "Original" 

    # TESTE CRIPTOGRAFIA METHOD CREATED  
    def test_serializer_hashes_password_on_creation(self):
        data = {
            "username": "crypto_user",
            "password": "batman_123",
            "email": "crypto@test.com"
        }
        serializer = UserSerializer(data=data)
        assert serializer.is_valid()
        user = serializer.save()
        assert user.password != "batman_123"
        assert user.check_password("batman_123")