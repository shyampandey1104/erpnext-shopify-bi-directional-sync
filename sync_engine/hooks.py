# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "sync_engine"
app_title = "Erpnext Shopify Bi Directional Sync"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Shopify Bi Directional Sync - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/sync_engine/css/sync_engine.bundle.css"
app_include_js = "/assets/sync_engine/js/sync_engine.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Shopify Bi Directional Sync Entry": {
        "validate": "sync_engine.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "sync_engine.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "sync_engine.tasks.hourly_sync"
    ],
    "daily": [
        "sync_engine.tasks.daily_reconciliation"
    ],
    "weekly": [
        "sync_engine.tasks.weekly_digest"
    ]
}
