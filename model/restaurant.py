from marshmallow import Schema, fields
from model.entree import EntreeSchema

class Restaurant():
  def __init__(self, id, name, city, parking, rating):
    self.id = id
    self.name = name
    self.city = city
    self.parking = parking
    self.rating = rating
    self.menu = []

  def __repr__(self):
    return '<Restaurant(name={self.name!r})>'.format(self=self)

  def addEntree(self, entree):
    self.menu.append(entree)

  

class RestaurantSchema(Schema):
  id = fields.Number()
  name = fields.Str()
  city = fields.Str()
  parking = fields.Boolean()
  rating = fields.Number()
  menu = fields.Nested(EntreeSchema, many=True)
