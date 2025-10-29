class Queue:
  def __init__(self):
    self.__list = []

  def __str__(self):
    return f"[{'--'.join(map(str, self.__list))}]"

  def enqueue(self, element):
    self.__list.append(element)
    return True

  def dequeue(self):
    if self.is_empty():
      return "No hay elementos en cola"
    return self.__list.pop(0)

  def first(self):
    if self.is_empty():
      return "No hay elementos en cola"
    return self.__list[0]

  def len(self):
        return len(self.__list)

  def is_empty(self):
    return len(self.__list) == 0