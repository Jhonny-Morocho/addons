from odoo import fields,models

class Ficha (models.Model):

    _name = 'ft.ficha'
    _description = 'Tabla de fichas tecnicas'
    #name=""
    name = fields.Char(string="Vehiculo",required=True)
    combustible= fields.Selection(selection=[("gasolina","Gasolina"),("diesel","Diesel")],
                                string="Tipo de combustible",required=True)

    torque_maximo = fields.Char(string="Torque Máximo",required=True)

    traccion = fields.Selection(selection=[("delantera","Delantera"),("trasera","Trasera")],
                                string="Tipo de Ubicacion",required=True)
                                
    cilindraje = fields.Float(string="Cilindraje")
    caja = fields.Selection(selection=[("manual","Manual"),("automatica","Automatica")],
                            string="Tipo de caja de Cambio",required=True)
    num_cilindros = fields.Float(string="Numero de cilindros",required=True)
    vehiculo_image = fields.Binary(string="Foto del vehiculo")