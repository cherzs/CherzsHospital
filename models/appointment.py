from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one('hospital.patient', string='Patient', tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', tracking=True)
    appointment_datetime = fields.Datetime(string='Appointment DateTime', tracking=True)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    medical_notes = fields.Html(string='Medical Notes', tracking=True)
    reference = fields.Char(string='Reference', readonly=True, copy=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='State', default='draft', tracking=True)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string='Priority', default='1', tracking=True)
    color = fields.Integer(string='Color')
    company_id = fields.Many2one('res.company', string='Company', 
                                default=lambda self: self.env.company)
    active = fields.Boolean(default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference'):
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    @api.constrains('appointment_datetime')
    def _check_appointment_datetime(self):
        for record in self:
            if record.appointment_datetime and record.appointment_datetime < fields.Datetime.now():
                raise ValidationError("Appointment datetime cannot be in the past!")

    def name_get(self):
        return [(record.id, f"{record.reference} - {record.patient_id.name}") 
                for record in self]
