from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField
from wtforms.validators import InputRequired
# from wtforms.validators import DataRequired

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class ShuffleThemesForm(FlaskForm):

    list_of_days = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # create a list of value/description tuples
    days = [(x, x) for x in list_of_days]
    example = MultiCheckboxField('Label', choices=days, validators=[InputRequired()])