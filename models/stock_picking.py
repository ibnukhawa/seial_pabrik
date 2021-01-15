from odoo import api, fields, models, _

class Picking(models.Model):
    _inherit = "stock.picking"

    serial_number_ids = fields.Many2many('serial.number.pabrik',string='Serial Number Pabrik')
    serial_number_pabrik = fields.Char(string = 'Serial Number Pabrik',)



 


