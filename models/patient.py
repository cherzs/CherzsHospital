from odoo import models, fields, api

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    patient_id = fields.Char(string='Patient ID', required=True)
    age = fields.Integer(string='Age')
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    emergency_contact = fields.Char(string='Emergency Contact')
    blood_type = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('ab+', 'AB+'), ('ab-', 'AB-'), ('o+', 'O+'), ('o-', 'O-')], string='Blood Type')
    notes = fields.Text(string='Notes')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')
    room_id = fields.Many2one('hospital.room', string='Room')
    nurse_ids = fields.Many2many('hospital.nurse', string='Nurses')
    avatar_128 = fields.Image(string='Avatar', max_width=128, max_height=128)
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for patient in self:
            patient.appointment_count = len(patient.appointment_ids)

