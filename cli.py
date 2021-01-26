# -*- coding: utf-8 -*-
"""
A cli.py script to centralized all cli commands
Created on :
@author:
"""

# imports
import argparse

# local imports
from src.models import Base, engine, session, User


parser = argparse.ArgumentParser(description="My cart cli")

# Add the arguments
parser.add_argument('-m', '--migrate', type=str, help='create the database tables')
parser.add_argument('-u', '--username', type=str, help='Username for the new user')
parser.add_argument('-p', '--password', type=str, help='password for the new user')
parser.add_argument('-n', '--name', type=str, help='Name for the new user')
parser.add_argument('-e', '--email', type=str, help='Email for the new user')


# Execute the parse_args() method
args = parser.parse_args()


def migrate():
    """
    A migrate command for creating database tables
    :return:
    """
    Base.metadata.create_all(engine)


def add_user():
    """
    username = Column(String)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    usertype = Column(String)
    :return:
    """
    username = args.username
    password = args.password
    name = args.name
    email = args.email

    if username and password and name and email:

        user = User(username=username, password=password, name=name, email=email)
        session.add(user)
        session.commit()


if __name__ == '__main__':
    if args.migrate:
        migrate()

    if args.username:
        add_user()