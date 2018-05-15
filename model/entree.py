from marshmallow import Schema, fields

class Entree():
  def __init__(self, id, name, cuisine, dinner):
    self.id = id
    self.name = name
    self.cuisine = cuisine
    self.dinner = dinner

  def __repr__(self):
    return '<Entree(name={self.name!r})>'.format(self=self)


class EntreeSchema(Schema):
  id = fields.Number()
  name = fields.Str()
  cuisine = fields.Str()
  dinner = fields.Boolean()
