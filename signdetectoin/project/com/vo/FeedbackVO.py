import wtforms

class FeedbackVO:
    feedbackID = wtforms.IntegerField
    feedbackRating = wtforms.IntegerField
    feedbackDescription = wtforms.StringField
    feedbackTo = wtforms.IntegerField
    feedbackFrom = wtforms.IntegerField
    feedbackDate = wtforms.DateField
    feedbackTime = wtforms.TimeField
    feedbackActiveStatus = wtforms.StringField