#from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.

class URLInput(EmbeddedDocument):
    url = fields.StringField(required=True)

class Place(Document):
    name = fields.StringField(required=True)
    state = fields.StringField(required=True)
    country = fields.StringField(required=True)
    latitude = fields.FloatField(required=True)
    longitude = fields.FloatField(required=True)
    photo_urls = fields.ListField(fields.EmbeddedDocumentField(URLInput))
    map_url = fields.StringField(required=True)
    description = fields.StringField(required=True)