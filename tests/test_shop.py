"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from api.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        product.buy(999)
        assert product.quantity == 1
        product.buy(1)
        assert product.quantity == 0
        with pytest.raises(ValueError):
            assert product.buy(1)

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:

    def test_add_product(self, cart, product):
        assert len(cart.products) == 0
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product, 1000)
        assert cart.products[product] == 1001

    def test_remove_product(self, cart, product):
        cart.add_product(product, 1000)
        cart.remove_product(product, 999)
        assert cart.products[product] == 1
        cart.remove_product(product, 1)
        assert len(cart.products) == 0
        with pytest.raises(ValueError):
            assert cart.remove_product(product, 1)

    def test_clear(self, cart, product):
        cart.add_product(product, 1000)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 99)
        assert cart.get_total_price() == 9900

    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy(product)
        assert len(cart.products) == 0
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy(product)





