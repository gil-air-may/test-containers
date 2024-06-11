from starlette.testclient import TestClient
import ipdb


from main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "world"}


def test_get_all_tabs():
    response = client.get("/tabs")
    assert response.status_code == 200
    assert response.json() == [
        {
            "tab_id": 1,
            "table_number": 1,
            "is_paid": 0,
            "items": '[{"name": "chicken_salad", "amount": 1}]',
            "from_day": "2024-05-18",
            "created_at": "2024-05-18T20:36:42",
        }
    ]
