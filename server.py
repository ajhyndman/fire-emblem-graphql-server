from ariadne import (
    ResolverMap,
    gql,
    load_schema_from_path,
    make_executable_schema,
    start_simple_server
)

from src.schema.Hero import hero
from src.loaders.heroes import HeroesLoader

# SCHEMA DEFINITION
type_defs = load_schema_from_path("./schema.graphql")

# RESOLVERS
query = ResolverMap("Query")

heroes_loader = HeroesLoader()

@query.field("heroes")
async def resolve_heroes(*_):
    return await heroes_loader.load()


# START SERVER
schema = make_executable_schema(type_defs, [query, hero])
start_simple_server(schema, host="localhost", port=8888)
