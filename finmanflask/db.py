from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session 
from sqlalchemy.exc import IntegrityError
from flask import g
import click 

# TODO: close connection upon tearing application context
# TODO: make those depend on some config

def get_engine():
    if 'dbEngine' not in g:
        url = URL.create(
            drivername="postgresql",
            username="admin",
            password="admin", 
            host="localhost",
            database="finman"
        )

        g.dbEngine = create_engine(url)

    return g.dbEngine

def init_db():
    from finmanflask.schema import Base, User
    # the database doesn't seem to be updated by the new table
    Base.metadata.create_all(get_engine())
    # TODO: add wiping the database clean upon init
    # TODO: get rid of adding a test user
    with Session(get_engine()) as session:
        try:
            session.add_all([User(username="filip", password="haslofilipa", email="3bentkowski@agh.edu.pl")])
            session.commit()
        except IntegrityError as e:
            session.rollback()
        finally:
            session.close()



        

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)