from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Bitaxe Gamma 601 Hardware Sale API",
    description="API oficial para la venta directa de 2x minadores Bitaxe Gamma 601 (BM1370).",
    version="2.0.0"
)

# Datos del producto físico
PRODUCT_DATA = {
    "item_id": "bitaxe-gamma-601-pair",
    "title": "Pack 2x Bitaxe Gamma 601 (BM1370 ASIC)",
    "status": "Available",
    "condition": "Used - Excellent Condition",
    "total_hashrate": "2.41 TH/s combined",
    "price_usdc": 250.00,  # Reemplaza con tu precio de venta
    "accepted_payment": "USDC on Base / Ethereum",
    "seller_wallet": "0xTU_WALLET_AQUI_EN_BASE",  # Pon tu wallet de Base aquí
    "specs": {
        "asic_chip": "BM1370",
        "power_consumption": "36W total",
        "includes": ["2x Bitaxe Gamma 601 boards", "Power supplies", "OLED displays pre-configured"]
    },
    "shipping": {
        "location": "Mexico",
        "shipping_methods": "Local pickup or international tracked shipping available"
    }
}

@app.get("/api/v1/hardware/item", summary="Consultar detalles del producto en venta")
def get_item_details():
    return PRODUCT_DATA

@app.post("/api/v1/hardware/buy-intent", summary="Registrar intención de compra")
def create_buy_intent(buyer_wallet: str, contact_info: str):
    return {
        "success": True,
        "message": "Intención de compra registrada. Envía el pago a la wallet indicada o contacta para el envío.",
        "pay_to": PRODUCT_DATA["seller_wallet"],
        "amount_usdc": PRODUCT_DATA["price_usdc"],
        "network": "Base (L2)"
    }
