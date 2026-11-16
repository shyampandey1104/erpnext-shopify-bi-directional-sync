# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "sync_engine"
app_title = "Erpnext Shopify Bi Directional Sync"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Shopify Bi Directional Sync for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/sync_engine/css/sync_engine.bundle.css"
app_include_js = "/assets/sync_engine/js/sync_engine.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "sync_engine.engine.on_document_submit",
        "on_cancel": "sync_engine.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "sync_engine.engine.daily_scheduled_sync"
    ]
}
