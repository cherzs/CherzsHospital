from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Name')
    doctor_id = fields.Char(string='Doctor ID')
    specialization = fields.Char(string='Specialization')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
