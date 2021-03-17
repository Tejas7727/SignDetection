import wtforms


class DatasetVO:
    datasetId = wtforms.IntegerField
    datasetName = wtforms.StringField
    datasetPath = wtforms.StringField
    datasetDescription = wtforms.StringField
