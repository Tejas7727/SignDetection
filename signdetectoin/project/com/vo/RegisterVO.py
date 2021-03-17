import wtforms

class RegisterVO:
    register_loginId = wtforms.IntegerField
    registerFirstName = wtforms.StringField
    registerLastName = wtforms.StringField
    registerContact = wtforms.StringField
    registerAddress = wtforms.StringField