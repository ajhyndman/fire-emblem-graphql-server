# fire-emblem-graphql-server

`fire-emblem-graphql-server` is a Python ASGI server application exposing a [GraphQL](https://graphql.org/) API, implemented with [ariadne](https://github.com/mirumee/ariadne).

## Consuming the API

TODO: Expand this section

## Running the server

Dependencies for `fire-emblem-graphql-server` are managed using [Poetry](https://poetry.eustace.io/).  Directions for installing poetry can be [found here](https://poetry.eustace.io/docs/#installation).

This server also relies on python 3.7+.  It's recommended that you install new versions of python using [pyenv](https://github.com/pyenv/pyenv).

Once you have poetry and python 3.7, start the server with the following commands:

1. `poetry install` (Automatically creates and manages a virtual environment for this server's python packages)
2. `poetry run dev`
