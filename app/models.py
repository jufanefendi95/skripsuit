from datetime import datetime
from app import db

class Level(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    nama          = db.Column(db.String(50))

class User(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    level_id      = db.Column(db.String(4), db.ForeignKey('level.id'))
    username      = db.Column(db.String(50))
    password      = db.Column(db.Text)
    no_telp       = db.Column(db.Text)
    alamat        = db.Column(db.Text)
    email         = db.Column(db.Text)

class Pelanggan(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    nama          = db.Column(db.String(50))
    alamat        = db.Column(db.String(50))
    daya          = db.Column(db.String(50))

class Target(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('user.id'))
    pelanggan_id  = db.Column(db.Text)

class Temuan(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('user.id'))
    target_id     = db.Column(db.Integer, db.ForeignKey('target.id'))
    pelanggan_id  = db.Column(db.Integer, db.ForeignKey('pelanggan.id'))
    tindakan      = db.Column(db.Text)
    ket           = db.Column(db.Text)
    tgl           = db.Column(db.DateTime)

class Buku(db.Model):
   id = db.Column(db.String(4), primary_key=True)
   judul = db.Column(db.String(40), unique=True)
   penulis = db.Column(db.String(25))
   penerbit = db.Column(db.String(30))
