from faker import Faker
from models import User, Blog
from random import choice, randint
from models import db
from app import app

fake = Faker()


def create_users() -> list[User]:
    users = []
    for _ in range(10):
        users.append(User(name=fake.name()))
    return users


def create_blogs(users: list[User]) -> list[Blog]:
    blogs = []
    for _ in range(10):
        random_user = choice(users)
        blogs.append(
            Blog(user_id=random_user.id, content=fake.text(), title=fake.sentence())
        )
    return blogs





with app.app_context():
    User.query.delete()
    Blog.query.delete()

    db.session.commit()
    users = create_users()

    db.session.add_all(users)
    db.session.commit()
    blogs = create_blogs(users)

    db.session.add_all(blogs)

    db.session.commit()




    db.session.commit()
    # import ipdb; ipdb.set_trace()
    print("seeding successful!")