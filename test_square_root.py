import math
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_valid_number():
    response = client.get("/square-root?number=25")
    assert response.status_code == 200
    assert response.json() == {"number": 25, "square_root": 5}
    response = client.get("/square-root?number=100")
    assert response.status_code == 200
    assert response.json() == {"number": 100, "square_root": 10}



def test_invalid_number():
    response = client.get("/square-root?number=5")
    assert response.status_code == 400
    assert response.json() == {"detail": "The number must be between 10 and 100"}
    
    response = client.get("/square-root?number=9")
    assert response.status_code == 400
    assert response.json() == {"detail": "The number must be between 10 and 100"}

    response = client.get("/square-root?number=101")
    assert response.status_code == 400
    assert response.json() == {"detail": "The number must be between 10 and 100"}

if __name__ == "__main__":
    test_valid_number()
    test_invalid_number()
    print("tests passed")
