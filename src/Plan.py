import json
from src.Model import Model
from src.Bag import Bag
from models.FileItem import FileItem

class Plan:
  __filepath: str

  def __init__(self, fp: str = '/project/files/json/plan.json') -> None:
    self.__filepath = fp

  def addList(self, data: list) -> None:
    merged = [x for n in (self.getList(), data) for x in n]
    self.__savePlan(merged)
    
  def update(self, bag: Bag) -> None:
    listing = self.getList()
    for item in bag.getItems():
      listing = self.__replcaeItem(listing, item)

    self.__savePlan(listing)

  def getList(self):
    return list(json.load(open(self.__filepath, 'r+')))
  
  def setFilepath(self, filepath: str):
    self.__filepath = filepath

  def updateFileItem(self, item: FileItem):
    listing = self.getList()
    listing = self.__replcaeItem(listing, item)

    self.__savePlan(listing)

  def getDownloadList(self):
    return list(filter(lambda item: not item['downloaded'], self.getList()))
  
  def getProcessList(self):
    return list(filter(lambda item: not item['processed'], self.getList()))

  def __replcaeItem(self, listing: list, item: FileItem) -> list:
    for i in range(len(listing)):
      if (listing[i]['name'] == item.name):
        listing[i] = item.getAttibutes()
        break

    return listing

  def __savePlan(self, data:list):
    json.dump(data, open(self.__filepath, 'w+'))