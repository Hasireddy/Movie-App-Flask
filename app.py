from flask import Flask
import os
from data_manager import DataManager
from models import db,Movie

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager()  # Create an object of the DataManager class


#Shows list of Users and a form for adding new users
@app.route('/', methods=['GET', 'POST'])
def list_users():
    users = data_manager.get_users()
    return str(users)


#Adds a new User to the database
@app.route('/users', methods = ['POST'])
def create_user():
    pass


#Retrieves user's favorite movie list it it is a GET request
#Add a new movie to a user's list of favorite movies if it is a POST request
@app.route('/users/<int:user_id>/movies', methods=['GET', 'POST'])
def user_favorite_movies(user_id):
    pass


#Modifies the title of a specific movie from a user's favorite movie list
@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie():
    pass

#Removes a specific movie from a user's favorite movie list
@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id):
    pass



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()