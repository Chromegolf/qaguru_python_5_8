import pytest
from api.models import Product
from api.models import Cart

@pytest.fixture
def cart():
    return Cart()
