from odoo import fields,models

class Movimiento (models.Model):

    _name = 'sa.movimiento' #sa_movimiento
    _description = 'Tabla movimiento'
    ##campos
    name = fields.Char(string="Nombre",required=True)
    type_move= fields.Selection(selection=[("ingreso","Ingreso"),("gasto","Gasto")],
                                string="Tipo de movimiento",default="ingreso",required=True)
    date = fields.Datetime(string="Fecha")
    amount = fields.Float(string="Monto")
    receipt_image = fields.Binary(string="Foto del recibo")
    notas = fields.Html(string="Notas")
    ##crera relacion
    user_id = fields.Many2one('res.users',string='Usuarios')
    categoria_id = fields.Many2one('sa.category',string='Categoria')
    ##movimiento & tags es mucho a mucho
    #tag_ids = fields.Many2many('sa.tag') # odo hace= sa_movimiento_sa_tag_rel
    #nombre personalizado y los campos
    tag_ids = fields.Many2many('sa.tag','sa_mov_sa_tag_rel','mov_id','tag_id')
class Category(models.Model):

    _name = 'sa.category'
    _description = 'Tabla categoria'
    ##campos
    name = fields.Char("Nombre")
class Tag(models.Model):

    _name = 'sa.tag'
    _description = 'Tabla tags'
    ##campos
    name = fields.Char("Nombre")
## agregar un nuevo campo a una tabla existen de odoo ## extender un modelo
class ResUsers(models.Model):

    _inherit = 'res.users'
    #one may necesita tener user_id para trabajar 

    movimiento_ids = fields.One2many('sa.movimiento', 'user_id')
    

### LA TABLA USUARIO YA EXISTE POR ENDE OCUPAREMOS LA QUE VIENE EN ODOO ##


