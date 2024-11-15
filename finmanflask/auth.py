from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, Response, json 
)
from finmanflask.db import get_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

def validate(field, value):
    """Validate the field of a given value"""
    # TODO: implement
    return None


@bp.route('/register', methods=('POST', ))
def register():

    input_error = {"status" : 400, "error": "Bad Request", "message":"Invalid input data", "details":[]}
    integrity_error_message = {"status": 409, "error": "Username is already taken."}
    input_error_throw = False


    for key in ['username', 'email', 'password']:
        if request.json.get(key) is None:
            input_error_throw = True
            input_error['details'].append({"field":key, "message":f"{key} is required."})
    
    for field in ['username', 'email', 'password']:
        error = validate(field, request.json[field])
        if error is not None:
            input_error_throw = True
            input_error['details'].append({"field":key , "message":"\n".join(error)})
    
    if input_error_throw is True:
        return jsonify(input_error), input_error['status']
    
    # insert the user into the database, and get their id
    from finmanflask.schema import User
    password_hash = generate_password_hash(request.json['password'])
    user = User(
        username=request.json['username'], 
        email=request.json['email'], 
        password=password_hash
    )
    with Session(get_engine()) as session:
        try:
            session.add(user)
            session.flush() # actually adds the user
            session.refresh(user) # synchronizes with db
            user_id = user.id
            session.commit()
        except IntegrityError as e:
            session.rollback()
            return jsonify(integrity_error_message), 409 #409 - conflict
        finally:
            session.close()
    # return the success response, along with the correct status code
    success = { "message": "User registered successfully", "user":{"id":user_id, "username": request.json['username'], "email":request.json['email']}}

    return jsonify(success), 201 # 201 - CREATED