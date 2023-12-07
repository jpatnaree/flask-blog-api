from flask import make_response, jsonify, request, g
from flask import Flask
from models import db, User, Blog
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def root():
    return "<h1>Simple blog site</h1>"


"""
GET/POST/PATCH/DELETE for User
"""


@app.get("/users")
def get_users():
    users = User.query.all()
    data = [user.to_dict() for user in users]
    return make_response(jsonify(data), 200)


@app.get("/users/<int:id>")
def get_user_by_id(id: int):
    user = db.session.get(User, id)
    if not user:
        return make_response(jsonify({"error": f"user id {id} not found"}), 404)
    return make_response(jsonify(user.to_dict()), 200)


@app.post("/users")
def post_user():
    user_data = request.get_json()
    user = User(name=user_data["name"])
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify(user.to_dict()), 201)


@app.patch("/users/<int:id>")
def patch_user(id: int):
    # same as user = db.session.get(User, id)
    user = User.query.filter(User.id == id).first()
    if not user:
        return make_response(jsonify({"error": f"blog id {id} not found"}), 404)
    patch_data = request.get_json()
    for key in patch_data:
        setattr(user, key, patch_data[key])

    db.session.add(user)
    db.session.commit()
    return make_response(jsonify(user.to_dict()), 200)


@app.delete("/users/<int:id>")
def delete_user(id: int):
    user = User.query.filter(User.id == id).first()
    if not user:
        return make_response(jsonify({"error": f"user id {id} not found"}), 404)
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify({}), 200)


"""
GET/POST/PATCH/DELETE for Blog
TODO: fill these in
"""


@app.get("/users/<int:id>/blogs")
def get_blogs_for_user(id: int):
    user = db.session.get(User, id)
    # user = User.query.filter(User.id == id).first()
    if not user:
        return make_response(jsonify({"error": f"user id {id} not found"}), 404)
    blogs = Blog.query.filter(Blog.user_id == id).all()
    # if not blogs:
    #     return make_response(jsonify({"error": f"no blogs"}), 404)
    return make_response(jsonify([b.to_dict() for b in blogs]), 200)


@app.post("/users/<int:id>/blogs")
def post_blog_for_user(id: int):
    data = request.json
    
    if not db.session.get(User, id):
        return make_response(jsonify({"error": f"user id {id} not found"}), 404)    
    try:
        new_blog = Blog(
            user_id=id, content=data.get("content"), title=data.get("title")
        )
        db.session.add(new_blog)
        db.session.commit()
        return make_response(jsonify(new_blog.to_dict()), 201)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": f"error{e} occurred while creating blog"}), 405)


@app.get("/blogs/<int:id>")
def get_blog_by_id(id: int):
    blog = Blog.query.filter(Blog.id == id).first()
    if not blog:
        return make_response(jsonify({"error": f"blog id {id} not found"}), 404)
    return make_response(jsonify(blog.to_dict()), 200)


@app.patch("/blogs/<int:id>")
def patch_blog(id: int):
    data = request.json
    blog = db.session.get(Blog, id)
    if not blog:
        return make_response(jsonify({"error": f"blog id {id} not found"}), 404)  
    try:
        for key in data:
            setattr(blog, key, data[key])
        db.session.add(blog)
        db.session.commit()
        return make_response(jsonify(blog.to_dict()), 201)
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": f"error{e} occurred while creating blog"}), 405)


@app.delete("/blogs/<int:id>")
def delete_blog(id: int):
    blog = db.session.get(Blog, id)
    if not blog:
        return make_response(jsonify({"error": f"blog id {id} not found"}), 404)
    db.session.delete(blog)
    db.session.commit()    
    return make_response(jsonify({}), 204)


if __name__ == "__main__":
    app.run(port=5555, debug=True)