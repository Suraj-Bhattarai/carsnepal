import pytest
from django.urls import reverse



def test_category_str(contact):
    assert category.__str__() == "django"




# def test_product_url_resolve(client, product):
#     slug = "product-slug"
#     url = reverse("catalogue:product_detail", args=[slug])
#     response = client.get(url)
#     assert response.status_code == 200


