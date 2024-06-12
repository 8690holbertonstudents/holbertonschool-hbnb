#!/usr/bin/python3
"""
Python module to manage persistence data
"""
import json
import os
from app.persistence.ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):
    """
    Create DataManager class inherit from IPersistenceManager
    """

    def __init__(self, storage_file):
        """
        """
        self.storage_file = storage_file

    def save(self, entity):
        """
        Method to save entity to storage
        """

        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except Exception:
            return False
        data.append(entity)

        with open(self.storage_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            return True

    def get_id(self, entity_id):
        """
        Method to retrieve an entity_type by id
        """

        with open(self.storage_file, 'r') as file:
            data = json.load(file)
            for item in data:
                for key in item:
                    if item[key] == entity_id:
                        return item
        return None

    def update(self, entity):
        """
        Method to update an entity in storage
        """
        pass

    def delete(self, entity_id, entity_type):
        """
        Method to delete an entity in storage
        """
        pass

    def get(self):
        """
        Method to get all entities of a given type
        """
        with open(self.storage_file, 'r') as file:
            return json.load(file)
