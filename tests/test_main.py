import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestRootRoute:
    """Test cases for the / route"""

    def test_root_empty_state(self) -> None:
        """Test the root endpoint with an empty state"""
        response = client.get("/")
        assert response.status_code == 422
        result = response.json()
        assert result["message"] == "Validation error"

class TestHealthRoute:
    """Test cases for the /health route"""

    def test_health_check(self) -> None:
        """Test the health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


if __name__ == "__main__":
    pytest.main([__file__])
