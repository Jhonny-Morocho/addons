from odoo import fields,models

class Ficha (models.Model):

    _name = 'ft.ficha'
    _description = 'Tabla de fichas tecnicas'
    #name=""
    name = fields.Char(string="Marca Vehiculo",required=True)
    estado= fields.Boolean(string="Estado",required=True,default=True)
    combustible= fields.Selection(selection=[("gasolina","Gasolina"),("diesel","Diesel")],
                                string="Tipo de combustible",required=True)

    torque_maximo = fields.Char(string="Torque Máximo",required=True)

    traccion = fields.Selection(selection=[("delantera","Delantera"),("trasera","Trasera")],
                                string="Tipo de Ubicacion",required=True)
                                
    cilindraje = fields.Float(string="Cilindraje")
    caja = fields.Selection(selection=[("manual","Manual"),("automatica","Automatica")],
                            string="Tipo de caja de Cambio",required=True)
    num_cilindros = fields.Float(string="Numero de cilindros",required=True)
    vehiculo_image = fields.Binary(string="Foto del vehiculo",required=True)
    
    ##realcionar modelos con la tabla existente usuarios many2One tabla usuario con movimiento
    user_id = fields.Many2one('res.users',string='Usuario',default=lambda self:self.env.user.id)
    ##def onchange(self):
      ##  return{
        ##    "type":"ir.actions.act_window",
         #   "name":"Proveedor "+self.name,
          #  "res_model":"res.users",
           # "views":[[False,"tree"]],
            #"target"="self",
            #"domain":[["ficha_id","=",self.id]]
        #}
    
class ResUser(models.Model):
    _inherit = "res.users"
    ficha_id = fields.One2many('ft.ficha', 'user_id')
