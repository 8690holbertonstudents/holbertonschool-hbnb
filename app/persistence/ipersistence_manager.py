#!/usr/bin/python3
"""
Module to create a persistence interface
"""
from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    """
    Create abstract class IPersistenceManager
    """
    @abstractmethod
    def save(self, entity):
        """
        Method to save an entity
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Method to retreive an entity object by id
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Method to update an entity
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Method to delete an entity object by id
        """
        pass
