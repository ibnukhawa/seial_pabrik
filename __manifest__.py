{
  'name': 'Serial Number Pabrik',
  'author': 'Odoo Innograph',
  'version': '0.1',
  'depends': [
    'stock','product',
  ],
  'data': [
    
    'views/serial_number_pabrik.xml',
    'views/stock_picking.xml',
  ],
  'qweb': [
    # 'static/src/xml/nama_widget.xml',
  ],
  'sequence': 4,
  'auto_install': False,
  'installable': True,
  'application': True,
  'category': 'Serial Number Pabrik',
  'summary': 'Add Product With Serial Number Pabrik at Inventory',
  'license': 'OPL-1',
  'images': ['static/description/icon.png'],
  'description': '-'
}