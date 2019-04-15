from typing import Any

from ariadne import gql, load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette

from src.loaders.base_stats import BaseStatsLoader
from src.loaders.heroes import HeroesLoader
from src.loaders.skills import SkillsLoader
from src.resolvers.Date import date_scalar
from src.resolvers.Hero import hero
from src.resolvers.HeroSkill import hero_skill
from src.resolvers.MoveType import move_type
from src.resolvers.Rarity import rarity
from src.resolvers.WeaponType import weapon_type
from src.resolvers.Query import query

# SCHEMA DEFINITION
type_defs = load_schema_from_path("src/schema.graphql")


class LoaderGraphQL(GraphQL):
    async def context_for_request(self, request: Any, data: Any) -> Any:
        return {
            "loaders": {
                "base_stats_loader": BaseStatsLoader(),
                "heroes_loader": HeroesLoader(),
                "skills_loader": SkillsLoader(),
            },
            "request": request,
        }


schema = make_executable_schema(
    type_defs, [query, hero, hero_skill, weapon_type, move_type, date_scalar, rarity]
)
graphql_server = LoaderGraphQL(schema)

app = Starlette()
app.add_route("/", graphql_server)
app.add_websocket_route("/", graphql_server)
