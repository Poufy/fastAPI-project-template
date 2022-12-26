from fastapi import APIRouter

router = APIRouter(prefix='/greet', tags=['Greet'])

# Order of the routes matter. The first route that matches the request will be executed. so if you have a route that matches any path, it should be the last route in the file.
@router.get('/anyone', summary='Greet everyone', description='This is a description for the greet everyone route', response_description='This is the response description')
def greet():
    return {'message': 'Hello everyone!'}


@router.get('/{name}')
def greet(name: str):
    return {'message': f'Hello {name}! How are you doing today?'}