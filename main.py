from typing import List
from fastapi import Depends, HTTPException, FastAPI
import sqlalchemy.orm as _orm
import fastapi as _fastapi

import services as _services
import schemas as _schemas

app = FastAPI(orm_mode="from_attributes")

_services.create_database()

@app.post("/users/", response_model=_schemas.User)
def create_user(user: _schemas.UserCreate, db: _orm.Session = Depends(_services.get_db)):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Oops, the email is in use.")
    try:
        return _services.create_user(db=db, user=user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/", response_model=List[_schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = Depends(_services.get_db),
):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=_schemas.User)
def read_user(user_id: int, db: _orm.Session = Depends(_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="Sorry, this user cannot be found."
        )
    return db_user

@app.post("/users/{user_id}/posts/", response_model=_schemas.Post)
def create_post(
    user_id: int,
    post: _schemas.PostCreate,
    db: _orm.Session = Depends(_services.get_db),
):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="Sorry, this user cannot be found."
        )
    return _services.create_post(db=db, post=post, user_id=user_id)

@app.get("/posts/", response_model=List[_schemas.Post])
def read_posts(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = Depends(_services.get_db),
):
    posts = _services.get_posts(db=db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}", response_model=_schemas.Post)
def read_post(post_id: int, db: _orm.Session = Depends(_services.get_db)):
    post = _services.get_post(db=db, post_id=post_id)
    if post is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="Sorry, this post cannot be found."
        )
    return post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: _orm.Session = Depends(_services.get_db)):
    _services.delete_post(db=db, post_id=post_id)
    return {"message": f"Successfully deleted post with id: {post_id}"}

@app.put("/posts/{post_id}", response_model=_schemas.Post)
def update_post(
    post_id: int,
    post: _schemas.PostCreate,
    db: _orm.Session = Depends(_services.get_db),
):
    return _services.update_post(db=db, post=post, post_id=post_id)
