import pytube
from flask_table import Table, Col
from flask_wtf import FlaskForm
from wtforms import form, StringField
from wtforms.validators import DataRequired
from flask_table import Table, Col


class SearchForm(FlaskForm):
    url = StringField('Give me the sauce plz', [DataRequired()])


class StreamTable(Table):
    itag = Col('iTag')
    res = Col('Resolution')
    abr = Col('Average Bitrate')
    video_codec = Col('Video Codec')
    audio_codec = Col('Audio Codec')
    filesize = Col('File Size')
