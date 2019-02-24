from app import db
from app.models import User, Post

users = User.query.all()

for u in users:
    print(u.id, u.username)