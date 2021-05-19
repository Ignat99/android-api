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
    }

    type Project {
        name: String
        product: String
        bars_length: Int
        fullName: String
    }
""")

query = QueryType()

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

project = ObjectType("Project")

@project.field("fullName")
def resolve_project_fullname(project, *_):
    return "%s %s" % (project["name"], project["product"])

schema = make_executable_schema(type_defs, query, project)

app = GraphQL(schema, debug=True)

#ma = Marshmallow(app)