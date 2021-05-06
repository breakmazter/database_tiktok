from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import *
from settings import *

engine = create_engine(POSTGRES_URL, echo=True)
Session = sessionmaker(bind=engine)

author_data = {'unique_id': 'bed',
               'nickname': 'red',
               'signature': '343',
               'avatar_image': 'image',
               'follower_count': 12,
               'following_count': 21,
               'heart_count': 3,
               'video_count': 4,
               'relation': 0,
               'bio_link': 'vk.com',
               'is_verified': True,
               'is_private': True,
               'is_commerce': False}
video_data = {'author_id': 1,
              'song_id': 1,
              'view_count': 0,
              'heart_count': 0,
              'comment_count': 0,
              'repost_count': 3,
              'height': 200,
              'width': 300,
              'duration': 10,
              'ratio': '240p',
              'format': 'mp4',
              'encoded_type': '0',
              'description': 'good video about monkey',
              'video_sticker_text': 'wtf',
              'preview_image': 'wtf',
              'is_ad': True,
              'is_stitch_enabled': False}
song_data = {'title': 'good music',
             'author_name': 'lsp',
             'album': 'tragic sity',
             'song_image': 'weq2rd2',
             'song_link': 'e_rty2',
             'duration': 10,
             'video_count': 20,
             'is_original': True}
tag_data = {'name_tag': 'nice_tag',
            'description': 'ls2pcc2cds2',
            'view_count': 2,
            'is_commerce': True}
parent_comment_data = {'author_id': 1,
                       'video_id': 1,
                       'comment_text': "ooh my god it\'s garbage!!!",
                       'heart_count': 45,
                       'is_child_comments': True,
                       'child_comment_count': 2}
child_comment_data = {'author_id': 2,
                      'parent_id': 1,
                      'comment_text': 'stupid comment',
                      'heart_count': 45}


def add_data():
    db_session = Session()

    author = Author(unique_id=author_data['unique_id'],
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

    video = Video(author_id=video_data['author_id'],
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

    song = Song(title=song_data['title'],
                author_name=song_data['author_name'],
                album=song_data['album'],
                song_image=song_data['song_image'],
                song_link=song_data['song_link'],
                duration=song_data['duration'],
                video_count=song_data['video_count'],
                is_original=song_data['is_original'])

    tag = Tag(name_tag=tag_data['name_tag'],
              description=tag_data['description'],
              view_count=tag_data['view_count'],
              is_commerce=tag_data['is_commerce'])

    parent_comment = ParentComment(author_id=parent_comment_data['author_id'],
                                   video_id=parent_comment_data['video_id'],
                                   comment_text=parent_comment_data['comment_text'],
                                   heart_count=parent_comment_data['heart_count'],
                                   is_child_comments=parent_comment_data['is_child_comments'],
                                   child_comment_count=parent_comment_data['child_comment_count'])

    child_comment = ChildComment(author_id=child_comment_data['author_id'],
                                 parent_id=child_comment_data['parent_id'],
                                 comment_text=child_comment_data['comment_text'],
                                 heart_count=child_comment_data['heart_count'])

    print(author, video, song, tag, parent_comment, child_comment)


if __name__ == "__main__":
    add_data()
