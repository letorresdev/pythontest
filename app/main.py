from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum


from .api.api import router as api_router
# from .api.api import router as api_router
#   It is needed to fix, im the  lambda environment i need to  use . to import the modules not here. from .api.api import router as api_router

app = FastAPI(
    title="backend",
    version=2.0,
    root_path="/test/"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {'nessage' : "Hello world22"}

app.include_router(api_router, prefix='/api/v1' )

handler = Mangum(app)


# Endpoints
#  localhost:8000/api/v1/routes/
#  localhost:8000/api/v1/routes/new
