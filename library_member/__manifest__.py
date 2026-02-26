{
    "name": "Library Members",
    "version": "1.0",
    "license": "AGPL-3",
    "depends": ["library_app", "mail"],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ],
    "installable": True,
    "application": False,
}