from ariadne import ObjectType

hero_skill = ObjectType("HeroSkill")


@hero_skill.field("skill")
async def resolve_skill(obj, info):
    return await info.context["loaders"]["skills_loader"].load(obj["key"])
