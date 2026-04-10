from django.contrib.auth.models import User

def create_user(name, email, password):
    if User.objects.filter(email=email).exists():
        raise Exception("Email already exists")
    user = User.objects.create_user(username=email, email=email, first_name=name, password=password)
    return user

def get_user_by_id(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None