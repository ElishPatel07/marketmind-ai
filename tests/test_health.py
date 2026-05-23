"""
Basic API tests.

Automated tests help:
- prevent regressions
- validate API behavior
- support CI/CD pipelines
- improve deployment confidence
"""

from fastapi.testclient import TestClient

from apps.api.main import app

# Test client simulates HTTP requests
client = TestClient(app)


def test_root_endpoint():
    """
    Validate root endpoint response.
    """

    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()
