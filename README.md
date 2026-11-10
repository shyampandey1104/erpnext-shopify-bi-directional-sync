# 🛍️ ERPNext & Shopify Bi-Directional Synchronization Engine

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Shopify API](https://img.shields.io/badge/Shopify-REST%20%7C%20Webhooks-95BF47.svg?logo=shopify)](https://shopify.dev)
[![ERPNext](https://img.shields.io/badge/ERPNext-v14%20%7C%20v15-blue.svg)](https://erpnext.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-throughput **E-Commerce Integration Pipeline** connecting **Shopify Stores** with **ERPNext**. Ingests Shopify order webhooks, maps taxes and SKUs to create native ERPNext `Sales Order` & `Customer` DocTypes, and syncs warehouse stock levels back to Shopify online inventory.

---

## ⚡ Highlights
- ⚡ **Real-Time Order Ingestion**: Automated transformation of Shopify `orders/create` webhooks.
- 📦 **Inventory Broadcast**: Pushes ERPNext Bin actual quantities to Shopify inventory levels.
- 🚚 **Fulfillment Sync**: Converts Shopify fulfillment events into ERPNext `Delivery Note` records.
- 🧪 **Pytest Coverage**: Unit tests included.

Author: **Shyamkumar Bhupendra Pandey** ([@shyampandey1104](https://github.com/shyampandey1104))
