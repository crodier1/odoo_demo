{
    "name": "Library Management",
    "summary": "Manage library catalog and book lending.",
    "category": "Services/Library",
    "author": "Daniel Reis",
    "license": "AGPL-3",
    "website": "https://github.com/PacktPublishing"
               "/Odoo-15-Development-Essentials",
    "version": "15.0.1.0.0",
    "depends": ["base"],
    "application": True,
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
        "data/res.partner.csv",
        "data/library.book.csv",
        "data/book_demo.xml",
    ]
}
