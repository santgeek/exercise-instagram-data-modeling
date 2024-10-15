import os  
import sys  
import enum  
from sqlalchemy import Column, ForeignKey, Integer, String, Enum as SQLAlchemyEnum  
from sqlalchemy.orm import relationship, declarative_base  
from sqlalchemy import create_engine  
from eralchemy2 import render_er  

Base = declarative_base()  

class MediaType(enum.Enum):  
    IMAGE = "image"  
    VIDEO = "video"  
    AUDIO = "audio"   

class User(Base):  
    __tablename__ = 'user'    
    id = Column(Integer, primary_key=True)  
    username = Column(String(250), nullable=False, unique=True)  
    first_name = Column(String(250))  
    last_name = Column(String(250))  
    email = Column(String(250), unique=True)  

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):  
    __tablename__ = 'post'   
    id = Column(Integer, primary_key=True)    
    user_id = Column(Integer, ForeignKey('user.id'))  # Renamed for clarity  
    user = relationship(User)  

class Media(Base):  
    __tablename__ = 'media'    
    id = Column(Integer, primary_key=True)  
    type = Column(SQLAlchemyEnum(MediaType), nullable=False)  
    street_number = Column(String(250))  
    url = Column(String(250))  
    post_id = Column(Integer, ForeignKey('post.id'))  
    post = relationship(Post)  

class Comment(Base):  
    __tablename__ = 'comment'    
    id = Column(Integer, primary_key=True)  
    comment_text = Column(String(250))  
    author_id = Column(Integer, ForeignKey('user.id'))  
    post_id = Column(Integer, ForeignKey('post.id'))  
    user = relationship(User)  
    post = relationship(Post)  

    def to_dict(self):  
        return {  
            "id": self.id,  
            "comment_text": self.comment_text,  
            "author_id": self.author_id,  
            "post_id": self.post_id  
        }  # Example of meaningful representation  

# Draw from SQLAlchemy base  
try:  
    result = render_er(Base, 'diagram.png')  
    print("Success! Check the diagram.png file")  
except Exception as e:  
    print("There was a problem generating the diagram")  
    raise e  