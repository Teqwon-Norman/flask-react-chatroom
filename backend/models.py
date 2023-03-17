from exts import db

"""
class Recipe:
    id: int primary key
    title: str 
    description: str (text)
"""

class Recipe(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, new_name=None, new_pass=None):
        if new_name: 
            self.user_name = new_name
        if new_pass: 
            self.password = new_pass