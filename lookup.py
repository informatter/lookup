from dataclasses import dataclass
from typing import Any
from typing import List


LOAD_FACTOR_THRESHOLD=0.75


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
    def __init__(self, length:int=11):
        self.length:int = length
        self.buckets:List[Data | None] = [None for _ in range(self.length)]
        self.size = 0

    
    def hash(self,key:Any, collision_count:int = 0)->int:
        """
        Hashes the key based on the Integer universe assumption using the hashing by division technique
        """
        key_hash = hash(key)
        hash_1 = key_hash % self.length
        hash_2 = 1 + (key_hash % (self.length - 1))
        return (hash_1 + collision_count * hash_2) % self.length
    

    def __compute_load_factor(self) ->float:
        """
        """
        # Load factor: 𝛼 = n / m
        return self.size / self.length


    def __resize(self):
        """
        Resizes the table by only hashing entries which have not been marked as deleted.
        It only creates the new table with active entries.
        """
        self.length  = self.length*2
        self.size = 0
        new_buckets = [None for _ in range(self.length)]
        
        for item in self.buckets:
            if item is None or item.is_deleted: continue

            self.__insert(new_buckets,item.key,item.value)
        
        self.buckets = new_buckets

    
    def __insert(self,buckets:List[Data|None], key:Any, value:Any) -> None:
    
        collision_count = 0
        home_location = self.hash(key,collision_count)

        if buckets[home_location] is None:
            buckets[home_location] = Data(key,value)
            self.size+=1
            return
        
        if buckets[home_location] is not None and buckets[home_location].key == key:
            buckets[home_location].value = value
            return
        

        delta_location = None
        collision_count+=1
        
        #start probing!

        while home_location != delta_location:
            delta_location = self.hash(key,collision_count)

            # if an item with the same key is being inserted, override its value
            if buckets[delta_location] is not None and buckets[delta_location].key == key:
                buckets[delta_location].value = value
                return

            if buckets[delta_location] is None:
                buckets[delta_location] = Data(key,value)
                self.size+=1
                return
            collision_count+=1
        

    def insert(self, key:Any, value:Any) -> None:

        load_factor:float = self.__compute_load_factor()
        if load_factor >= LOAD_FACTOR_THRESHOLD:
            self.__resize()

        self.__insert(self.buckets,key,value)


    def search (self, key:Any)-> Any | None:
        """
        Gets a value by a specified key.

        Returns
        -------
        `None` if the element does not exist; Otherwise the value is returned
        """

        collision_count = 0
        home_location = self.hash(key,collision_count)
        data:None|Data = self.buckets[home_location]

        if data is None:
            return None

        if data is not None and data.key == key and data.is_deleted is False:
            return data.value
        
    
        delta_location = None
        collision_count+=1
        
        # start probing!

        while home_location != delta_location:
            delta_location = self.hash(key,collision_count)
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

        collision_count = 0
        home_location = self.hash(key,collision_count)
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
        while home_location != delta_location:
            delta_location = self.hash(key,collision_count)
            data:None|Data = self.buckets[delta_location]
            if data is None:
                return False
            if data is not None and data.key == key and data.is_deleted is False:
                data.is_deleted = True
                self.size-=1
                return True
            collision_count+=1

        return False

