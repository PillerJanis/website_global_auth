from odoo import http
from odoo.http import request

PUBLIC_WHITELIST = [
    '/web', '/web/login', '/web/signup', '/web/reset_password',
    '/website/seo_sitemap', '/website/translations', '/robots.txt',
]

class WebsiteGlobalAuth(http.Controller):

    @http.route(['/<path:path>', '/'], type='http', auth="public", website=True)
    def intercept_all(self, path='', **kwargs):
        path = '/' + path if path else '/'
        
        # Ignoriere bekannte technische oder Login-Routen
        for allowed in PUBLIC_WHITELIST:
            if path.startswith(allowed):
                return http.request._serve_static(path) if allowed.endswith('.txt') else None

        # Wenn nicht eingeloggt, weiterleiten zum Login
        if not request.env.user or request.env.user._is_public():
            return http.redirect_with_hash('/web/login')

        # Wenn eingeloggt: normal verarbeiten lassen
        return request._serve_page()
