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

    def __init__(self):
        """
        The constructor of the class BaseModel
        """

        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def update(self):
        """
        Update the entity with datetime
        """
        self.updated_at = datetime.now()
