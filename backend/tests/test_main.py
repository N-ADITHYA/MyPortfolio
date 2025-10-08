from fastapi.testclient import TestClient
from backend.main import app
from backend.database import session_local, Base, engine
from backend.models import ContactForm

# Use a test database for isolation
def setup_test_db():
    Base.metadata.create_all(bind=engine)

def teardown_test_db():
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_create_user():
    # Setup test database before running the test
    setup_test_db()

    # Define the data to send
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "message": "This is a test message."
    }

    # Make a POST request to the endpoint
    response = client.post("/create_user", json=user_data)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response data matches what you expect
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "timestamp" in data

    # Teardown test database after the test completes
    teardown_test_db()