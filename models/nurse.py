from odoo import models, fields

class Nurse(models.Model):
    _name = 'hospital.nurse'
    _description = 'Nurse'

    name = fields.Char(string='Name', required=True)
    nurse_id = fields.Char(string='Nurse ID', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    department = fields.Char(string='Department')
    shift = fields.Selection([
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', 'Night')
    ], string='Shift', required=True)
    patient_id = fields.Many2many('hospital.patient', string='Patients') 