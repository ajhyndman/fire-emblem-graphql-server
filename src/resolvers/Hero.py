from ariadne import ObjectType

hero = ObjectType("Hero")


@hero.field("baseStats")
async def resolve_base_stats(obj, info):
    return await info.context["loaders"]["base_stats_loader"].load(obj["name"])
