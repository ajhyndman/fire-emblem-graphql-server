from typing import Any

from ariadne import (
    ResolverMap,
    gql,
    load_schema_from_path,
    make_executable_schema,
    start_simple_server
)
from starlette.applications import Starlette
import uvicorn

from src.graphql import GraphQL
from src.loaders.heroes import HeroesLoader
from src.resolvers.Hero import hero
from src.resolvers.Query import query

# SCHEMA DEFINITION
type_defs = load_schema_from_path("./schema.graphql")


class LoaderGraphQL(GraphQL):
    async def context_for_request(self, request: Any) -> Any:
        return {
            "loaders": {
                "heroes_loader": HeroesLoader(),
            },
            "request": request,
        }


# START SERVER
schema = make_executable_schema(type_defs, [query, hero])
graphql_server = LoaderGraphQL(schema)

app = Starlette()
app.add_route("/", graphql_server)
app.add_websocket_route("/", graphql_server)
app.debug = True

uvicorn.run(app, host='localhost', port=8888)
