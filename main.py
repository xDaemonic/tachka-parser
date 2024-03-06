from src.FileScrapper import FileScraper
from src.Bag import Bag
from src.Model import Model
from src.Plan import Plan
from scenario.GlobalCategoriesScenario import GlobalCategoriesScenario
from models.FileItem import FileItem

if __name__ == "__main__":
  plan = Plan()
  scrapper = FileScraper()

  download_list = plan.getDownloadList()
  if download_list and len(download_list) > 0: 
    data = [FileItem(item) for item in download_list]    
    bag = Bag(data)

    for bag_item in bag.getItems():
      filepath = scrapper.download_file(bag_item)
      bag_item.setAttribute('filepath', filepath)
      bag_item.setAttribute('downloaded', True)
      plan.updateItem(bag_item)

  process_list = plan.getProcessList()
  if process_list and len(process_list) > 0:
    data = [FileItem(item) for item in process_list]
    bag = Bag(data)
    

  