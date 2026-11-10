"""Unit tests for ShopifyERPNextSyncEngine."""

from sync_engine.engine import ShopifyERPNextSyncEngine, ShopifyOrderWebhook, ShopifyOrderLine


def test_shopify_order_to_erpnext_sales_order():
    webhook = ShopifyOrderWebhook(
        id=99283746,
        order_number="1042",
        email="customer@example.com",
        financial_status="paid",
        line_items=[
            ShopifyOrderLine(sku="SKU-TSHIRT-BLK", title="Cotton T-Shirt Black (M)", quantity=2, price=799.0)
        ],
        total_price=1598.0,
        shipping_address={"name": "Aakash Patel", "city": "Mumbai"},
    )

    so = ShopifyERPNextSyncEngine.map_shopify_order_to_erpnext(webhook)
    assert so.customer == "Aakash Patel"
    assert so.po_no == "SHOPIFY-1042"
    assert len(so.items) == 1
    assert so.items[0]["item_code"] == "SKU-TSHIRT-BLK"
    assert so.grand_total == 1598.0
