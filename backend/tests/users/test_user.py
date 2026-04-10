import pytest

pytestmark = pytest.mark.django_db

from app.services.user_service import create_user, get_user_by_id


def test_create_user_success():
    user = create_user(
        name="Bianca",
        email="bianca@email.com",
        password="123456"
    )

    assert user is not None
    assert user.id is not None
    assert user.email == "bianca@email.com"


def test_create_user_duplicate_email():
    create_user(
        name="Bianca",
        email="bianca@email.com",
        password="123456"
    )

    with pytest.raises(Exception):
        create_user(
            name="Outro Usuario",
            email="bianca@email.com",
            password="abcdef"
        )


def test_get_user_by_id():
    user = create_user(
        name="Bianca",
        email="bianca2@email.com",
        password="123456"
    )

    found_user = get_user_by_id(user.id)

    assert found_user is not None
    assert found_user.id == user.id


def test_get_user_not_found():
    user = get_user_by_id(999999)

    assert user is None