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
        projects(creator_id: Int = 1): [Project!]!
        users: [User!]!
        components(project_id: Int = 1): [Component!]!
    }

    type Component {
        id: ID!
        category: String
        code: String
        name: String
        position: String
        price: Int
        price_insystem: Int
        product: String
        weight: Int
    }

    type User {
        id: ID!
        first_name: String
        last_name: String
        username: String
        creator_id: Int
    }


    type Project {
        id: ID!
        name: String
        product: String
        bars_length: Int
    }
""")

query = QueryType()

@query.field("users")
def resolve_projects(*_):
    users = db_service.get_users_list()
    for user_c in users:
        first_name = user_c.first_name
        print("User First Name: %s, " % first_name)
    return users



@query.field("projects")
def resolve_projects(*_, creator_id):
    projects = db_service.get_projects_list_by_creator_id(creator_id)
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

#@user.field("username")
#def resolve_user_username(user, *_):
#    return "%s %s" % (user["first_name"], user["last_name"])

schema = make_executable_schema(type_defs, query, user, project)

app = GraphQL(schema, debug=True)

#ma = Marshmallow(app)