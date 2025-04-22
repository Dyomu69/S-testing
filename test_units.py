import pytest
from app import app

def test_create_internship():
    client = app.test_client()
    response = client.post('/internships', json={"title": "Test Role"})
    assert response.status_code == 201