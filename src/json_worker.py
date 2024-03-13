import json

def set_process_category_status(url: str, status: bool) -> None:
  with open(file, 'a+') as file:
    items = json.load(file)
    for i in range(0, len(items)):
      if (items[i]['url'] == url):
        items[i]['proc'] = status
        break
      
    file.truncate()
    json.dump(items, file)
    file.close()
      