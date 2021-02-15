from odoo import models, fields, api

from random import randint

class PlanningSlot(models.Model):
    _name = 'planning.slot'
    _description = 'Shift'

    _order = 'start_datetime,id desc'

    def _default_color(self):
        return '#'+ format(randint(0,16777215),'x')

    company_id = fields.Many2one(
        'res.company',required=True, default=lambda self: self.env.company
    )
    display_name = fields.Char(string='Display Name', translate=True)
    description = fields.Text(translate=True)
    allocated_hours = fields.Float('Allocated Hours')
    html_description = fields.Html(string='HTML Description')

    role_id = fields.Many2one('planning.role', required=True)
    start_datetime = fields.Datetime(help='Date when shift started', default=fields.Datetime.now)
    end_datetime = fields.Datetime(help='Date when shift ended', default=fields.Datetime.now)
    project_id = fields.Many2one('project.project')
    task_id = fields.Many2one('project.task')
    employee_id = fields.Many2one('hr.employee')
    manager_id = fields.Many2one('hr.employee', related="employee_id.parent_id")
    color = fields.Char(
        string='Color Index',
        default=lambda self: self._default_color(),
        related='role_id.color',
        help='Social planning role color.')

    template_id = fields.Many2one('planning.slot.template', readonly=True)

    @api.model
    def get_templates(self):
        return self.env['planning.slot.template'].search([])

    #template_autocomplete_ids = fields.Many2many('planning.slot.template', default=get_templates)
    # all records passed the test, don't return anything
    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', "Social planning role name already exists!"),
    # ]

    def name_get(self):
        return [(record.id, record.display_name) for record in self]


    @api.constrains('display_name')
    def set_display_name(self):
        if not self.display_name:
            self.display_name = self.role_id.display_name
    # @api.onchange('template_id')
    # def change_template_id(self):
    #     self.role_id = self.template_id.role_id
    #     #self.start_datetime = self.template_id.start_time
