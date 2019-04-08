#from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.

class URLInput(EmbeddedDocument):
    url = fields.StringField(required=True)

class Place(Document):
    name = fields.StringField(required=True)
    state = fields.StringField(required=True)
    country = fields.StringField(required=True)
    address = fields.StringField(required=False)
    latitude = fields.FloatField(required=True)
    longitude = fields.FloatField(required=True)
    photo_urls = fields.ListField(fields.EmbeddedDocumentField(URLInput))
    map_url = fields.StringField(required=True)
    description = fields.StringField(required=False)
    place_id = fields.StringField(required=True)


class Place2(Document):
    name = fields.StringField(required=True)
    state = fields.StringField(required=True)
    country = fields.StringField(required=True)
    address = fields.StringField(required=False)
    latitude = fields.FloatField(required=True)
    longitude = fields.FloatField(required=True)
    photo_urls = fields.ListField(required=False)
    map_url = fields.StringField(required=True)
    description = fields.StringField(required=False)
    place_id = fields.StringField(required=True)
    place_type = fields.ListField(required=True)

    meta = {'indexes': [
        {'fields': ['$name', "address"],
         'default_language': 'english',
         'weights': {'name': 10, 'address': 2}
        }
    ]}