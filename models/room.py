from odoo import models, fields, api

class HospitalRoom(models.Model):
    _name = 'hospital.room'
    _description = 'Hospital Room'

    name = fields.Char(string='Name', required=True)
    room_number = fields.Char(string='Room Number', required=True)
    room_type = fields.Selection([
        ('general', 'General Ward'),
        ('private', 'Private Room'),
        ('icu', 'ICU'),
        ('operation', 'Operation Theater'),
    ], string='Room Type', required=True)
    capacity = fields.Integer(string='Capacity')
    status = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Under Maintenance'),
    ], string='Status', default='available')
    notes = fields.Text(string='Notes')

    _sql_constraints = [
        ('unique_room_number', 'unique(room_number)', 'Room number must be unique!')
    ]
 