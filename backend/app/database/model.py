import bcrypt
from app.database.db_init import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(256))

    sessions = db.relationship('Sessions', backref='user', lazy=True)

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password_hash = self.set_password(password)

    def __repr__(self):
        return '<User(id: %r)> ' % (self.id)
    
    def set_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    @staticmethod
    def get_users():
        return User.query.all()
    

class Sessions(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    videos = db.relationship('Video', backref='session', lazy=True)
    session_content = db.relationship('SessionContent', backref='session', lazy=True)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<Sessions(user_id: %r)> ' % (self.user_id)

    
class SessionContent(db.Model):
    __tablename__ = 'session_content'
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.Integer)
    content = db.Column(db.String(None))
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'), nullable=False)

    def __init__(self, sequence, content, session_id):
        self.sequence = sequence
        self.content = content
        self.session_id = session_id

    def __repr__(self):
        return '<SessionContent(seq: %r, content: %r)>' % (self.sequence, self.content)


class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(None))
    start = db.Column(db.Float)
    end = db.Column(db.Float)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'), nullable=False)

    def __init__(self, video_id, start, end, session_id):
        self.video_id = video_id
        self.start = start
        self.end = end
        self.session_id = session_id

    def __repr__(self):
        return '<Video(video_id: %r)>' % (self.video_id)
    

class MainFunc:
    def create(obj):
        db.session.add(obj)
        db.session.commit()

    def get_all(obj):
        return obj.query.all()
    
    def get(obj, **kwargs):
        return obj.query.filter_by(**kwargs).first() 
    
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def update(obj, **kwargs):
        for attr, value in kwargs.items():
            setattr(obj, attr, value)
        db.session.commit()