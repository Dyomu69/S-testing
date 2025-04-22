from app import app

def test_integration():
    client = app.test_client()
    client.post('/internships', json={"title": "Integration Test"})
    response = client.get('/internships')
    assert len(response.json) == 1