# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DoctorClass(models.Model):
    # _name = 'doctor.class'
    _inherit = ['account.move']
    
    delevery_done = fields.Boolean(string='Done', default=False, tracking=True)
    receipt_name = fields.Char(string='Recipient Name', tracking=True)
    receipt_number = fields.Char(string='Recipient Number', tracking=True)
