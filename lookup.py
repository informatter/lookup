from dataclasses import dataclass
from typing import Any
from typing import List


RESIZE_UP_THRESHOLD=0.60
RESIZE_DOWN_THRESHOLD = 0.12


@dataclass
class Data:
    def __init__(self,key:Any, value:Any,is_soft_deleted:bool=False):
        self.key = key
        self.value=value
        self.is_soft_deleted  = is_soft_deleted
    def __str__(self):
        return f'key: {self.key}, value: {self.value}, is_soft_deleted:{self.is_soft_deleted}'
    def __repr__(self):
        return str(self)
    

class Lookup:
    def __init__(self, length:int=11):
        self.length:int = length
        self._slots:List[Data | None] = [None for _ in range(self.length)]
        self._active_slot_counter = 0 #  only keeps track active slots - soft deleted will not be counted
        self._occupied_slot_counter = 0 # keeps track of all occupied slots - both active and soft deleted

    
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
        Load factor will be calculated using the `_occupied_slot_counter` over the length.
        `_occupied_slot_counter` is used so all items, including the soft deleted are used.
        """
        # Load factor: 𝛼 = n / m
        return self._occupied_slot_counter / self.length


    def __resize(self, new_size:int):
        """
        Resizes the table by only hashing entries which have not been marked as deleted.
        It only creates the new table with active entries.
        """
        self.length  = new_size
        self._active_slot_counter = 0
        new_slots = [None for _ in range(self.length)]
        
        for item in self._slots:
            if item is None or item.is_soft_deleted: continue

            self.__insert(new_slots,item.key,item.value)
        
        self._slots = new_slots

    
    def __insert(self,buckets:List[Data|None], key:Any, value:Any) -> None:
        """
        Inserts a new element in to the table. Resizing will be done of the `RESIZE_UP_THRESHOLD`
        is exceeded 
        """
    
        collision_count = 0
        home_location = self.hash(key,collision_count)

        if buckets[home_location] is None:
            buckets[home_location] = Data(key,value)
            self._active_slot_counter+=1
            self._occupied_slot_counter+=1
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
                self._active_slot_counter+=1
                self._occupied_slot_counter+=1
                return
            collision_count+=1

    
    def get_size(self):
        return self._active_slot_counter

    def get_slots(self):
        return self._slots
    
    def get_load_factor(self):
        return self.__compute_load_factor()
        

    def insert(self, key:Any, value:Any) -> None:
        """
        Inserts a new element in to the table. If the `key` already exists,
        the corresponding item's value will be overriden with the provided `value`
        args:
        `key:Any` - The key of the element
        `value:Any` - The value of the element
        """

        load_factor:float = self.__compute_load_factor()
        if load_factor >= RESIZE_UP_THRESHOLD:
            self.__resize(self.length*2)

        self.__insert(self._slots,key,value)


    def search (self, key:Any)-> Any | None:
        """
        Gets a value by a specified key.
        args:
        `key:Any` - The key of the element to search for

        Returns
        -------
        `None` if the element does not exist; Otherwise the value is returned
        """

        collision_count = 0
        home_location = self.hash(key,collision_count)
        data:None|Data = self._slots[home_location]

        if data is None:
            return None

        if data is not None and data.key == key and data.is_soft_deleted is False:
            return data.value
        
    
        delta_location = None
        collision_count+=1
        
        # start probing!

        while home_location != delta_location:
            delta_location = self.hash(key,collision_count)
            data:None|Data = self._slots[delta_location]
            if data is None:
                return None
            if data is not None and data.key == key and data.is_soft_deleted is False:
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
        load_factor:float = self.__compute_load_factor()
        new_size = self.length // 2
        collision_count = 0
        home_location = self.hash(key,collision_count)
        data:None|Data = self._slots[home_location]

        if data is None:
            return False
        
        if data is not None and data.key == key and data.is_soft_deleted:
            return False
        
        if data is not None and data.key == key and data.is_soft_deleted is False:
            data.is_soft_deleted = True
            self._active_slot_counter-=1
            if load_factor <= RESIZE_DOWN_THRESHOLD:
                self.__resize(new_size)
            return True
        
        delta_location = None
        collision_count+=1

        # start probing!
        while home_location != delta_location:
            delta_location = self.hash(key,collision_count)
            data:None|Data = self._slots[delta_location]
            if data is None:
                return False
            if data is not None and data.key == key and data.is_soft_deleted is False:
                data.is_soft_deleted = True
                self._active_slot_counter-=1
                if load_factor <= RESIZE_DOWN_THRESHOLD:
                    self.__resize(new_size)
                return True
            collision_count+=1

        return False

