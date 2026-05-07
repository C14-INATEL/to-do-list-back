from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest
from rest_framework import status

from app.services.user_service import create_user
from users.views import UserDetailView

from app.services.user_service import get_user_by_id


class TestUserWithMock:
    def test_create_user_raises_exception_when_email_already_exists(self):
        with patch("app.services.user_service.User.objects.filter") as mock_filter, patch(
            "app.services.user_service.User.objects.create_user"
        ) as mock_create_user:
            mock_filter.return_value.exists.return_value = True

            with pytest.raises(Exception, match="Email already exists"):
                create_user(name="Bianca", email="bianca@email.com", password="123456")

            mock_filter.assert_called_once_with(email="bianca@email.com")
            mock_create_user.assert_not_called()

    def test_user_detail_put_returns_400_when_serializer_is_invalid(self):
        request = SimpleNamespace(
            user=SimpleNamespace(id=1, username="user", email="user@test.com", first_name="User"),
            data={"email": "invalid-email"},
        )

        with patch("users.views.UserSerializer") as mock_serializer_class:
            mock_serializer = Mock()
            mock_serializer.is_valid.return_value = False
            mock_serializer.errors = {"email": ["Enter a valid email address."]}
            mock_serializer_class.return_value = mock_serializer

            response = UserDetailView().put(request)

            mock_serializer_class.assert_called_once_with(
                request.user, data=request.data, partial=True
            )
            mock_serializer.is_valid.assert_called_once_with()
            mock_serializer.save.assert_not_called()
            assert response.status_code == status.HTTP_400_BAD_REQUEST
            assert response.data == {"email": ["Enter a valid email address."]}

    def test_create_user_successfully_creates_user(self):
        with patch("app.services.user_service.User.objects.filter") as mock_filter, \
            patch("app.services.user_service.User.objects.create_user") as mock_create:

            # Simula que email NÃO existe
            mock_filter.return_value.exists.return_value = False

            # Usuário fake
            mock_user = Mock()
            mock_create.return_value = mock_user

            result = create_user("Bianca", "bianca@email.com", "123456")

            # Verifica se checou o email
            mock_filter.assert_called_once_with(email="bianca@email.com")

            # Verifica se tentou criar corretamente
            mock_create.assert_called_once_with(
                username="bianca@email.com",
                email="bianca@email.com",
                first_name="Bianca",
                password="123456"
            )

            # Verifica retorno
            assert result == mock_user

    def test_get_user_by_id_returns_user_when_found(self):
        with patch("app.services.user_service.User.objects.get") as mock_get:

            mock_user = Mock(id=1, email="bianca@email.com")
            mock_get.return_value = mock_user

            result = get_user_by_id(1)

            mock_get.assert_called_once_with(id=1)

            assert result == mock_user