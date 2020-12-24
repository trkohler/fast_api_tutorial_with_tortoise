from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}


def test_dynamic_routing():
    number: int = 10
    response = client.get(f"/dynamic_routing/{number}")
    assert response.status_code == 200
    assert response.json() == {"number": number}


def test_dynamic_routing_with_query_params():
    number: int = 10
    add: int = 12
    multiply: int = 4
    response = client.get(
        f"/dynamic_routing/{number}", params={"add": add, "multiply": multiply}
    )
    assert response.status_code == 200
    assert response.json() == {"number": (number + add) * multiply}