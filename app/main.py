import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.routes import router as api_router
from mangum import Mangum
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

app = FastAPI()

# Rate limiting: 10 requests per minute per IP
limiter = Limiter(key_func=get_remote_address, default_limits=["10/minute"])
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": str(exc)})


app.include_router(api_router, prefix="/api", tags=["starwars"])


def gcp_entrypoint(request):
    from mangum import Mangum

    handler = Mangum(app)
    return handler(request)
