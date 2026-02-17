odoo.define('survey_extension_ui.form', function (require) {
    'use strict';

    var SurveyForm = require('survey.form');

    SurveyForm.include({
        /**
         * Overridden to collect answer from dropdown.
         * Signature: (params, $parent, questionId)
         * - params: the data object being build for submission
         * - $parent: the jQuery element with data-question-type
         * - questionId: the ID of the question
         */
        _prepareSubmitChoices: function (params, $parent, questionId) {
            var $dropdown = $parent.find('select.o_survey_form_choice_item');
            if ($dropdown.length > 0) {
                var val = $dropdown.val();
                if (val && val !== '-1') {
                    // Standard Odoo method to add single/multiple choice answer
                    params = this._prepareSubmitAnswer(params, questionId, val);
                }
                // Also check for comments (standard survey feature)
                params = this._prepareSubmitComment(params, $parent, questionId, false);
                return params;
            }
            return this._super.apply(this, arguments);
        }
    });
});
