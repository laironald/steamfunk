from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
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
    stats = relationship("UserStats", backref="user")

class UserStats(Base):
    __tablename__ = 'user_stats'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(45), ForeignKey(User.id))



"""
'user_id'
'url'
'total_view_13-05'
'overview_views_13-05'
'total_view_13-06'
'overview_views_13-06'
'total_view_13-07'
'overview_views_13-07'
'vizcards'
'vizume_type'
'origin'
'name'
'created_at'
'updated_at'
'last_sign_in_at'
'sign_in_count'
'location'
'auth_count'
'linkedin'
'facebook'
'twitter'
'instagram'
'foursquare'
'brief_bio'
'share_follow_me_video_count'
'share_follow_me_video_first_used_at'
'share_follow_me_video_last_used_at'
'set_twitter_profile_url_follow_me_count'
'set_twitter_profile_url_follow_me_first_used_at'
'set_twitter_profile_url_follow_me_last_used_at'
'share_follow_me_friends_count'
'share_follow_me_friends_first_used_at'
'share_follow_me_friends_last_used_at'
'set_url_count'
'set_url_first_used_at'
'set_url_last_used_at'
'share_vizcard_count'
'share_vizcard_first_used_at'
'share_vizcard_last_used_at'
'follow_me_count'
'follow_me_first_used_at'
'follow_me_last_used_at'
'opened_follow_me_drip1_count'
'opened_follow_me_drip1_first_used_at'
'opened_follow_me_drip1_last_used_at'
'opened_follow_me_drip2_count'
'opened_follow_me_drip2_first_used_at'
'opened_follow_me_drip2_last_used_at'
'edit_order_page_count'
'edit_order_page_first_used_at'
'edit_order_page_last_used_at'
'edit_add_page_count'
'edit_add_page_first_used_at'
'edit_add_page_last_used_at'
'photo_page_set_count'
'photo_page_set_first_used_at'
'photo_page_set_last_used_at'
'photo_cover_set_count'
'photo_cover_set_first_used_at'
'photo_cover_set_last_used_at'
'vizcard_created_count'
'vizcard_created_first_used_at'
'vizcard_created_last_used_at'
'photo_profile_set_count'
'photo_profile_set_first_used_at'
'photo_profile_set_last_used_at'
'edit_color_set_count'
'edit_color_set_first_used_at'
'edit_color_set_last_used_at'
'opened_fm_newfeatures_2013july_count'
'opened_fm_newfeatures_2013july_first_used_at'
'opened_fm_newfeatures_2013july_last_used_at'
'bio_viewed_editor_count'
'bio_viewed_editor_first_used_at'
'bio_viewed_editor_last_used_at'
'connections_invite_friends_count'
'connections_invite_friends_first_used_at'
'connections_invite_friends_last_used_at'
'bio_viewed_analytics_count'
'bio_viewed_analytics_first_used_at'
'bio_viewed_analytics_last_used_at'
'bio_viewed_settings_count'
'bio_viewed_settings_first_used_at'
'bio_viewed_settings_last_used_at'
'connections_created_count'
'connections_created_first_used_at'
'connections_created_last_used_at'
'connections_invite_friends_count_count'
'connections_invite_friends_count_first_used_at'
'connections_invite_friends_count_last_used_at'
'share_connections_count'
'share_connections_first_used_at'
'share_connections_last_used_at'
'share_connections_friends_count'
'share_connections_friends_first_used_at'
'share_connections_friends_last_used_at'
"""
