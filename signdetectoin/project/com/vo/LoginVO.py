import wtforms


class LoginVO:
    loginEmail = wtforms.StringField
    loginPassword = wtforms.StringField
    loginRole = wtforms.StringField

