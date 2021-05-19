# coding: utf-8
#from src.config import *
#from marshmallow import *
from src.example import *
from src.models import *


#class UserAlertSchema(ma.ModelSchema):
#    class Meta:
#        model = UserAlert
#        sqla_session = db_service.db_session


#user_alert_schema = UserAlertSchema()
#user_alerts_schema = UserAlertSchema(many=True)


#class NetworkAnalysisSchema(ma.ModelSchema):
#    class Meta:
#        model = NetworkAnalysis
#        sqla_session = db_service.db_session


#network_analysis_schema = NetworkAnalysisSchema()
#network_analyses_schema = NetworkAnalysisSchema(many=True)


class ProjectSchema(ma.ModelSchema):
    class Meta:
        model = ProjectsProject
        sqla_session = db_service.db_session


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
