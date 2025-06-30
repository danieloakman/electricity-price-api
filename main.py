from typing import Dict, Any, List
from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

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


@app.get("/")
async def root(
    state: str = Query(..., description="The state of the electricity usage to query.")
) -> JSONResponse:
    """Get the electricity usage for a given state."""
    return JSONResponse(content={"state": state}, status_code=200)


if __name__ == "__main__":
    from uvicorn import run

    run(app, host="0.0.0.0", port=8000)
