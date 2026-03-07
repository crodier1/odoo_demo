{ "name": "Library Book Checkout",
  "description": "Members can borrow books from the library.",
  "author": "Daniel Reis",
  "depends": ["library_member"],
  "data": [
    "security/ir.model.access.csv",
    "wizard/checkout_mass_message_wizard_view.xml",
    "views/library_menu.xml",
    "views/checkout_view.xml",
    "data/library_checkout_stage.xml",
  ],
  "depends": ["library_member", "mail"],
}