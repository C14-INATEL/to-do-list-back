from types import SimpleNamespace
from unittest.mock import patch

import pytest
from django.contrib.auth.models import User
from rest_framework import status

from app.services.user_service import get_user_by_id
from users.views import UserDetailView


def test_get_user_by_id_returns_none_when_user_does_not_exist():
    with patch("app.services.user_service.User.objects.get") as mock_get:
        mock_get.side_effect = User.DoesNotExist

        result = get_user_by_id(999)

        mock_get.assert_called_once_with(id=999)
        assert result is None


def test_user_detail_get_returns_authenticated_user_data():
    request = SimpleNamespace(
        user=SimpleNamespace(id=5, username="antonio@email.com", email="antonio@email.com", first_name="Antonio")
    )

    response = UserDetailView().get(request)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == 5
    assert response.data["email"] == "antonio@email.com"
    assert response.data["first_name"] == "Antonio"
