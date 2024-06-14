#!/usr/bin/python3
"""
Python module to manage persistence data
"""
import json
import os
from app.persistence.ipersistence_manager import IPersistenceManager
from app.models.base_model import BaseModel


class DataManager(IPersistenceManager):
    """
    Create DataManager class inherit from IPersistenceManager
    """

    def __init__(self, storage_file):
        """
        """
        self.storage_file = storage_file

    def r_data(self):
        """
        Internal method to read data from the storage file
        """
        if not os.path.exists(self.storage_file):
            return []
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
                if not file_data:
                    return []
                return file_data
        except Exception:
            return False

    def w_data(self, data):
        """
        Internal method to write data to the storage file
        """
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception:
            return False

    def save(self, entity):
        """
        Method to save entity to storage
        """
        data = self.r_data()
        if data is False:
            return False
        data.append(entity)
        return self.w_data(data)

    def get_id(self, entity_id):
        """
        Method to retrieve an entity_type by id
        """
        data = self.r_data()
        if data is False:
            return None

        for item in data:
            for key in item:
                if item[key] == entity_id:
                    return item
        return False

    def update(self, entity_type, entity):
        """
        Method to update an entity in storage
        """
        data = self.r_data()
        if data is False:
            return False

        updated = False
        for item in data:
            if item[entity_type] == entity[entity_type]:
                data.remove(item)
                entity['updated_at'] = BaseModel.update(self)
                data.append(entity)
                updated = True
                break

        if updated:
            return self.w_data(data)
        return False

    def delete(self, entity_type, entity):
        """
        Method to delete an entity in storage
        """
        data = self.r_data()
        if data is False:
            return False

        data_s_lenght = len(data)
        for item in data:
            if item[entity_type] == entity[entity_type]:
                data.remove(item)
            if len(data) != data_s_lenght:
                return self.w_data(data)
        return False

    def get(self):
        """
        Method to get all entities of a given type
        """
        data = self.r_data()
        if data is False:
            return None
        return data
