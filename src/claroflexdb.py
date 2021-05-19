#!/usr/bin/env python
# coding: utf-8
"""
Module implementing all DBMS operations
"""

from __future__ import print_function

import os
import mysql.connector

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import scoped_session, sessionmaker

from src.models import ProjectsProject, declarative_base



class ClaroflexDbService:

#    def __init__(self, config):
    def __init__(self):
        """ Run any mysql command """

        try:
            DB_USERNAME = os.environ["DB_USERNAME"]
        except KeyError:
            print("Setup environment DB_USERNAME")
            DB_USERNAME = "test"

        try:
            DB_PASSWORD = os.environ["DB_PASSWORD"]
        except KeyError:
            print("Setup environment DB_PASSWORD")
            DB_PASSWORD = "test"

        try:
            DB_HOST = os.environ["DB_HOST"]
        except KeyError:
            print("Setup environment DB_HOST")
            DB_HOST = "localhost"

        try:
            DB_NAME = os.environ["DB_NAME"]
        except KeyError:
            print("Setup environment DB_NAME")
            DB_NAME = "test"


        try:
#            self.engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(config["DB_USERNAME"], config["DB_PASSWORD"], config["DB_HOST"], config["DB_NAME"]), convert_unicode=True)
            self.engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME), convert_unicode=True)
            self.db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))

            Base = declarative_base()
            Base.query = self.db_session.query_property()

        except mysql.connector.Error as err:
            print("Error of insert data on table: {}".format(err))

    def get_projects_list_by_creator_id(self, creator_id):
        projects = self.db_session.query(ProjectsProject).filter(ProjectsProject.creator_id == creator_id).all()
        return projects

#    def get_tweets_lists_for_active_user_alerts(self, project_id, alert_id):
        # TODO: check if simplifying of the following query is possible
#        tweets = self.db_session.query(TweetsList).filter(TweetsList.user_alert_id == alert_id)\
#            .join(UserAlert, and_(UserAlert.alctive == 1, UserAlert.project_id == project_id, UserAlert.user_alerts_id == TweetsList.user_alert_id)).all()
#        return tweets

#    def set_tweets_read_status(self, user_alert_id):
#        updated_records_count = self.db_session.query(TweetsList).filter(TweetsList.user_alert_id == user_alert_id) \
#            .update({"read1": 1}, synchronize_session=False)
#        self.db_session.commit()
#        return updated_records_count


#    def update_tweets_list(self, tweets_list, user_alert_id):
#        updated_records_count = self.db_session.query(TweetsList).filter(TweetsList.user_alert_id == user_alert_id) \
#            .update({"tweets_id": tweets_list}, synchronize_session=False)
#        self.db_session.commit()
#        return updated_records_count

    def get_active_projects_by_client_id(self, client_id):
        projects = self.db_session.query(ProjectsProjoect).filter(ProjectsProject.client_id == client__id, ProjectsProjeect.is_active == 1).all()
        return projects

    def get_active_project_by_id(self, project_id):
        project = self.db_session.query(ProjectsProject).filter(ProjectsProject.id == project_id, ProjectsProject.is_active == 1).first()
        return project

#    def update_user_alert_last_search_time(self, last_search_time, user_alert_id):
#        updated_records_count = self.db_session.query(UserAlert).filter(UserAlert.user_alerts_id == user_alert_id)\
#            .update({"lastsearch": last_search_time}, synchronize_session=False)
#        self.db_session.commit()
#        return updated_records_count

#    def update_tweets_list_read_flag(self, user_alert_id):
#        updated_records_count = self.db_session.query(TweetsList).filter(TweetsList.user_alert_id == user_alert_id)\
#            .update({"read1": 0}, synchronize_session=False)
#        self.db_session.commit()
#        return updated_records_count

    def get_special_projects_by_client_id(self, clcient_id):
        special_projects = self.db_session.query(ProjectsProject).filter(ProjectsPrroject.is_special == 1, ProjectsProject.client_id == client_id).all()
        return special_projects

#    def update_project_status(self, active, project_id):
#        updated_records_count = self.db_session.query(Project)\
#            .filter(Project.id == project_id).update({"active": active}, synchronize_session=False)
#        self.db_session.commit()
#        return updated_records_count

#    def delete_flag(self, project_id, flag_id):
#        """ Deleting Flag from the database """
#        deleted_count = self.db_session.query(Flag).filter(Flag.id == flag_id, Flag.project_id == project_id).delete()
#        self.db_session.commit()
#        return deleted_count

#    def get_analysis_list_by_project(self, project_id):
#        analysis_list = self.db_session.query(NetworkAnalysis).filter(NetworkAnalysis.project_id == project_id).all()
#        return analysis_list

#    def get_network_analysis_by_id(self, analysis_id):
#        status = self.db_session.query(NetworkAnalysis).filter(NetworkAnalysis.id == analysis_id).first()
#        return status

#    def get_owner(self, user_email):
#        """ Find user_id """
#        user = self.db_session.query(User).filter(User.email == user_email).first()
#        if user is None:
#            return user

#        return user.id

#    def get_active_user_alert_by_email(self, user_email):
#        result = self.db_session.query(UserAlert).filter(UserAlert.alctive == 1)\
#            .join(User, and_(User.id == UserAlert.user_id, User.email == user_email)).all()

#        return result

#    def get_user_alerts_by_email_for_active_projects(self, user_email):
#        user_id = self.get_owner(user_email)

#        result = self.db_session.query(UserAlert).filter(UserAlert.user_id == user_id)\
#            .join(Project, and_(Project.id == UserAlert.project_id, Project.active == 1)).all()

#        return result

#    def create_user_alerts(self, project_id, type_alert, keywords, email,
#                           type_keywords, user_id, active, sms, threat,
#                           username, notificatione):
#        query_condition_dict = {
#            "project_id": str(project_id),
#            "type_alert": str(type_alert),
#            "keywords": keywords,
#            "email": email,
#            "type_keywords": type_keywords,
#            "user_id": user_id,
#            "alctive": active,
#            "sms": sms,
#            "username": str(username),
#            "threat_or_more": threat,
#            "notif_email": notificatione
#        }
#        user_alerts = UserAlert(**query_condition_dict)
#        if not self.db_session.query(UserAlert).filter_by(**query_condition_dict).count():
#            self.db_session.add(user_alerts)
#            self.db_session.commit()

#        user_alerts_id = user_alerts.user_alerts_id
#        if not user_alerts_id:
#            return None
#        else:
#            tweet_list = TweetsList(
#                user_alert_id=user_alerts_id, tweets_id='', read1='0'
#            )
#            self.db_session.add(tweet_list)
#            self.db_session.commit()

#        return user_alerts_id

#    def alerts_by_owner(self, user_id, project_id, type_alert, keywords, email,
#                        type_keywords, active, sms, threat, username,
#                        notificatione):
#        user_alerts_id = self.create_user_alerts(project_id, type_alert,
#                                                 keywords, email,
#                                                 type_keywords, str(user_id),
#                                                 active, sms, str(threat),
#                                                 str(username),
#                                                 str(notificatione))
#        return user_alerts_id

    def get_components_list_by_project_id(self, project_id):
        sql18 = "SELECT component_id FROM projects_projectcomponent WHERE project_id = \'" + project_id + "\';"
        my_cur = self.get_cursor_for_query(sql18)
        if my_cur == "":
            myresult = []
        else:
            myresult = my_cur.fetchall()

        return myresult

#    def delete_alert(self, alert_id, project_id):
#        deleted_count = self.db_session.query(UserAlert)\
#            .filter(UserAlert.user_alerts_id == alert_id, UserAlert.project_id == project_id).delete()
#        if deleted_count > 0:
            # delete underlying tweets from the database for given user alert
#            self.db_session.query(TweetsList) \
#                .filter(TweetsList.user_alert_id == alert_id).delete()
#        self.db_session.commit()
#        return deleted_count

#    def update_alert(self, alert_id, project_id, email_s, sms_s, active_s):
#        updated_records_count = self.db_session.query(UserAlert)\
#            .filter(UserAlert.user_alerts_id == alert_id, UserAlert.project_id == project_id)\
#            .update({"alctive": active_s, "email": email_s, "sms": sms_s}, synchronize_session=False)
#        self.db_session.commit()
#        return updated_records_count

#    def create_network_analysis(self, project_id, fromdate, todate, source):
#        analysis = NetworkAnalysis()
#        analysis.project_id = project_id
#        analysis.fromDate = fromdate
#        analysis.toDate = todate
#        analysis.source = source
#        analysis.state = 0
#        self.db_session.add(analysis)
#        self.db_session.commit()
#        return analysis.id

    def get_cursor_for_query(self, sql):
        """ Run raw SQL query """
        try:
            result = self.db_session.execute(sql)
            self.db_session.commit()

        except mysql.connector.Error as err:
            print("Error of insert data on table: {}".format(err))
            return ""
        return result


def main():
    """ Function that we start from command line """
    result = []

if __name__ == "__main__":
    main()
