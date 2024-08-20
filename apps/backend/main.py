from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema.schema import schema
import os
from dotenv import load_dotenv
from tortoise import Tortoise


async def init_db():
    db_url: str = os.getenv('DATABASE_URL')

    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix='/graphql')


@app.get('/')
def index():
    return {'message': 'Hello, there!'}


if __name__ == '__main__':
    import uvicorn
    load_dotenv()

    init_db()

    uvicorn.run(app, host='0.0.0.0', port=8000)
