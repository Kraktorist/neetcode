#!/usr/bin/env python

class LRUCache:
  
  capacity = 0
  cache = dict()
  head = None 
  tail = None

  def __init__(self, capacity: int):
    """
    """
    self.capacity = capacity

  def get(self, key: int) -> int:
    if key in self.cache.keys():
      self.cache[key]['before'] = None
      self.cache[key]['next'] = self.head
      self.head = self.cache[key]
      return self.cache[key]['value']
    return -1

  def put(self, key: int, value: int) -> None:
      if key in self.cache.keys():
        # update key
        self.cache[key]['before']['next'] = self.cache[key]['next']
        self.cache[key]['next']['before'] = self.cache[key]['before']

        self.cache[key]['before'] = None
        self.cache[key]['next'] = self.head
        self.head = self.cache[key]
      elif len(self.cache.keys()) < self.capacity:
        # insert in non full cache
        self.cache[key] = dict()
        self.cache[key]['before'] = None
        self.cache[key]['next'] = self.head
        if self.head:
            self.head['before'] = self.cache[key]
        self.head = self.cache[key]
      else:
        # insert in full cache
        self.tail = self.tail['before']
        self.tail['next'] = None
        self.cache[key] = dict()
        self.cache[key]['before'] = None
        self.cache[key]['next'] = self.head
      self.cache[key]['value'] = value



