from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String, Unicode, UnicodeText, Boolean, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import exists

''' +++++++++++++++++++++++++++++++++++
Define Tables:
+++++++++++++++++++++++++++++++++++ '''

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(45), primary_key=True)
    url = Column(String(45))
    total_view_13_05 = Column(Integer)
    overview_views_13_05 = Column(Integer)
    total_view_13_06 = Column(Integer)
    overview_views_13_06 = Column(Integer)
    total_view_13_07 = Column(Integer)
    overview_views_13_07 = Column(Integer)
    vizcards = Column(Integer)
    vizume_type = Column(String(45))
    origin = Column(String(45))
    name = Column(Unicode(128))
    sign_in_count = Column(Integer)
    location = Column(String(128))
    auth_count = Column(Integer)
    linkedin = Column(String(45))
    facebook = Column(String(45))
    twitter = Column(String(45))
    instagram = Column(String(45))
    foursquare = Column(String(45))
    brief_bio = Column(UnicodeText)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_sign_in_at = Column(DateTime)

    share_follow_me_video_count = Column(Integer)
    share_follow_me_video_first_used_at = Column(DateTime)
    share_follow_me_video_last_used_at = Column(DateTime)

    set_twitter_profile_url_follow_me_count = Column(Integer)
    set_twitter_profile_url_follow_me_first_used_at = Column(DateTime)
    set_twitter_profile_url_follow_me_last_used_at = Column(DateTime)

    share_follow_me_friends_count = Column(Integer)
    share_follow_me_friends_first_used_at = Column(DateTime)
    share_follow_me_friends_last_used_at = Column(DateTime)

    set_url_count = Column(Integer)
    set_url_first_used_at = Column(DateTime)
    set_url_last_used_at = Column(DateTime)

    share_vizcard_count = Column(Integer)
    share_vizcard_first_used_at = Column(DateTime)
    share_vizcard_last_used_at = Column(DateTime)

    follow_me_count = Column(Integer)
    follow_me_first_used_at = Column(DateTime)
    follow_me_last_used_at = Column(DateTime)

    opened_follow_me_drip1_count = Column(Integer)
    opened_follow_me_drip1_first_used_at = Column(DateTime)
    opened_follow_me_drip1_last_used_at = Column(DateTime)

    opened_follow_me_drip2_count = Column(Integer)
    opened_follow_me_drip2_first_used_at = Column(DateTime)
    opened_follow_me_drip2_last_used_at = Column(DateTime)

    edit_order_page_count = Column(Integer)
    edit_order_page_first_used_at = Column(DateTime)
    edit_order_page_last_used_at = Column(DateTime)

    edit_add_page_count = Column(Integer)
    edit_add_page_first_used_at = Column(DateTime)
    edit_add_page_last_used_at = Column(DateTime)

    photo_page_set_count = Column(Integer)
    photo_page_set_first_used_at = Column(DateTime)
    photo_page_set_last_used_at = Column(DateTime)

    photo_cover_set_count = Column(Integer)
    photo_cover_set_first_used_at = Column(DateTime)
    photo_cover_set_last_used_at = Column(DateTime)

    vizcard_created_count = Column(Integer)
    vizcard_created_first_used_at = Column(DateTime)
    vizcard_created_last_used_at = Column(DateTime)

    photo_profile_set_count = Column(Integer)
    photo_profile_set_first_used_at = Column(DateTime)
    photo_profile_set_last_used_at = Column(DateTime)

    edit_color_set_count = Column(Integer)
    edit_color_set_first_used_at = Column(DateTime)
    edit_color_set_last_used_at = Column(DateTime)

    opened_fm_newfeatures_2013july_count = Column(Integer)
    opened_fm_newfeatures_2013july_first_used_at = Column(DateTime)
    opened_fm_newfeatures_2013july_last_used_at = Column(DateTime)

    bio_viewed_editor_count = Column(Integer)
    bio_viewed_editor_first_used_at = Column(DateTime)
    bio_viewed_editor_last_used_at = Column(DateTime)

    connections_invite_friends_count = Column(Integer)
    connections_invite_friends_first_used_at = Column(DateTime)
    connections_invite_friends_last_used_at = Column(DateTime)

    bio_viewed_analytics_count = Column(Integer)
    bio_viewed_analytics_first_used_at = Column(DateTime)
    bio_viewed_analytics_last_used_at = Column(DateTime)

    bio_viewed_settings_count = Column(Integer)
    bio_viewed_settings_first_used_at = Column(DateTime)
    bio_viewed_settings_last_used_at = Column(DateTime)

    connections_created_count = Column(Integer)
    connections_created_first_used_at = Column(DateTime)
    connections_created_last_used_at = Column(DateTime)

    connections_invite_friends_count_count = Column(Integer)
    connections_invite_friends_count_first_used_at = Column(DateTime)
    connections_invite_friends_count_last_used_at = Column(DateTime)

    share_connections_count = Column(Integer)
    share_connections_first_used_at = Column(DateTime)
    share_connections_last_used_at = Column(DateTime)

    share_connections_friends_count = Column(Integer)
    share_connections_friends_first_used_at = Column(DateTime)
    share_connections_friends_last_used_at = Column(DateTime)
