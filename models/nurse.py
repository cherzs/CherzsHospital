from odoo import models, fields, api

class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _description = 'Hospital Nurse'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, tracking=True)
    nurse_id = fields.Char(string='Nurse ID', required=True, tracking=True)
    department = fields.Selection([
        ('emergency', 'Emergency'),
        ('icu', 'ICU'),
        ('general', 'General Ward'),
        ('pediatric', 'Pediatric'),
        ('surgical', 'Surgical'),
    ], string='Department', required=True, tracking=True)
    nurse_type = fields.Selection([
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
    ], string='Type', default='full_time', tracking=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')
    zip_code = fields.Char(string='ZIP')
    notes = fields.Text(string='Notes')

    _sql_constraints = [
        ('unique_nurse_id', 'unique(nurse_id)', 'Nurse ID must be unique!')
    ]