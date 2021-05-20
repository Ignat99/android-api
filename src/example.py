#!/usr/bin/env python3

from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL
from src.claroflexdb import ClaroflexDbService
#from src.serializers import *
import json
#from marshmallow import Marshmallow

db_service = ClaroflexDbService()

type_defs = gql("""
    type Query {
        projects: [Project!]!
        users: [User!]!
    }

    type User {
        first_name: String
        last_name: String
        username: String
        creator_id: Int
        fullName: String
    }


    type Project {
        name: String
        product: String
        bars_length: Int
    }
""")

query = QueryType()

@query.field("users")
def resolve_projects(*_):
    users = db_service.get_users_list()
    for user in users:
        first_name = user.first_name
        print("User First Name: %s, " % first_name)
    return users



@query.field("projects")
def resolve_projects(*_):
    projects = db_service.get_projects_list_by_creator_id(502)
    for project in projects:
        name = project.name
        print("Name: %s, " % name)
    return projects
#    return json.loads(projects)
#    return projects_schema.dump(projects)
#    return [
#        {"firstName": "John", "lastName": "Doe", "age": 21},
#        {"firstName": "Bob", "lastName": "Boberson", "age": 24},
#    ]

user = ObjectType("User")
project = ObjectType("Project")

@user.field("fullName")
def resolve_user_fullname(project, *_):
    return "%s %s" % (user["first_name"], user["last_name"])

schema = make_executable_schema(type_defs, query, user, project)

app = GraphQL(schema, debug=True)

#ma = Marshmallow(app)