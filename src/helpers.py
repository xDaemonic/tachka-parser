def merge(list1: list, list2: list) -> list:
  return [x for n in (list1, list2) for x in n]

def chunks(lst: list, n: int):
  def chunker(l, s):
    for i in range(0, len(l), s):
      yield lst[i:i + s]
  
  return list(chunker(lst, n))