import os
import pickle
from abc import ABC


class DAO(ABC):
    def __init__(self, datasource: str = "", folder: str = "data") -> None:
        self.__datasource = os.path.join(folder, datasource)
        self.__cache = {}
        os.makedirs(folder, exist_ok=True)
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __load(self) -> None:
        with open(self.__datasource, "rb") as f:
            self.__cache = pickle.load(f)

    def __dump(self) -> None:
        with open(self.__datasource, "wb") as f:
            pickle.dump(self.__cache, f)

    def add(self, key, obj) -> None:
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def get_all(self) -> list:
        return list(self.__cache.values())

    def update(self, key, obj) -> None:
        try:
            if self.__cache[key] is not None:
                self.__cache[key] = obj 
                self.__dump()  
        except KeyError:
            pass

    def remove(self, key) -> None:
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass
