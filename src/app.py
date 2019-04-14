from typing import Any

from ariadne import gql, load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette

from src.loaders.heroes import HeroesLoader
from src.resolvers.Date import date_scalar
from src.resolvers.Hero import hero
from src.resolvers.MoveType import move_type
from src.resolvers.WeaponType import weapon_type
from src.resolvers.Query import query

# SCHEMA DEFINITION
type_defs = load_schema_from_path("src/schema.graphql")


class LoaderGraphQL(GraphQL):
    async def context_for_request(self, request: Any, data: Any) -> Any:
        return {"loaders": {"heroes_loader": HeroesLoader()}, "request": request}


schema = make_executable_schema(
    type_defs, [query, hero, weapon_type, move_type, date_scalar]
)
graphql_server = LoaderGraphQL(schema)

app = Starlette()
app.add_route("/", graphql_server)
app.add_websocket_route("/", graphql_server)
