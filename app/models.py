from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    upvotes = db.relationship('UpVote',backref = 'user',lazy = "dynamic")
    downvotes = db.relationship('DownVote',backref = 'user',lazy = "dynamic")
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        
        return comments
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        print(self.password_hash)
        print(password)
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f'User {self.username}'
    
class Pitch(db.Model):
    
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    upvotes = db.relationship('UpVote',backref = 'pitch',lazy = "dynamic")
    downvotes = db.relationship('DownVote',backref = 'pitch',lazy = "dynamic")
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,pitch_category):
        pitches = Pitch.query.filter_by(pitch_category = pitch_category).all()
        return pitches

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(id=id).first()

        return pitch 
    
class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comments= db.Column(db.String)
    pitch_id = db.Column(db.Integer)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
class UpVote(db.Model):
    
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key = True)
    upvote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_votes(self):
        db.session.add(self)
        db.session.commit()
    
    def add_upvotes(cls, id):
        upvote_pitch = Upvote(user=current_user, pitch_id=id)
        upvote_pitch.save_upvotes()

    @classmethod
    def get_upvotes(cls, id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote

    @classmethod
    def get_all_upvotes(cls, pitch_id):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes
    
class DownVote(db.Model):
    
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_votes(self):
        db.session.add(self)
        db.session.commit()
    
    def add_downvotes(cls, id):
        downvote_pitch = Downvote(user=current_user, pitch_id=id)
        downvote_pitch.save_downvotes()

    @classmethod
    def get_downvotes(cls, id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    @classmethod
    def get_all_downvotes(cls, pitch_id):
        downvotes = Downvote.query.order_by('id').all()
        return downvotes