from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = SelectField('Type',choices=[('Business','Business'), ('Software','Software')],validators=[Required()])
    title = StringField('Pitch title',validators=[Required()])
    about = TextAreaField('About Pitch')
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class CommentsForm(FlaskForm):
    comments = TextAreaField('Add your Comments', validators=[Required()])
    submit = SubmitField('Submit Comment')