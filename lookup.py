from dataclasses import dataclass
from typing import Any
from typing import List


@dataclass
class Data:
    def __init__(self,key:Any, value:Any,is_deleted:bool=False):
        self.key = key
        self.value=value
        self.is_deleted  = is_deleted
    def __str__(self):
        return f'key: {self.key}, value: {self.value}, is_deleted:{self.is_deleted}'
    def __repr__(self):
        return str(self)
    



class Lookup:

    def __init__(self, length:int=10):
        self.length:int = length
        self.buckets:List[Data | None] = [None for _ in range(self.length)]
        self.size = 0
        # TODO Calculate load factor: 𝛼 = n / m, where n are total items and m is table size -> should be kept < 0.75

    
    def __hash(self,key:Any, collision_count:int)->int:
        """
        Hashes the key based on the Integer universe assumption using the hashing by division technique
        """
        key_hash = hash(key)
        hash_1 = key_hash % self.length
        hash_2 = 1 + (key_hash % (self.length - 1))
        return (hash_1 + collision_count * hash_2) % self.length


    

    def __resize(self):
        #TODO
        pass


    def insert(self, key:Any, value:Any) -> None:


        collision_count = 0
        home_location = self.__hash(key,collision_count)

        if self.buckets[home_location] is None:
            self.buckets[home_location] = Data(key,value)
            self.size+=1
            return

        delta_location = None
        collision_count+=1
        
        # location is full - start probing!

        while home_location != delta_location:
            delta_location = self.__hash(key,collision_count)
            if self.buckets[delta_location] is None:
                self.buckets[delta_location] = Data(key,value)
                self.size+=1
                return
            collision_count+=1
        
        # TODO handle when insertion can't happen -> resize table is full!


    def search (self, key:Any)-> Any | None:
        """
        Gets a value by a specified key.

        Returns
        -------
        `None` if the element does not exist; Otherwise the value is returned
        """

        collision_count = 0
        home_location = self.__hash(key,collision_count)
        data:None|Data = self.buckets[home_location]

        if data is None:
            return None

        if data is not None and data.key == key and data.is_deleted is False:
            return data.value
        
    
        delta_location = None
        collision_count+=1
        
        # start probing!
        # when load factor approaches 1 or is 1 search is O(n)

        while home_location != delta_location:
            delta_location = self.__hash(key,collision_count)
            data:None|Data = self.buckets[delta_location]
            if data is None:
                return None
            if data is not None and data.key == key and data.is_deleted is False:
                return data.value
            collision_count+=1
        
        return None

   
    def delete(self,key:Any)->bool:
        """
        Deletes an element by the specified key.

        Returns
        -------
        `True` if the deletion succeeded; otherwise `False`
        """

        # [{'key': 5, 'value': 'a'}, {'key': 11, 'value': 'a'}, {'key': 3, 'value': 'a'}, {'key': 10, 'value': 'a'}, {'key': 4, 'value': 'a'}]

        # [{'key': 5, 'value': 'a'}, {'key': 11, 'value': 'a'}, {'key': 3, 'value': 'a'},        __None               , {'key': 4, 'value': 'a'}]

        collision_count = 0
        home_location = self.__hash(key,collision_count)
        data:None|Data = self.buckets[home_location]

        if data is None:
            return False
        
        if data is not None and data.key == key and data.is_deleted:
            return False
        
        if data is not None and data.key == key and data.is_deleted is False:
            data.is_deleted = True
            self.size-=1
            return True
        
        delta_location = None
        collision_count+=1

        # start probing!
        # when load factor approaches 1 or is 1 search is O(n)

        while home_location != delta_location:
            delta_location = self.__hash(key,collision_count)
            data:None|Data = self.buckets[delta_location]
            if data is None:
                return False
            if data is not None and data.key == key and data.is_deleted is False:
                data.is_deleted = True
                self.size-=1
                return True
            collision_count+=1

        return False

