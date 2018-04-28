# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
import werkzeug

from odoo import http, _
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.main import ensure_db, Home
from odoo.exceptions import UserError
from odoo.http import request

_logger = logging.getLogger(__name__)

class DarfLogin(Home):
    
    def get_auth_signup_config(self):
        token_address = request.env['res.company'].search([],limit=1)
        qcontext = super(DarfLogin,self).get_auth_signup_config()
        qcontext.update({'token_address':token_address.token_address,
                         'abi':token_address.token_interface,
                         'min_tokens_amount':token_address.min_tokens_amount,})
        print(qcontext)
        return qcontext
    
    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        
        qcontext = self.get_auth_signup_qcontext()
        if 'error' not in qcontext and request.httprequest.method == 'POST':
            if 'min_tokens_amount' in qcontext.keys() and qcontext.get('token_amount') is not None:
                print(qcontext['min_tokens_amount'])
                print('test')
                if float(qcontext.get('token_amount')) <= qcontext['min_tokens_amount']:
                    raise werkzeug.exceptions.NotFound()
        
        res = super(DarfLogin,self).web_auth_signup(*args, **kw)
        return res