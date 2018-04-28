from openerp import models, fields, api, _
from odoo.exceptions import ValidationError, UserError



class UserTokenSetting(models.Model):
    
    _inherit = 'res.company'
    
    token_address = fields.Char(string="Token Addres for login")
    min_tokens_amount = fields.Float(string="Minimal token amount",help="How many tokens are needed for singup")
    token_interface = fields.Char(string="Token ABI")
    ethereum_address = fields.Char(string="Account address in Ethereum Blockchain")
    
    