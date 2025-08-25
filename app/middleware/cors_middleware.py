from fastapi.middleware.cors import CORSMiddleware #for resolve cors issue

def setup_cors(app):
    origins = [
        "http://localhost:3000",
        "https://localhost:3000"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
