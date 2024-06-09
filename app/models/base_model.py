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
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


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
