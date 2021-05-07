from sqlalchemy import insert
from db.models import *


def create_author(author_data: dict, db_session):
    try:
        author = Author(id=author_data['id'],
                        unique_id=author_data['unique_id'],
                        nickname=author_data['nickname'],
                        signature=author_data['signature'],
                        avatar_image=author_data['avatar_image'],
                        follower_count=author_data['follower_count'],
                        following_count=author_data['following_count'],
                        heart_count=author_data['heart_count'],
                        video_count=author_data['video_count'],
                        relation=author_data['relation'],
                        bio_link=author_data['bio_link'],
                        is_verified=author_data['is_verified'],
                        is_private=author_data['is_private'],
                        is_commerce=author_data['is_commerce'])
        db_session.add(author)
        db_session.flush()
    except Exception as e:
        db_session.rollback()
        raise e


def create_video(video_data: dict, db_session):
    try:
        video = Video(id=video_data['id'],
                      author_id=video_data['author_id'],
                      song_id=video_data['song_id'],
                      view_count=video_data['view_count'],
                      heart_count=video_data['heart_count'],
                      comment_count=video_data['comment_count'],
                      repost_count=video_data['repost_count'],
                      height=video_data['height'],
                      width=video_data['width'],
                      duration=video_data['duration'],
                      ratio=video_data['ratio'],
                      format=video_data['format'],
                      encoded_type=video_data['encoded_type'],
                      description=video_data['description'],
                      video_sticker_text=video_data['video_sticker_text'],
                      preview_image=video_data['preview_image'],
                      is_ad=video_data['is_ad'],
                      is_stitch_enabled=video_data['is_stitch_enabled'])
        db_session.add(video)
        db_session.flush()
    except Exception as e:
        db_session.rollback()
        raise e


def create_tag(tag_data: dict, db_session):
    try:
        tag = Tag(id=tag_data['id'],
                  name_tag=tag_data['name_tag'],
                  description=tag_data['description'],
                  view_count=tag_data['view_count'],
                  is_commerce=tag_data['is_commerce'])
        db_session.add(tag)
        db_session.flush()
    except Exception as e:
        db_session.rollback()
        raise e


def create_song(song_data: dict, db_session):
    try:
        song = Song(id=song_data['id'],
                    title=song_data['title'],
                    author_name=song_data['author_name'],
                    album=song_data['album'],
                    song_image=song_data['song_image'],
                    song_link=song_data['song_link'],
                    duration=song_data['duration'],
                    video_count=song_data['video_count'],
                    is_original=song_data['is_original'])
        db_session.add(song)
        db_session.flush()
    except Exception as e:
        db_session.rollback()
        raise e


def create_parent_comment(parent_comment_data: dict, db_session):
    try:
        parent_comment = ParentComment(id=parent_comment_data['id'],
                                       author_id=parent_comment_data['author_id'],
                                       video_id=parent_comment_data['video_id'],
                                       comment_text=parent_comment_data['comment_text'],
                                       heart_count=parent_comment_data['heart_count'],
                                       is_child_comments=parent_comment_data['is_child_comments'],
                                       child_comment_count=parent_comment_data['child_comment_count'])
        db_session.add(parent_comment)
        db_session.flush()
    except Exception as e:
        db_session.rollback()
        raise e


def create_child_comment(child_comment_data: dict, db_session):
    try:
        child_comment = ChildComment(id=child_comment_data['id'],
                                     author_id=child_comment_data['author_id'],
                                     parent_id=child_comment_data['parent_id'],
                                     comment_text=child_comment_data['comment_text'],
                                     heart_count=child_comment_data['heart_count'])
        db_session.add(child_comment)
        db_session.flush()
    except Exception as e:
        db_session.rollback()
        raise e


def create_video_tag(video_id, tag_id, db_session):
    try:
        dt = insert(VideoTag).values(video_id=video_id, tag_id=tag_id)
        db_session.execute(dt)
        db_session.flush()
    except Exception as e:
        db_session.rollback()
        raise e
