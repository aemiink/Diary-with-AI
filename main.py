# İçe aktar
from flask import Flask, render_template,request, redirect
# Veri tabanı kitaplığını bağlama
from flask_sqlalchemy import SQLAlchemy
#speech.py içerisinden speech fonksiyonu içeri aktardık.
from speech import speechlan


app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma

class Card(db.Model):
    # Sütun oluşturma
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Başlık
    title = db.Column(db.String(100), nullable=False)
    # Tanım
    subtitle = db.Column(db.String(300), nullable=False)
    # Metin
    text = db.Column(db.Text, nullable=False)

    # Nesnenin ve kimliğin çıktısı
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Ödev #2. Kullanıcı tablosunu oluşturun
class User(db.Model):
    #autoincrement=True özelliği, veritabanı tablolarında otomatik olarak artan bir sayısal değer atamak için kullanılan bir mekanizmadır. 
    # Bu sayede, her yeni eklenen satıra benzersiz bir kimlik numarası (ID) verilir.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # E-Posta 
    address = db.Column(db.String(100), nullable=False)
    #Şifre
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f'<Card {self.id}>'


# İçerik sayfasını çalıştırma
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Ödev #4. yetkilendirmeyi uygulamak
            users_db = User.query.all()
            for user in users_db:
                if form_login == user.address and form_password == user.password:
                    return redirect('/index')
                else:
                    error = "Hatalı Giriş Yaptınız!"
            return render_template('login.html', error=error)
        else:
            return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login= request.form['email']
        password = request.form['password']
        
        #Ödev #3 Kullanıcı verilerinin veri tabanına kaydedilmesini sağlayın
        user = User(address = login, password = password)
        db.session.add(user)
        db.session.commit()

        return redirect('/')
    
    else:    
        return render_template('registration.html')


# İçerik sayfasını çalıştırma
@app.route('/index')
def index():
    # Veri tabanı girişlerini görüntüleme
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Kayıt sayfasını çalıştırma
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Giriş oluşturma sayfasını çalıştırma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Ses kaydı alma
@app.route('/record')
def record():
    try:
        text = speechlan("tr-TR")
    except:
        text = "Bir şeyler yanlış gitti, tekrar deneyin..."
    return render_template('create_card.html', text=text)

# Ses kaydı alma
@app.route('/recorden')
def recorden():
    try:
        text = speechlan("en-GB")
    except:
        text = "Sonthing is wrong... Please try again..."
    return render_template('create_card.html', text=text)

# Giriş formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Veri tabanına gönderilecek bir nesne oluşturma
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')





if __name__ == "__main__":
    app.run(debug=True)
