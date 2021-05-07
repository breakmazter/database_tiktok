from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.crud import *
from settings import *

engine = create_engine(POSTGRES_URL, echo=True)
Session = sessionmaker(bind=engine)

author_data = [{'id': 1,
                'unique_id': 'Alica',
                'nickname': 'Alica',
                'signature': '22',
                'avatar_image': 'image',
                'follower_count': 12,
                'following_count': 21,
                'heart_count': 23,
                'video_count': 4,
                'relation': 0,
                'bio_link': 'vk.com, ok.com',
                'is_verified': True,
                'is_private': False,
                'is_commerce': False},

               {'id': 2,
                'unique_id': 'Bob',
                'nickname': 'Bob',
                'signature': '11',
                'avatar_image': 'image',
                'follower_count': 12,
                'following_count': 21,
                'heart_count': 3,
                'video_count': 78,
                'relation': 0,
                'bio_link': 'vk.com',
                'is_verified': True,
                'is_private': False,
                'is_commerce': False}]

video_data = {'id': 1,
              'author_id': 1,
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

song_data = {'id': 1,
             'title': 'good music',
             'author_name': 'lsp',
             'album': 'tragic sity',
             'song_image': 'weq2rd2',
             'song_link': 'e_rty2',
             'duration': 10,
             'video_count': 20,
             'is_original': True}

tag_data = [{'id': 1,
             'name_tag': 'red',
             'description': 'ls2pcc2cds2',
             'view_count': 2,
             'is_commerce': False},

            {'id': 2,
             'name_tag': 'green',
             'description': 'lwefsdcscds2',
             'view_count': 3,
             'is_commerce': True}]

parent_comment_data = [{'id': 1,
                        'author_id': 1,
                        'video_id': 1,
                        'comment_text': "thanks))",
                        'heart_count': 10000,
                        'is_child_comments': False,
                        'child_comment_count': 0},

                       {'id': 2,
                        'author_id': 2,
                        'video_id': 1,
                        'comment_text': "ooh my god it\'s garbage!!!",
                        'heart_count': 45,
                        'is_child_comments': False,
                        'child_comment_count': 0}]


def add_data():
    db_session = Session()

    # creation of two authors in tiktok
    create_author(author_data=author_data[0], db_session=db_session)
    create_author(author_data=author_data[1], db_session=db_session)

    # creating a song that was played in the video
    create_song(song_data=song_data, db_session=db_session)

    # creation video
    create_video(video_data=video_data, db_session=db_session)

    # adding tags under the video
    create_tag(tag_data=tag_data[0], db_session=db_session)
    create_tag(tag_data=tag_data[1], db_session=db_session)

    # creating a link between all tags and all videos
    create_video_tag(video_data['id'], tag_data[0]['id'], db_session=db_session)
    create_video_tag(video_data['id'], tag_data[1]['id'], db_session=db_session)

    # creation comments author
    create_parent_comment(parent_comment_data=parent_comment_data[0], db_session=db_session)
    create_parent_comment(parent_comment_data=parent_comment_data[1], db_session=db_session)

    db_session.commit()


if __name__ == "__main__":
    add_data()
