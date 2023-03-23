import pytest
from django.test import Client
from django.urls import reverse, resolve
from .models import Letting, Address


@pytest.mark.django_db
def test_lettings_index():
    client = Client()
    path = reverse('lettings:index')
    response = client.get(path)
    assert response.status_code == 200
    assert b'<title>Lettings</title>' in response.content
    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db
def test_letting():
    client = Client()
    address = Address.objects.create(
        number=1111, street='xxxxx',
        city='xxxxx', state='xxxxx',
        zip_code=1111, country_iso_code='xxxx'
        )
    letting = Letting.objects.create(title='Test', address=address)
    result = client.get(reverse('lettings:letting', args=[letting.id]))
    assert result.status_code == 200
    assert b'<title>Test</title>' in result.content
