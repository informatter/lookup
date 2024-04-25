from typing import Any
from typing import List

class Lookup:

    def __init__(self, length:int=10):
        self.length:int = length
        self.buckets:List[List[dict]] = [list() for _ in range(self.length)]#[ [],[]...n]
        self.size = 0

    
    def __hash(self,key:Any)->int:
        """
        Hashes the key based on the Integer universe assumption using the hasing by division technique
        """
        return hash(key) % self.length
    

    def __get_bucket(self,key:Any) -> List[dict]:
        hash:int = self.__hash(key)
        return self.buckets[hash]
    

    def __resize(self):
        #TODO
        pass

    def __handle_collisions(self):
        #TODO
        pass

    

    def insert(self, key:Any, value:Any) -> None:
        target_bucket:List[dict]  = self.__get_bucket(key)

        # Does not add items with the same key to the bucket. Instead it updates the old value with the new value
        for item in target_bucket:
            if item["key"] == key:
                item["value"] = value
                return
            
        # handles hash colission: key is different but hashed key is the same.
        # v1
        target_bucket.append({"key":key,"value":value})
        self.size+=1

   
    def delete(self,key:Any)->bool:
        """
        Deletes an element by the specified key.

        Returns
        -------
        `True` if the deletion succeeded; otherwise `False`
        """

        target_bucket:List[dict]  = self.__get_bucket(key)
        n =  len(target_bucket)

        if n == 0:
            return False
        if n ==1:
            del target_bucket[0]
            self.size-=1
            return True
        index_to_remove = None
        for i, item in enumerate(target_bucket):
            if item["key"] == key:
                index_to_remove = i
                break
        del target_bucket [index_to_remove]

        self.size-=1

        return True

    def get (self, key:Any)-> Any | None:
        """
        Gets a value by a specified key.

        Returns
        -------
        `None` if the element does not exist; Otherwise the value is returned
        """
        target_bucket:List[dict]  = self.__get_bucket(key)
        n =  len(target_bucket)
        if n == 0:
            return None
        if n ==1:
            return target_bucket[0]
        
        # loop until we find element with key
        for item in target_bucket:
            if item["key"] == key:
                return item["value"]
        
        return None

