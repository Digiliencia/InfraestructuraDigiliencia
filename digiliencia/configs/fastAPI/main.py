# /main.py
# Added middleware for CORS, rate limiting, and security headers
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from api.routers import auth  # Add other routers here
from core.config import settings

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address, default_limits=["100 per minute"])

app = FastAPI(
    title="Secure and Performant Chat API",
    description="An API with async support, refresh tokens, rate limiting, and security headers.",
)

# Add state for the limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# --- Middleware ---
# 1. CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 2. Security Headers Middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self'"
    )
    return response


# --- Routers ---
# Apply rate limiting to specific routers or endpoints
api_router = APIRouter(prefix="/api")


# Rate limit the auth router more strictly
@app.middleware("http")
async def rate_limit_auth(request: Request, call_next):
    try:
        if request.url.path.endswith("/login") or request.url.path.endswith(
            "/register"
        ):
            await limiter.check(request)
    except RateLimitExceeded as e:
        return JSONResponse(
            status_code=429, content={"detail": f"Too many requests: {e.detail}"}
        )
    response = await call_next(request)
    return response


api_router.include_router(auth.router)
api_router.include_router(auth.users_router)

app.mount("/api", api_router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "API REST"}
