from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    # add relationship
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    # add serialization rules
    serialize_rules = ('-hero_powers.hero',)
    
def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'hero_powers': [{
                'id': hp.id,
                'hero_id': hp.hero_id,
                'strength': hp.strength,
                'power': {
                    'id': hp.power.id,
                    'name': hp.power.name,
                    'description': hp.power.description
                }
            } for hp in self.hero_powers]
        }

def __repr__(self):
        return f'<Hero {self.id}>'


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    # add relationship
    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')
    heroes = association_proxy('hero_powers', 'hero')

    # add serialization rules
    serialize_rules = ('-hero_powers.power',)

    # add validation
    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("name must be 20 characters long")
        return value

    def __repr__(self):
        return f'<Power {self.id}>'


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)   
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    # add relationships
    hero = db.relationship('Hero', back_populates='powers')
    power = db.relationship('Power', back_populates='heroes')
    power_name = association_proxy('power', 'name')

    # add serialization rules
    serialize_rules = ('-hero.hero_powers', '-power.heroes')


    # add validation
    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['low', 'medium', 'high']:
            raise ValueError("Strength must be 'low', 'medium', or 'high'")
        return value   

    def __repr__(self):
        return f'<HeroPower {self.id}>'
