from dotenv import load_dotenv
import os

# Load environment variables BEFORE any other imports
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Import blockchain router (this will now have access to .env variables)
from routers.blockchain import router as blockchain_router
from routers.blockchain_logs_router import router_blockchain_logs as BlockchainLogsRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup/shutdown events
    """
    # Startup
    print("🚀 Starting Blockchain Activity Logging Service...")
    print("✅ Service initialized")
    
    yield  # Application runs here
    
    # Shutdown
    print("🛑 Shutting down Blockchain Activity Logging Service...")
    print("✅ Service stopped")

app = FastAPI(
    title="Blockchain Activity Logging Service",
    description="Microservice for logging all POST and PATCH operations to BuildBear Blockchain",
    version="1.0.0",
    lifespan=lifespan
)

# Include blockchain router
app.include_router(blockchain_router, prefix="/blockchain", tags=["Blockchain Logging"])
app.include_router(BlockchainLogsRouter, prefix="/blockchain-logs", tags=["Blockchain Logs"])

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://bleu-ums-zeta.vercel.app",
        "https://bleu-ims-beta.vercel.app",
        "https://bleu-pos-tau.vercel.app",
        "https://authservices-npr8.onrender.com",
        "https://bleu-stockservices.onrender.com",
        "https://ims-restockservices.onrender.com",
        "https://bleu-oos-rouge.vercel.app",
        "https://ordering-service-8e9d.onrender.com",
        "https://sales-services.onrender.com",
        "https://blockchainservices.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/", tags=["Health Check"])
def read_root():
    return {
        "status": "ok",
        "message": "Blockchain Activity Logging Service is running.",
        "service": "blockchain-logger",
        "port": 9005,
        "version": "1.0.0"
    }

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {
        "status": "healthy",
        "service": "blockchain-logger",
        "port": 9005
    }

# Uvicorn runner
if __name__ == "__main__":
    import uvicorn
    
    print("=" * 70)
    print("🔗 Starting Blockchain Activity Logging Service on http://0.0.0.0:9005")
    print("📚 API docs available at http://127.0.0.1:9005/docs")
    print("🔐 BuildBear Blockchain Integration Enabled")
    print("=" * 70)
    
    uvicorn.run("main:app", port=9005, host="0.0.0.0", reload=True)