#!/usr/bin/python3
"""
Defines module base_model
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines class BaseModel
    """

    def __init__(self, id, created_at, updated_at):
        """
        The constructor of the class BaseModel
        """

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
        """
        Save the entity with uuid and datetime
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()

    def update(self):
        """
        Update the entity with datetime
        """
        self.updated_at = datetime.now()
