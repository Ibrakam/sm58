from sqlalchemy import (Column, String, Integer, ForeignKey,
                        DateTime, BigInteger, Boolean, Text)

from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


# модель User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    age = Column(String, nullable=True)
    city = Column(String, nullable=True)
    reg_date = Column(DateTime, default=datetime.now())


# модель UserPost
class UserPost(Base):
    __tablename__ = "userposts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # 1
    main_text = Column(String, nullable=False)
    hashtag = Column(String, ForeignKey("hashtags.hashtag_text"))
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy="subquery")  # {"id": 1, "username": "saddsa"}
    hashtag_fk = relationship("Hashtag", lazy="subquery")


# модель PostPhoto
class PostPhoto(Base):
    __tablename__ = 'postphoto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('userposts.id'))
    photo_file = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now)

    post_fk = relationship(UserPost, lazy='subquery')


# модель Comment
class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('userposts.id'))
    text = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')


# модель Hashtag
class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hashtag_text = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())
