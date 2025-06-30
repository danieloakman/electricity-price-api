from typing import Dict, Any, List
from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from validation import AustralianState
from electricity_prices import mean_price_by_state

app = FastAPI(title="Electricity Usage API", version="0.1.0")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """Handle Pydantic validation errors with detailed error messages"""
    errors: List[Dict[str, Any]] = [
        {
            "field": " -> ".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"],
            "input": error.get("input"),
        }
        for error in exc.errors()
    ]

    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation error",
            "errors": errors,
            "detail": "One or more fields failed validation",
        },
    )


@app.get("/health")
async def health_check() -> JSONResponse:
    """Health check endpoint"""
    return JSONResponse(content={"status": "healthy"}, status_code=200)


@app.get("/mean-price/{state}")
async def root(state: AustralianState) -> JSONResponse:
    """Get the electricity usage for a given state."""

    print("state:", state)
    try:
        mean_price = mean_price_by_state(state)
        return JSONResponse(
            content={"state": state, "mean_price": mean_price},
            status_code=200,
        )
    except ValueError as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=400,
        )


if __name__ == "__main__":
    from uvicorn import run

    run(app, host="0.0.0.0", port=8000)
