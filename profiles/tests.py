import pytest
from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Profile


@pytest.mark.django_db
def test_profiles_index():
    client = Client()
    path = reverse('profiles:index')
    response = client.get(path)
    assert response.status_code == 200
    assert b'<title>Profiles</title>' in response.content
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile():
    client = Client()
    user = User.objects.create_user(username='test', password='test')
    profile = Profile.objects.create(user=user, favorite_city='Lyon')
    result = client.get(reverse('profiles:profile', args=[profile.user]))
    assert result.status_code == 200
    assert 'Lyon' in str(result.content)


# @pytest.mark.django_db
# def test_profiles():
#     client = Client()
#     profiles = Profile.objects.all()
#     for profile in profiles:
#         path = reverse('profiles:profile', args=[profile.user])
#         response = client.get(path)
#         assert response.status_code == 200
#         assert profile.user in response.content
