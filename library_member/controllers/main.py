from odoo import http
from odoo.addons.library_app.controllers.main import Books

class BooksExtended(Books):
    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        available_param = kwargs.get("available")
        
        # Check if the response has the data we want to filter
        if hasattr(response, 'qcontext') and available_param in ['0', '1']:
            all_books = response.qcontext.get("books")
            if all_books:
                if available_param == "1":
                    # Keep only books where is_available is True
                    filtered_books = all_books.filtered(lambda b: b.is_available)
                else:
                    # Keep only books where is_available is False
                    filtered_books = all_books.filtered(lambda b: not b.is_available)
                
                response.qcontext["books"] = filtered_books
        
        return response