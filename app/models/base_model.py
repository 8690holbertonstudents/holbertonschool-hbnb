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

    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        The constructor of the class BaseModel
        """

        self.id = id if id else str(uuid4())
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def save(self):
        """
        Save the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def update(self):
        """
        Update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
