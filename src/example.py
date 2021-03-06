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
        componentids (project_id: Int = 1): [Projectcomponent!]!
        component (component_id: Int = 1): [Component!]!
    }

    type Projectcomponent {
        id: ID!
        component_id: Int
        project_id: Int
        product: String
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

@query.field("component")
def resolve_component(*_, component_id):
    components = db_service.get_component_by_component_id(component_id)
#    for component_c in components:
#        code = component_c.code
#        print("Component code: %d " % component_c.component_id)
    return components



@query.field("componentids")
def resolve_componentsids(*_, project_id):
    components = db_service.get_componentids_list_by_project_id(project_id)
    for component_c in components:
#        code = component_c.code
        print("Component code: %d " % component_c.component_id)
    return components


@query.field("users")
def resolve_users(*_):
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