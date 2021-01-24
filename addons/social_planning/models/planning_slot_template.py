from odoo import models, fields

class PlanningSlotTemplate(models.Model):
    _name = 'planning.slot.template'
    _description = 'Shift Template'

    company_id = fields.Many2one(
        'res.company',required=True, default=lambda self: self.env.company
    )
    display_name = fields.Char(string='Display Name', required=True, translate=True)
    description = fields.Text(translate=True)
    duration = fields.Float('Duration', required=True)
    html_description = fields.Html(string='HTML Description')

    project_id = fields.Many2one('project.project')
    role_id = fields.Many2one('planning.role')
    start_time = fields.Float('Start Time', required=True)
    task_id = fields.Many2one('project.task')

    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', "Social planning role name already exists!"),
    # ]
