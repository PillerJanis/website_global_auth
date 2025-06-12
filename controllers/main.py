from odoo import http
from odoo.http import request

class WebsiteGlobalAuth(http.Controller):
    @http.route(['/shop', '/website', '/'], type='http', auth='public', website=True)
    def restrict_access(self, **kw):
        if not request.env.user._is_authenticated():
            return request.redirect('/web/login')
        # Wenn angemeldet, normale Seite laden
        return request.redirect(request.httprequest.path)  # oder rendere original
