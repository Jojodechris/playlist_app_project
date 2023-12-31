# forms.py file

"""Forms for playlist app."""

from wtforms import StringField,SelectField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):

    """Form for adding playlists."""
    name= StringField("Name", validators=[InputRequired()])
    description=StringField("Description", validators=[InputRequired()])

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title=StringField("Title", validators=[InputRequired()])
    artist=StringField("Artist", validators=[InputRequired()])

    # Add the necessary code to use this form

# def coerce_int(x):
#     return x[0]

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add')
