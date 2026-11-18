# Real Estate Property Management (Odoo 17)

An Odoo 17 module for managing properties and owners, with a state workflow and history tracking, OWL components, an API, Excel reporting, and Arabic translation.

> Technical module name: `app_one`.

## Features

- **Properties & owners** with tags and chatter (`mail.thread`, activities).
- **Workflow:** Draft / Sold / Rejected / Closed, with a **history** log of every state change and a **change-state wizard**.
- **Validation:** SQL `UNIQUE` constraint on the property name, and Python constraints on expected price and bedrooms.
- **Integration:** extends `sale.order`, `account.move`, and `res.partner` (depends on `sale_management` and `account`).
- **OWL components:** custom list view and form view.
- **Reports:** QWeb PDF (with a custom font) and an Excel (XLSX) report.
- **REST API:** `POST /v1/property` (create) and `GET /v1/property/<id>` (read).
- **i18n:** Arabic translation (`ar_001.po`).
- **Unit tests** (`TransactionCase`).

## Notes

- The API endpoints are demo-grade: the create endpoint uses `auth='none'` and should be protected (API key / authenticated user) before any production use.
- Additional endpoints (update, delete, list) exist in the controller but are currently commented out.

## Stack

Python · XML · OWL (JavaScript) · CSS · PostgreSQL · QWeb · XLSX

## Installation

1. Copy this folder into your Odoo `addons` directory as `app_one`.
2. Update the apps list and install **App one**.

## Author

Yousef Ibrahim — [GitHub](https://github.com/yousefemara09) · [LinkedIn](https://www.linkedin.com/in/yousef-ibrahim-148b48240/)
