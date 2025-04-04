from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="clinical_diagnosis_extraction",
    )

    from clinical_diagnosis_extraction.routers import router

    app.include_router(router)

    return app


if __name__ == "__main__":
    app = create_app()

app = fastapi.FastAPI()
