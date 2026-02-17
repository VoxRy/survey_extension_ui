# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SurveyQuestion(models.Model):
    """ Inherit survey.question to add display customization. """
    _inherit = 'survey.question'

    question_type = fields.Selection(
        selection_add=[('note', 'Bilgi Notu / Metin Bloğu')],
        ondelete={'note': 'cascade'})
