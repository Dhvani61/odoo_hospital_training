from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'hospital appointment'
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', String="Patient")
    appointment_time = fields.Datetime(String='Appointment Time', default=fields.Datetime.now)
    appointment_date = fields.Date(String='Appointment Date', default=fields.Date.context_today)
    gendeeer = fields.Selection(string='Gender', tracking=True, related='patient_id.gender', readonly=False)
    ref = fields.Integer(String='Reference')
    prescription = fields.Html(string='Prescription')
    doctor_id = fields.Many2one("res.users", string="Doctors")

# one2many field
    pharmacy_line_ids = fields.One2many("appointment.pharmacy.lines", 'appointment_id', string='Pharmacy Lines')

    color= fields.Integer(string='color')
    hide_sales_price= fields.Boolean(string='Hide sales price')
    priority= fields.Selection(([
        ('0','Normal'),
        ('1', 'low'),
        ('2', 'high'),
        ('3', 'very high')]), string='priority', help="help for selection field")

    state= fields.Selection(([
        ('draft','Draft'),
        ('in_consultation','In consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
        ]), string='State', default='draft', required=True)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref


    def action_test(self):
        print("\n\n\n\n\n\nbutton has been clicked!!!!")
        obj = self.id
        print(self.patient_id, 'obj')
        return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'You are Gorgeous',
                    # 'img_url': '/web/image/%s/%s/image_1024' % (self.team_id.user_id._name, self.team_id.user_id.id)
                    # if self.team_id.user_id.image_1024 else '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                    }
                }

# status bar buttons
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

# for One2many field


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id= fields.Many2one('product.product', required=True)
    price_unit= fields.Float(related="product_id.list_price")
    qty= fields.Integer(string='Quantity', default=1)

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')



