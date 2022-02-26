# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class todo_list(models.Model):
#     _name = 'todo_list.todo_list'
#     _description = 'todo_list.todo_list'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

## CREAR UNA TABLA 
##conectarme a la base de datos
from odoo import models,fields

class Todo(models.Model):
    #nombre de la tabla
    _name="todo_app" #nombre de la tabla
    _description="Lista de tareas"
    name=fields.Char(string='Nombre')
    state= fields.Char(string='Estado')


