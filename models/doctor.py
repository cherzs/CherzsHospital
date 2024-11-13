from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    doctor_id = fields.Char(string='Doctor ID', required=True)
    specialization = fields.Char(string='Specialization')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    avatar_128 = fields.Image(string='Avatar', max_width=128, max_height=128)
    doctor_type = fields.Selection([
        ('permanent', 'Permanent'),
        ('intern', 'Intern'),
        ('visiting', 'Visiting')
    ], string='Doctor Type', required=True, default='permanent')
