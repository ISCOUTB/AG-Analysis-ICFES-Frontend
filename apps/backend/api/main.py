from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from typing import List


@strawberry.type
class Movie:
    title: str
    director: str


movies_data = [
    Movie(title='foo', director='bar'),
    Movie(title='for', director='baz'),
    Movie(title='fur', director='buz')
]


@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        return movies_data

@strawberry.type
class Mutation:
    @strawberry.field
    def add_movie(self, title: str, director: str) -> Movie:
        movies_data.append(Movie(title=title, director=director))
        return Movie(title=title, director=director)

schema = strawberry.Schema(query=Query, mutation=Mutation)
app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello there!'}

app.add_route('/graphql', GraphQL(schema=schema, debug=True))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
