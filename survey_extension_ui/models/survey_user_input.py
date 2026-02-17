# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    def save_lines(self, question, answer, comment=None):
        """ Overridden to skip saving for 'note' question type. """
        if question.question_type == 'note':
            return
        return super(SurveyUserInput, self).save_lines(question, answer, comment)
