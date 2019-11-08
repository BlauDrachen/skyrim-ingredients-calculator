from . import db


class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    effect_id1 = db.Column(db.Integer, db.ForeignKey('effects.id'))
    effect_id2 = db.Column(db.Integer, db.ForeignKey('effects.id'))
    effect_id3 = db.Column(db.Integer, db.ForeignKey('effects.id'))
    effect_id4 = db.Column(db.Integer, db.ForeignKey('effects.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    value = db.Column(db.Integer),
    weight = db.Column(db.Float)
    

class Effect(db.Model):
    __tablename__ = 'effects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    is_dlc = db.Column(db.Boolean)
