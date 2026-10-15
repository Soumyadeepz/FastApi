
from fastapi.testclient import TestClient

from main import app

client = TestClient(app) # testclient i sused to simulate the api

# test home api
def test_home():
    response = client.get("/")
    #status code check
    assert response.status_code == 200
    # response data check(assert - check the expected result)
    assert response.json() == {"message":"hello soumya"}
    
# Test add api
def test_add():
    response = client.get("/add?a=5&b=3") # route
    
    assert response.status_code == 200
    assert response.json() =={"result":8}