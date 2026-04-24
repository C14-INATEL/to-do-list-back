from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest
from rest_framework import status

from app.services.user_service import create_user
from users.views import UserDetailView


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
