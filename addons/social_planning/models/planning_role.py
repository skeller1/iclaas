from odoo import models, fields

from random import randint

class PlanningRole(models.Model):
    _name = 'planning.role'
    _description = 'Planning role'
    _order = 'sequence, id'


    def _default_color(self):
        return "#FF0000"

    active = fields.Boolean('Active', default=True)
    name = fields.Char(string='Role Name', required=True, translate=True)
    description = fields.Text(translate=True)
    sequence = fields.Integer(default=1)
    employee_ids = fields.Many2many('hr.employee', 'employee_planning_role_rel', 'planning_role_id', 'emp_id', string='Employees',
        )

    color = fields.Char(
    string='Color Index', default=lambda self: self._default_color(),
    help='Social planning role color.')


    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Social planning role name already exists!"),
    ]
