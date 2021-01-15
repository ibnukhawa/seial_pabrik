from odoo import api, fields, models
from datetime import datetime,timedelta,time

class SerialNumberPabrik(models.Model):
    _name = "serial.number.pabrik"

    name = fields.Char(string = 'Serial Number Pabrik', help = 'Enter S/N', required =True)
    number_product = fields.Char(string = 'Serial Number Pabrik', help = 'Enter S/N',)
    date = fields.Date(string='Tanggal',default=fields.Date.today())
    used_serial = fields.Boolean(string='Done')

    @api.onchange('number_product')
    def onchange_number_product(self):
        self.used = any(number_product.used for number_product in self.number_product)
        self.number_warn = 'block' if self.used else 'no-message'
        self.number_warn_msg = "Done" if self.number_warn != 'no-message' and not self.number_warn_msg else self.number_warn_msg


