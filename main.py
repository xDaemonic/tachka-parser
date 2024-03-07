from src.FileScrapper import FileScraper
from src.Bag import Bag
from src.Plan import Plan

from factory.BagFactory import BagFactory
from factory.ScenarioFactory import ScenarioFactory

from models.FileItem import FileItem

def dd(el):
  if isinstance(el, Bag):
    print(vars(el.getItems()[0]))

  exit(200)

if __name__ == "__main__":
  plan = Plan()
  process_bag = BagFactory.make(plan.getProcessList(), FileItem)
  for item in process_bag.getItems():
    if item.hasScenario():
      scenario = ScenarioFactory.make(item.scenario)
      scenario.run(item)
  
  
  
  
  # scrapper = FileScraper()



  # download_bag = BagFactory.make(plan.getDownloadList(), FileItem)
  # download_bag = scrapper.download_files(download_bag)
  
  # plan.update(download_bag)
  # del download_bag

  # process_bag = BagFactory.make(plan.getProcessList(), FileItem)
  # for item in process_bag.getItems():
  #   if item.hasScenario() and item.hasHtml():
  #     scenario = ScenarioFactory.make(item.scenario, item.getHtml())
  #     scenario.run()