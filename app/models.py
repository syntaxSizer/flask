from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('post',backref='author', lazy='dynamic')


    def __repr__(self):
        return '<User %r>' % (self.nickname)


class post(db.Model):
      id = db.Column(db.Integer,primary_key = True)
      body = db.Column(db.String(140))
      timestamp = db.Column(db.DateTime)
      user_id = db.Column(db.Integer, db.ForeignKey('user_id'))
      
 
      def __repr__(self):
          return '<post %r>' % (self.body)
