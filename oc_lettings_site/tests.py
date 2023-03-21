from django.test import Client
from django.urls import reverse, resolve


def test_index():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    assert response.status_code == 200
    assert b"Welcome to Holiday Homes" in response.content
    assert resolve(path).view_name == "index"
