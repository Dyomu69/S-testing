from unittest.mock import patch
from app import app

@patch('app.internships', new_callable=list)
def test_mocked_internship(mock_list):
    client = app.test_client()
    response = client.post('/internships', json={"title": "Mocked Job"})
    assert len(mock_list) == 1