import wtforms


class ComplaintVO:
    complaintId = wtforms.IntegerField
    complaintSubject = wtforms.StringField
    complaintDescription = wtforms.StringField
    complaintTo= wtforms.IntegerField
    complaintFrom = wtforms.IntegerField
    complaintDate = wtforms.DateField
    complaintTime = wtforms.TimeField
    complaintStatus = wtforms.StringField
    complaintActiveStatus = wtforms.StringField
    complaintReply = wtforms.StringField