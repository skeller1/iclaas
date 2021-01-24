from odoo import models, fields

from random import randint

class PlanningSlot(models.Model):
    _name = 'planning.slot'
    _description = 'Shift'

    def _default_color(self):
        return '#'+ format(randint(0,16777215),'x')

    company_id = fields.Many2one(
        'res.company',required=True, default=lambda self: self.env.company
    )
    display_name = fields.Char(string='Display Name', translate=True)
    description = fields.Text(translate=True)
    allocated_hours = fields.Float('Allocated Hours')
    html_description = fields.Html(string='HTML Description')

    role_id = fields.Many2one('planning.role')
    start_datetime = fields.Datetime(help='Date when shift started', default=fields.Datetime.now)
    end_datetime = fields.Datetime(help='Date when shift ended', default=fields.Datetime.now)
    project_id = fields.Many2one('project.project')
    task_id = fields.Many2one('project.task')
    employee_id = fields.Many2one('hr.employee')
    manager_id = fields.Many2one('hr.employee', related="employee_id.parent_id")
    color = fields.Char(
        string='Color Index', default=lambda self: self._default_color(),
        help='Social planning role color.')

    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', "Social planning role name already exists!"),
    # ]
