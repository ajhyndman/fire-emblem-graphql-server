from src.loaders.heroes import HeroesLoader
from ariadne import QueryType

# RESOLVERS
query = QueryType()

@query.field("allHeroes")
async def resolve_all_heroes(obj, info):
    return await info.context["loaders"]["heroes_loader"].load("ALL")