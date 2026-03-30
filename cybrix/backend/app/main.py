from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.analyze import router as analyze_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="CYBRIX AI API",
        description="Initial API foundation for cybersecurity analysis workflows.",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(analyze_router, prefix="/analyze", tags=["Analyze"])

    @app.get("/health", tags=["Health"])
    def healthcheck() -> dict[str, str]:
        return {"status": "ok"}

    return app
app = create_app()