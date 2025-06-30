import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestMeanPriceRoute:
    """Test cases for the /mean-price/{state} route"""

    def test_mean_price_invalid_state(self) -> None:
        """Test the mean price endpoint with an invalid state"""
        response = client.get("/mean-price/invalid_state")
        assert response.status_code == 422
        result = response.json()
        assert result["message"] == "Validation error"

    def test_mean_price_valid_state(self) -> None:
        """Test the mean price endpoint with a valid state"""
        response = client.get("/mean-price/NSW")
        assert response.status_code == 200
        result = response.json()
        assert "state" in result
        assert "mean_price" in result
        assert result["state"] == "NSW"


class TestHealthRoute:
    """Test cases for the /health route"""

    def test_health_check(self) -> None:
        """Test the health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


if __name__ == "__main__":
    pytest.main([__file__])
