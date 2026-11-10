"""Shopify E-Commerce & ERPNext Bi-Directional Synchronization Engine."""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class ShopifyOrderLine(BaseModel):
    sku: str
    title: str
    quantity: int
    price: float


class ShopifyOrderWebhook(BaseModel):
    id: int
    order_number: str
    email: str
    financial_status: str  # paid, pending
    fulfillment_status: Optional[str] = None
    line_items: List[ShopifyOrderLine]
    total_price: float
    shipping_address: Dict[str, Any]


class ERPNextSalesOrderPayload(BaseModel):
    doctype: str = "Sales Order"
    customer: str
    po_no: str  # Shopify Order ID
    items: List[Dict[str, Any]]
    grand_total: float


class ShopifyERPNextSyncEngine:
    """Translates and maps Shopify order webhooks into ERPNext Sales Orders."""

    @staticmethod
    def map_shopify_order_to_erpnext(order: ShopifyOrderWebhook) -> ERPNextSalesOrderPayload:
        customer_name = order.shipping_address.get("name", order.email)

        erp_items = [
            {
                "item_code": line.sku or "GENERIC-ECOMM",
                "item_name": line.title,
                "qty": line.quantity,
                "rate": line.price,
                "amount": line.quantity * line.price,
            }
            for line in order.line_items
        ]

        return ERPNextSalesOrderPayload(
            customer=customer_name,
            po_no=f"SHOPIFY-{order.order_number}",
            items=erp_items,
            grand_total=order.total_price,
        )

    @staticmethod
    def map_erpnext_stock_to_shopify(item_code: str, warehouse_qty: float) -> Dict[str, Any]:
        """Prepare Shopify inventory_levels/set payload."""
        return {
            "sku": item_code,
            "available": int(warehouse_qty),
        }
