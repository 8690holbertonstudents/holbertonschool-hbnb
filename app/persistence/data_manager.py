#!/usr/bin/python3
"""
Python module to manage persistence data
"""
import json
import os
from .ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):
    """
    Create DataManager class inherit from IPersistenceManager
    """
    json_dir = 'app/storage/'

    def _get_file_path(self, entity_type):
        """
        Method to retrieve the good file path for a given entity_type
        """
        return os.path.join(self.json_dir, f'{entity_type}.json')

    def save(self, entity):
        """
        Method to save entity to storage
        """
        pass

    def get(self, entity_id, entity_type):
        """
        Method to retrieve an entity_type by id
        """
        full_path = self._get_file_path(entity_type)
        with open(full_path, 'r') as file:
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

    def get_all(self, entity_type):
        """
        Method to get all entities of a given type
        """
        full_path = self._get_file_path(entity_type)
        with open(full_path, 'r') as file:
            return json.load(file)
