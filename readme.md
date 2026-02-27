# 📚 Library Management System

A custom Odoo 15 application designed to manage library books, authors, and memberships.

---

## 🚀 Getting Started

Follow these steps to activate the development environment and launch the Odoo server.

### 1. Open Ubuntu Terminal
Ensure you are operating within your WSL/Ubuntu instance where the project files are located.

### 2. Activate the Python Virtual Environment
Run the following command to load the Odoo 15 dependencies:
```bash
source ~/[insert file directory of your python dependencies]/bin/activate
```

### 3. Start the app on http://localhost:8069/
Run the following app to start the library app in Ubuntu:
```bash
odoo -c ~/.odoorc -d library
```

### 3. Update the Library app
Run the following app to update the library app in Ubuntu:
```bash
odoo -c ~/.odoorc -d library -u library_app
```
