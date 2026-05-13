from api.client import APIClient
from api.endpoints import BASE_URL, GET_USERS, CREATE_USER

client = APIClient(BASE_URL)

def test_get_users():
    
    response = client.get(GET_USERS)
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert "data" in data
    assert len(data["data"]) > 0
    
    
def test_create_user():
    payload = {
        "name" : "John",
        "job" : "SDET"
    }
    response = client.post(CREATE_USER,payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John"
    assert data["job"] == "SDET"
    
    '''
    Now your project shows:

    ✅ UI automation
    ✅ API automation
    ✅ Layered architecture
    
    Interview Gold

If asked:

👉 “Why API testing?”

Say:

“UI tests are slower and flaky.     
I validate business logic at the API layer for faster feedback and use UI tests only for end-to-end coverage.”

Your project now includes:

POM-based UI framework
End-to-end flows
Parameterized tests
API layer
    '''
    
    