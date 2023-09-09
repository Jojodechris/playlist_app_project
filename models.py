# models.py file 

"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'my-playlist'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.Text, nullable=False)
    description=db.Column(db.Text, nullable=False)
    # song_id=db.Column(db.Integer, db.ForeignKey('my-song.id'))

    song = db.relationship('Song', primaryjoin='Playlist.id == foreign(Song.id)')

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""
    __tablename__ = 'my-song'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.Text, nullable=False)
    artist=db.Column(db.Text, nullable=False)
    # playlist_id=db.Column(db.Integer, db.ForeignKey('my-playlist.id'))
    playlist = db.relationship('Playlist', primaryjoin='Song.id == foreign(Playlist.id)')

    # Define the relationship to playlists
    # playlists = db.relationship('Playlist', secondary='playlist_song', back_populates='songs')


 

    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlist-song'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id=db.Column(db.Integer, db.ForeignKey('my-playlist.id'))
    song_id=db.Column(db.Integer, db.ForeignKey('my-song.id'))
#     # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
