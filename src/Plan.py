import json
from src.Model import Model

class Plan:
  __filepath: str

  def __init__(self, fp: str = '/project/plan.json') -> None:
    self.__filepath = fp

  def getList(self):
    return list(json.load(open(self.__filepath, 'r+')))
  
  def setFilepath(self, filepath: str):
    self.__filepath = filepath

  def updateItem(self, item: Model): 
    listing = self.getList()
    for i in range(len(listing)):
      if (listing[i]['name'] == item.name):
        listing[i] = item.getAttibutes()

    self.__savePlan(listing)

  def __savePlan(self, data:list):
    json.dump(data, open(self.__filepath, 'w+'))

  def getDownloadList(self):
    return list(filter(lambda item: not item['downloaded'], self.getList()))
  
  def getProcessList(self):
    return list(filter(lambda item: not item['processed'], self.getList()))
  