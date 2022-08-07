#!/usr/bin/python3
"""
Defines the base for the rest of the models
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes and methods for others
    Also links this model to FileStorage using the variable storage
    """
    def __init__(self, *args, **kwargs):
        """Initializes an instance"""

        if kwargs and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']

            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)
    def __str__(self):
        """string representation of the instance"""
        
        return f"[{type(self).__name__} ({self.id}) {self.__dict__}]"

    def save(self):
        """save updates to an instance"""

        self.__dict__.update({'updated_at': datetime.now()})
        form .__init__ import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance"""

        disdict = dict(self.__dict__)
        disdict.update({'__class__': type(self}.__name__,
                        'updated_at': self.updated_at.isoformat(),
                        'id': self.id,
                        'created_at': self.ceated_at.isoformat()})
        return disdict
