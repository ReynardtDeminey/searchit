from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField,IntegerField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    username = StringField('Username', render_kw={"placeholder": "Username"})
    subreddit = StringField('Subreddit', render_kw={"placeholder": "Subreddit"})
    num_of_records = IntegerField('Number of Records', render_kw={"placeholder": "Number of Records"})
    choice = SelectField('Post', choices=[('post', 'Post'), ('comment', 'Comment')])
    query = StringField('Search Term', render_kw={"placeholder": "Search term"})
    submit = SubmitField('Search')