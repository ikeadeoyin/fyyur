from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)



#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.ARRAY(db.String()))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String())
    shows = db.relationship("Show", backref="venue", cascade="all, delete")

    def __init(self,name, city,  state, address, phone, image_link, facebook_link, genres, seeking_talent, seeking_description, website_link):
      self.name = name
      self.city = city
      self.state = state
      self.address = address
      self.phone = phone
      self.image_link = image_link
      self.facebook_link = facebook_link
      self.website_link = website_link
      self.genres = genres
      self.seeking_talent = seeking_talent
      self.seeking_description = seeking_description

    def __repr__(self):
      return f"<Venue {self.id} {self.name} {self.city} {self.state} {self.genres} {self.website_link} {self.seeking_talent}>"

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    # genres = db.Column(db.String())
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String())
    shows = db.relationship("Show", backref="artist", cascade="all, delete")

    def __init(self,name, city,  state, phone, image_link, facebook_link, genres, seeking_venue, seeking_description, website_link):
      self.name = name
      self.city = city
      self.state = state
      self.phone = phone
      self.image_link = image_link
      self.facebook_link = facebook_link
      self.website_link = website_link
      self.genres = genres
      self.seeking_venue = seeking_venue
      self.seeking_description = seeking_description

    def __repr__(self):
       return f"<Artist {self.id} {self.name} {self.city}>"

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
  __tablename__ = "Show"

  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey("Artist.id"), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey("Venue.id"), nullable=False)
  start_time = db.Column(db.DateTime, nullable=False)

  def __init__(self,artist_id, venue_id, start_time):
    self.artist_id = artist_id
    self.venue_id = venue_id
    self.start_time = start_time


  def __repr__(self):
      return f"<Show {self.id} {self.artist_id} {self.venue_id}>"
