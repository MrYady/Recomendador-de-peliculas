from wtforms import Form
from wtforms import StringField, TextAreaField

class CommentForm(Form):
    peli = StringField('pelicula')
    R_peli = TextAreaField('Recomendacion')