def merge(list1: list, list2: list) -> list:
  return [x for n in (list1, list2) for x in n]

def chunker(l, s):
  for i in range(0, len(l), s):
    yield l[i:i + s]

def chunks(lst: list, n: int):
  return list(chunker(lst, n))