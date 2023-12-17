#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add_user method save the user to the databasee"""
        ed_user = User(email=email, hashed_password=hashed_password)
        self._session.add(ed_user)
        self._session.commit()
        return ed_user

    def find_user_by(self, **user) -> User:
        """method. This method takes in arbitrary keyword arguments
        and returns the first row found in the users table as
        filtered by the method’s input arguments"""
        if not user:
            raise InvalidRequestError
        try:
            users = self._session.query(User).filter_by(**user).first()
        except InvalidRequestError:
            raise InvalidRequestError
        if not users:
            raise NoResultFound
        return users

    def update_user(self, user_id: int, **user) -> None:
        """method will use find_user_by to locate the user to
        update, then will update the user’s attributes as passed in
        the method’s arguments then commit changes to the database"""
        users = self.find_user_by(id=user_id)
        for key, value in user.items():
            if not hasattr(users, key):
                raise ValueError
            else:
                setattr(users, key, value)
                self._session.commit()
