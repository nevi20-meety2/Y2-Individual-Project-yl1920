from sqlalchemy import Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import create_engine

Base= declarative_base()

class User(Base):
	__tablename__ ='users'
	id_table = Column(Integer,primary_key=True)
	Fname = Column(String)
	Lname = Column(String)
	username = Column(String)
	password = Column(String)
	media = Column(String)
	song = Column(String)
	favmember = Column(String)
	favalbum = Column(String)
	opinion = Column(String)

	def __repr__(self):
		return("first name:{}, \n"
			"last name:{}, \n"
			"username:{}, \n"
			"password:{}, \n"
			"media:{}, \n"
			"song:{}, \n"
			"favmember:{}, \n"
			"favalbum:{}, \n"
			"opinion:{}. \n"  
			).format(
			self.Fname,
			self.Lname,
			self.username,
			self.password,
			self.media,
			self.song,
			self.favmember,
			self.favalbum,
			self.opinion
			)