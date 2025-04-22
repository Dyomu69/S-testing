from app import app  # <-- Ensure this line exists

def test_api_error_handling():
    client = app.test_client()  # <-- Use app.test_client(), NOT app.apptest_client()
    response = client.post(
        '/internships',
        data="invalid",
        headers={'Content-Type': 'application/json'}  # Fixed syntax
    )
    assert response.status_code == 400