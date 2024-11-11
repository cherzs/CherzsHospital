from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'

    name = fields.Char(string='Name')
    patient_id = fields.Char(string='Patient ID')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
