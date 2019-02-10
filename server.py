from ariadne import (
    ResolverMap,
    gql,
    make_executable_schema,
    start_simple_server
)

from src.schema.Hero import hero
from src.loaders.heroes import batch_get_heroes

# SCHEMA DEFINITION
type_defs = gql("""
type Query {
    heroes: [Hero!]!
}

type Hero {
    name: String!
    shortName: String
    title: String
    moveType: MoveType!
    weaponType: WeaponType!
}

enum MoveType {
    Armored
    Cavalry
    Flying
    Infantry
}

enum WeaponType {
    BLUE_LANCE
    BLUE_TOME
    BLUE_BOW
    BLUE_BREATH
    GREEN_AXE
    GREEN_TOME
    GREEN_BOW
    GREEN_BREATH
    RED_SWORD
    RED_TOME
    RED_BOW
    RED_BREATH
    COLORLESS_BOW
    COLORLESS_DAGGER
    COLORLESS_STAFF
}
""")

# RESOLVERS
query = ResolverMap("Query")


@query.field("heroes")
def resolve_heroes(*_):
    return batch_get_heroes()


# START SERVER
schema = make_executable_schema(type_defs, [query, hero])
start_simple_server(schema, host="localhost", port=8888)
