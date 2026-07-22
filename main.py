from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Bitaxe Gamma 601 Hardware Sales API",
    description="API oficial para la venta de par de minadores Bitaxe Gamma 601",
    version="2.0.0"
)

# Datos del producto y wallet configurada
PRODUCT_DATA = {
    "item_id": "bitaxe-gamma-601-pair",
    "title": "2x Bitaxe Gamma 601 ASICs (Pair)",
    "status": "available",
    "price_usd": 150.00,
    "currency": "USD",
    "total_hashrate": "2.41 TH/s combined",
    "power_consumption": "~36W total",
    "description": "Lote de 2 minadores ASIC Bitaxe Gamma 601 listos para minería en solitario o pool.",
    "payment_methods": {
        "usdt_trc20": "TAS6CrszaXy6wX4oovuVHaRPugNJZAQxL1"
    },
    "instructions": "Envía el monto equivalente en USDT (TRC20) a la dirección indicada. Notifica al vendedor con el Hash de la transacción para coordinar el envío."
}

@app.get("/")
def get_root():
    return {
        "message": "Bienvenido a la API comercial de Bitaxe Gamma 601",
        "docs": "/docs",
        "product_endpoint": "/product"
    }

@app.get("/product")
def get_product():
    """Devuelve los detalles del producto, precio y dirección de wallet"""
    return PRODUCT_DATA

@app.get("/health")
def health_check():
    return {"status": "ok"}
    
