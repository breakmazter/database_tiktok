__all__ = ('Author', 'Video', 'Tag', 'Song', 'ParentComment', 'ChildComment', 'VideoTag')

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table
from sqlalchemy.sql import func

from settings import *

Base = declarative_base()
engine = create_engine(POSTGRES_URL, echo=True)


VideoTag = Table('video_tag', Base.metadata,
                 Column('video_id', Integer, ForeignKey('video.id'), primary_key=True),
                 Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True))


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)

    # you mean tik tok id? it's better to rename. id is not unique)?
    unique_id = Column(String)
    nickname = Column(String)
    signature = Column(String)
    avatar_image = Column(String)
    follower_count = Column(Integer)
    following_count = Column(Integer)
    heart_count = Column(Integer)
    video_count = Column(Integer)
    relation = Column(Integer)
    bio_link = Column(String)
    is_verified = Column(Boolean)
    is_private = Column(Boolean)
    is_commerce = Column(Boolean)

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())

    videos = relationship('Video', back_populates='author')
    parent_comments = relationship('ParentComment', back_populates='author')
    child_comments = relationship('ChildComment', back_populates='author')

    def __repr__(self):
        return f"<Author([{self.id}], [{self.unique_id}])>"


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)

    author_id = Column(ForeignKey('author.id'))
    song_id = Column(ForeignKey('song.id'))

    view_count = Column(Integer)
    heart_count = Column(Integer)
    comment_count = Column(Integer)
    repost_count = Column(Integer)
    height = Column(Integer)
    width = Column(Integer)
    duration = Column(Integer)
    ratio = Column(String)
    format = Column(String)
    encoded_type = Column(String)
    description = Column(String)
    video_sticker_text = Column(String)
    preview_image = Column(String)
    is_ad = Column(Boolean)
    is_stitch_enabled = Column(Boolean)

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())

    author = relationship('Author', back_populates='videos')
    tags = relationship('Tag', secondary=VideoTag, back_populates='videos')
    parent_comments = relationship('ParentComment', back_populates='video')
    song = relationship('Song', back_populates='videos')

    def __repr__(self):
        return f"<Video([{self.id}], [{self.author_id}], [{self.description}])>"


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)

    name_tag = Column(String)
    description = Column(String)
    view_count = Column(Integer)
    is_commerce = Column(Boolean)

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())

    videos = relationship('Video', secondary=VideoTag, back_populates='tags')

    def __repr__(self):
        return f"<Tag([{self.id}], [{self.name_tag}])>"


class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)

    title = Column(String)
    author_name = Column(String)
    album = Column(String)
    song_image = Column(String)
    song_link = Column(String)
    duration = Column(Integer)
    video_count = Column(Integer)
    is_original = Column(Boolean)

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())

    videos = relationship('Video', back_populates='song')

    def __repr__(self):
        return f"<Song([{self.id}], [{self.title}])>"


class ParentComment(Base):
    __tablename__ = 'parent_comment'

    id = Column(Integer, primary_key=True)

    author_id = Column(Integer, ForeignKey('author.id'))
    video_id = Column(Integer, ForeignKey('video.id'))

    comment_text = Column(String)
    heart_count = Column(Integer)
    is_child_comments = Column(Boolean)
    child_comment_count = Column(Integer)

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())

    video = relationship('Video', back_populates='parent_comments')
    child_comments = relationship('ChildComment', back_populates='parent_comment')
    author = relationship('Author', back_populates='parent_comments')

    def __repr__(self):
        return f"<ParentComment([{self.id}], [{self.video_id}])>"


class ChildComment(Base):
    __tablename__ = 'child_comment'

    id = Column(Integer, primary_key=True)

    author_id = Column(Integer, ForeignKey('author.id'))
    parent_id = Column(Integer, ForeignKey('parent_comment.id'))

    comment_text = Column(String)
    heart_count = Column(Integer)

    created_at = Column(DateTime, server_default=func.now())
    modified_at = Column(DateTime, onupdate=func.now())

    author = relationship('Author', back_populates='child_comments')
    parent_comment = relationship('ParentComment', back_populates='child_comments')

    def __repr__(self):
        return f"<ChildComment([{self.id}], [{self.parent_id}])>"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
