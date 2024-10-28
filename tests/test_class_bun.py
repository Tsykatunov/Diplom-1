import pytest
from bun import Bun

def test_bun_init():
    bun = Bun("test bun", 100)
    assert bun.name == "test bun"
    assert bun.price == 100

@pytest.mark.parametrize("name, price, expected_name, expected_price", [
    ("white bun", 200, "white bun", 200),
    ("black bun", 150, "black bun", 150)
])
def test_bun_getters(name, price, expected_name, expected_price):
    bun = Bun(name, price)
    assert bun.get_name() == expected_name
    assert bun.get_price() == expected_price