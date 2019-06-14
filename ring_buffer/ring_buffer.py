class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    next_spot = self.current + 1
    if next_spot > len(self.storage) - 1:
      next_spot = 0

    self.storage[self.current] = item
    self.current = next_spot



  def get(self):
    return [i for i in self.storage if i is not None]
