from odoo import models, fields

class Room(models.Model):
    _name = 'hospital.room'
    _description = 'Hospital Room'

    name = fields.Char(string='Room Name', required=True)
    room_number = fields.Char(string='Room Number', required=True)
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    ], string='Room Type', required=True)
    capacity = fields.Integer(string='Capacity', default=1)
    is_available = fields.Boolean(string='Is Available', default=True)
    patient_id = fields.One2many('hospital.patient', 'room_id', string='Patients') 