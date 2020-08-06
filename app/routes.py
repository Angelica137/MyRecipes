from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'user_name': 'Angelica'}
    recipes = [
			{
          'recipe': 'Fish Tacos',
          'description': 'Delicious fish tacos from Tijuana',
          'time': 25,
          'calories': 400,
			},
			{			
          'recipe': 'Chicken Katsu Curry',
          'description': 'the best chicken katsu ever',
          'time': 20,
          'calories': 350,
			}
		]
    return render_template('index.html', title='Home', user=user, recipes=recipes)
