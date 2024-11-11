from odoo import models, fields

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    appointment_datetime = fields.Datetime(string='Appointment DateTime')
    description = fields.Text(string='Description')
