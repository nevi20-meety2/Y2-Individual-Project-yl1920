from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


# replace lecture.db with your own database file
engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))


def add_user(Fname,Lname,username,password,media,song,favmember,favalbum,opinion):
	user_object = User(Fname=Fname,Lname=Lname,
		username=username,password=password,media=media
		,song=song,favmember=favmember,favalbum=favalbum,opinion=opinion)
	session.add(user_object)
	session.commit()

def qurey_users():
	return session.query(User).all()

def query_user(username):
	return session.query(User).filter_by(username=username).first()

def checkUser(username,password):
	user = query_user(username)
	if password == user.password:
		return True
	else:
		return False

#print(qurey_users())
#print(checkUser('f','f'))
print(qurey_users())