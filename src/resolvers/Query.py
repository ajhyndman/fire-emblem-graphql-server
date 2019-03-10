from src.loaders.heroes import HeroesLoader
from ariadne import ResolverMap

# RESOLVERS
query = ResolverMap("Query")

@query.field("heroes")
async def resolve_heroes(obj, info):
    return await info.context["loaders"]["heroes_loader"].load("ALL")