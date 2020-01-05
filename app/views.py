from flask import render_template, url_for, redirect, request, session, escape
from app import app
from flask import render_template
from app.forms import UserForm, PelangganForm
from app.models import Level, User, Pelanggan, Target, Temuan, Buku
from flask_login import login_required
from flask_bootstrap import Bootstrap 


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
Bootstrap(app)
'''
@app.route("/")
def index():
	return 'okebos'
'''
def index():
    return redirect(url_for('login'))

def ValidasiLogin(Form):
  if Form:
    DataUser=User.query.filter_by(username=Form['username'],password=Form['password']).first()
    if DataUser:
      session['user'] = {'username':DataUser.username,'id':DataUser.id}
      return {'error' : False, 'username':DataUser.username}
    else:
      return {'error' : True}

@app.route("/")
@app.route("/login",methods=['POST','GET'])
def login():
  session.pop('user', None)
  validasi = ValidasiLogin(request.form)
  if request.method == 'POST':
    if validasi['error'] == False:
      return redirect(url_for('home'))
    return 'login gagal'
  return render_template("login.html")

@app.route("/home")
def home():
	if 'user' not in session:
		return render_template('login.html')

	DataUser = {
		'id': escape(session['user']['id']),
		'username' : escape(session['user']['username'])
	}

	return render_template('admin_home.html')

@app.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
	return render_template("dashboard.html")
'''
@app.route("/level", methods=['POST', 'GET'])
def level():
    if request.method == 'POST':
        nama       = request.form['nama']
        AddUser = Level(nama=nama)
        db.session.add(AddUser)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template("register.html")
'''
#halaman untuk tambah user
@app.route('/register', methods=['GET', 'POST'])
def register():
   form = UserForm(request.form)
   if request.method == 'POST':
      if form.validate():
        level_id = form.level_id.data
        username = form.username.data
        email    = form.email.data
        password = form.password.data
        no_telp  = form.no_telp.data
        alamat   = form.alamat.data
        AddUser  = User(username=username, email=email, password=password, no_telp=no_telp,alamat=alamat,level_id=level_id)
        db.session.add(AddUser)
        db.session.commit()
        return 'Data suda tersimpan'
      else:
         # mengambil daftar kesalahan yang muncul
         # pada saat proses validasi
         errors = form.errors.items()         
         return render_template('register.html',form=form, errors=errors)
   return render_template('register.html', form=form)


@app.route('/pelanggan', methods=['GET', 'POST'])
def pelanggan():
   form = PelangganForm(request.form)
   if request.method == 'POST':
      if form.validate():
        nama          = form.nama.data
        alamat        = form.alamat.data
        daya          = form.daya.data
        AddPelanggan  = Pelanggan(nama=nama, alamat=alamat, daya=daya)
        db.session.add(AddPelanggan)
        db.session.commit()
        return 'Data suda tersimpan'
      else:
         # mengambil daftar kesalahan yang muncul
         # pada saat proses validasi
         errors = form.errors.items()         
         return render_template('pelanggan.html',form=form, errors=errors)
   return render_template('pelanggan.html', form=form)


@app.route('/tampil',methods=['GET', 'POST'])
def tampil():
  return render_template('tampil.html', container = User.query.all())

@app.route('/tampilpelanggan',methods=['GET', 'POST'])
def tampil_pelanggan():
  return render_template('tampilpelanggan.html', container = Pelanggan.query.all())

@app.route("/about")
def about():
    return 'halaman about'


@app.route('/ubah/<id>', methods=['GET', 'POST'])
def ubah(id):
	user= User.query.filter_by(id=id).first()
	if request.method == 'POST':
		user.id = request.form['id']
		#DataUser.level_id = request.form['level_id']
		user.username = request.form['username']
		user.no_telp = request.form['no_telp']
		user.alamat = request.form['alamat']
		user.email = request.form['email']
		#Data=User(level_id,username,no_telp,alamat,email)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('index'))
	else:
		return render_template('ubah_form.html', user=user)


@app.route('/hapus/<int:id>', methods=['GET', 'POST'])
def hapus(id):
	dataUser= User.query.filter_by(id=id).first()
	db.session.delete(dataUser)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/de/<int:id>', methods=['GET', 'POST'])
def de(id):
	dataUser= User.query.filter_by(id=id).first()
	db.session.delete(dataUser)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/bukuu')
def bukuu():   
   return render_template('index.html', container=Buku.query.all())

@app.route('/tambahbukuu', methods=['GET','POST'])
def tambahbukuu():
   if request.method == 'POST':
      id = request.form['id']
      judul = request.form['judul']
      penulis = request.form['penulis']
      penerbit = request.form['penerbit']
      buku = Buku(id=id, judul=judul, penulis=penulis, penerbit=penerbit)
      db.session.add(buku)
      db.session.commit()
      return redirect(url_for('bukuu'))
   else:
      return render_template('tambah_formbukuu.html')

@app.route('/tambah', methods=['GET','POST'])
def tambah():
   if request.method == 'POST':
      id = request.form['id']
      judul = request.form['judul']
      penulis = request.form['penulis']
      penerbit = request.form['penerbit']
      buku = Buku(id, judul, penulis, penerbit)
      db.session.add(buku)
      db.session.commit()
      return redirect(url_for('index'))
   else:
      return render_template('tambah_form.html')


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
    