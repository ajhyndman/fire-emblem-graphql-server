from ariadne import (
    ResolverMap,
    gql,
    make_executable_schema,
    start_simple_server
)

from src.schema.Hero import hero
from src.loaders.heroes import batch_get_heroes

# SCHEMA DEFINITION
type_defs = gql('''
type Query {
    heroes: [Hero!]!
}

"""
A hero present in the [Fire Emblem: Heroes](https://fire-emblem-heroes.com/) game.

---

Data about this hero is pulled from the [Fire Emblem: Heroes Wiki](https://feheroes.gamepedia.com/).
"""
type Hero {
    "The canonical, unique name of the hero"
    name: String!

    "A short form of the hero's name"
    shortName: String

    "The hero's title.  e.g. 'Marquess of Ostia'"
    title: String

    "The movement type of the hero"
    moveType: MoveType!

    "The weapon type that the hero can wield"
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
''')

# RESOLVERS
query = ResolverMap("Query")


@query.field("heroes")
def resolve_heroes(*_):
    return batch_get_heroes()


# START SERVER
schema = make_executable_schema(type_defs, [query, hero])
start_simple_server(schema, host="localhost", port=8888)
