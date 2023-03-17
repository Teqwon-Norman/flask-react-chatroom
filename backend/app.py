from flask import Flask, render_template, request, session, redirect, send_from_directory
from flask_socketio import join_room, leave_room, send, SocketIO
from flask_restx import Api, Resource, fields
from models import Recipe
from exts import db
from config import DevConfig
from string import ascii_uppercase

import random as rand

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

api = Api(app, doc='/docs')
socketio = SocketIO(app)

#model (serializer)
recipe_model = api.model(
    'Recipe',
    {
        "id": fields.Integer(),
        "user_name": fields.String(50),
        "password": fields.String(50)
    }
)

@api.route('/recipes')
class RecipesResource(Resource):
    @api.marshal_list_with(recipe_model)
    def get(self):
        """Get all recipes"""

        recipes=Recipe.query.all()
        return recipes

    @api.marshal_with(recipe_model)
    def post(self):
        """Create a new recipe"""
        data = request.get_json()
        new_recipe = Recipe(
            user_name = data.get('username'),
            password = data.get('password')
        )

        new_recipe.save()
        return new_recipe, 201

@api.route('/recipe/<int:id>')
class RecipeResource(Resource):
    def get(self, id):
        """Get a recipe by ID"""

        pass


    def post(self, id):
        """Update a recipe by ID"""
        pass

    def delete(self, id):
        """Delete a recipe by ID"""
        pass


@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {'message':'Hello World'}
    
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Recipe': Recipe
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)
        create = request.form.get('create', False)

        if not name:
            return "home page" # error please enter a name

        response_body = {
            'name': name,
            'code': code,
            'join': join,
            'create': create
        }
    response_body = {
            'name': name,
            'code': code,
            'join': join,
            'create': create
        }

    return response_body


if __name__ == '__main__':
    socketio.run(app, debug=True)