import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestMeanPriceRoute:
    """Test cases for the /mean-price/{state} route"""

    def test_mean_price_invalid_state(self) -> None:
        """Test the mean price endpoint with an invalid state"""
        for invalid_state in ["invalid_state", "nsw"]:
            response = client.get(f"/mean-price/{invalid_state}")
            assert response.status_code == 422
            result = response.json()
            assert result["message"] == "Validation error"

    def test_mean_price_valid_state(self) -> None:
        """Test the mean price endpoint with a valid state"""
        for state in ["NSW", "VIC", "QLD", "SA", "TAS"]:
            response = client.get(f"/mean-price/{state}")
            result = response.json()
            assert (
                response.status_code == 200
            ), f"State {state} returned {response.status_code},Error: {result}"
            assert "state" in result
            assert "mean_price" in result
            assert result["state"] == state
            assert result["mean_price"] > 1

    def test_mean_price_missing_state(self) -> None:
        """Test the mean price endpoint with a state missing from the data"""

        for state in ["ACT", "NT", "WA"]:
            response = client.get(f"/mean-price/{state}")
            assert response.status_code == 400
            result = response.json()
            assert "not found in data" in result["error"]


class TestHealthRoute:
    """Test cases for the /health route"""

    def test_health_check(self) -> None:
        """Test the health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


if __name__ == "__main__":
    pytest.main([__file__])
