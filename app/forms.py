from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,RadioField, SelectField, BooleanField, SubmitField, PasswordField, IntegerField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, Length, Email, URL


class LevelUserForm(FlaskForm):
	nama 		      = StringField('Nama:')
	submit 		   = SubmitField('Kirim')


class UserForm(FlaskForm):
   level_id       = RadioField('Level Id',
      choices     =[('user','User'),('admin','Admin')])
   username       = StringField('User Name:',
      validators  =[Required('Nama harus diisi.'), Length(max=25)])
   email          = StringField('Email:',
      validators  =[Required('Email harus diisi.'), Email('Alamat email tidak ditulis dengan benar.')])
   password       = PasswordField('Password:',
      validators  =[Required('Password harus diisi'), Length(min=8)])
   no_telp        = StringField('No Telpon: ',
      validators  =[Required('No Telpon harus diisi'),Length(max=15)])
   alamat         = StringField('Alamat : ',
      validators  =[Required('Alamat harus diisi'),Length(max=25)])
   submit         = SubmitField('kirim')


class PelangganForm(FlaskForm):
   nama       	  = StringField('Nama',
      validators  =[Required('Nama harus diisi.'), Length(max=50)])
   alamat         = StringField('Alamat:',
      validators  =[Required('Nama harus diisi.'), Length(max=50)])
   daya           = StringField('Daya:',
      validators  =[Required('Email harus diisi.'), Length(max=25)])
   submit         = SubmitField('Simpan')


class TemuanForm(FlaskForm):
   tindakan       = StringField('Tindakan',
      validators  =[Required('Tindakan harus di isi.'), Length(max=100)])
   ket            = StringField('Alamat:',
      validators  =[Required('Keterangan harus di isi.'), Length(max=100)])
   submit         = SubmitField('Kirim')


class LoginForm(FlaskForm):
   username       = StringField('User Name: ',
      validators  =[Required('Username harus di isi.'), Length(max=100)])
   password       = StringField('Password:',
      validators  =[Required('Password harus di isi.'), Length(min=5, max=100)])
   submit         = SubmitField('Kirim')