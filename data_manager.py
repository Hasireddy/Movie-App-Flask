from models import db, User, Movie

#The DataManager class will use SQLAlchemy to interact with SQLite database.It performs all CRUD operations

class DataManager():
    def __init__(self, name):
        self.name = name

    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_users(self):
        users = User.query.all()
        return users

    def get_movies(self,user_id):
        pass

    def add_movie(self, movie):
        pass

    def update_movie(self, movie_id, new_title):
        pass

    def delete_movie(self,movie_id):
        pass



