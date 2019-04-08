from src.loaders.heroes import HeroesLoader
from ariadne import ObjectType

# RESOLVERS
query = ObjectType("Query")

@query.field("heroes")
async def resolve_heroes(obj, info):
    return await info.context["loaders"]["heroes_loader"].load("ALL")