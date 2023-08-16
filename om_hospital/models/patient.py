from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'hospital patient'

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Integer(String='Reference')
    dob = fields.Date(String='Date of Birth')
    age = fields.Integer(string='Age', tracking=True, compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(String='Active',
                            default=True)  # by adding default value as True, records will be visible when they will be created.
# Image field
    image = fields.Image(string='Image')

# many2one field
    appointment_id= fields.Many2one('hospital.appointment', String="Appointment")

# many2many field
    tag_ids = fields.Many2many('hospital.appointment',string='Tags')

    @api.depends('dob')
    def _compute_age(self):
        for i in self:
            today = date.today()
            if i.dob:
                i.age = today.year - i.dob.year
            else:
                i.age = 1
