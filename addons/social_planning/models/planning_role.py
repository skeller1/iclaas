from odoo import models, fields

from random import randint

class PlanningRole(models.Model):
    _name = 'planning.role'
    _description = 'Planning role'
    _order = 'sequence, id'


    def _default_color(self):
        random_number = randint(0,16777215)
        return '#'+ format(random_number,'x')

    active = fields.Boolean('Active', default=True)
    company_id = fields.Many2one('res.company',required=True)
    sequence = fields.Integer(default=1)

    name = fields.Char(string='Role Name', required=True, translate=True)
    description = fields.Text(translate=True)
    html_description = fields.Html(string='HTML Description')
    employee_ids = fields.Many2many('hr.employee', 'employee_planning_role_rel', 'planning_role_id', 'emp_id', string='Employees',
        )

    color = fields.Char(
    string='Color Index', default=lambda self: self._default_color(),
    help='Social planning role color.')


    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Social planning role name already exists!"),
    ]
