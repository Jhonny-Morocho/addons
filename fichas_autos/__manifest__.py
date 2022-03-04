# -*- coding: utf-8 -*-
{
    'name': "Ficha tecnica",

    'summary': """
        FICHAS DE AUTOS""",

    'description': """
        Crear un módulo en Odoo 15 que sea capaz de crear fichas técnicas de autos con 10
campos mínimo. Los datos deben persistir en la base de datos. Se debe listar en el front
todas las fichas técnicas asociadas al proveedor y cada ficha técnica se debe modificar,
eliminar o imprimir. Se debe poder dar de baja y volver a activar las fichas técnicas. Las
fichas técnicas que estén dadas de bajas, deben aparecer también en el listado de las
fichas asociadas al proveedor.
Todas estas acciones deben ser desde el front, las mismas deben ser responsive.
Desde el backend se gestionarán todas las fichas técnicas. Las fichas técnicas se deben
dar de baja y en la vista de Tree se deben visualizar de diferente color. Sólo el asesor
asociado a la cuenta de un proveedor, debe ser capaz de modificar sus fichas técnicas
en el backend.
    """,

    'author': "Jhonny Morocho",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir_model_access.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
