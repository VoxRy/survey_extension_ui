# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Survey Extension: UI Improvements",
    "version": "15.0.1.0.0",
    "category": "Marketing/Surveys",
    "summary": "Adds 'Note' question type and 'Display as Dropdown' option to Surveys.",
    "author": "Kais Akram",
    "license": "LGPL-3",
    "depends": ["survey"],
    "data": [
        "views/survey_question_views.xml",
        "views/survey_question_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "survey_extension_ui/static/src/css/survey_ui.css",
            "survey_extension_ui/static/src/js/survey_form.js",
        ],
    },
    "installable": True,
    "application": False,
}
