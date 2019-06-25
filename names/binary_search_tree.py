class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_branch = BinarySearchTree(value)
    current_branch = self

    # seek this value's spot
    # traverse the tree until we find the missing
    # branch that can hold this value
    while True:
      if current_branch.value <= value:
        if current_branch.right:
          current_branch = current_branch.right
        else:
          current_branch.right = new_branch
          break
      elif current_branch.value > value:
        if current_branch.left:
          current_branch = current_branch.left
        else:
          current_branch.left = new_branch
          break

  def contains(self, target):
    current_branch = self

    # traverse each branch until we hit the target or None
    while current_branch and current_branch.value != target:
      if target < current_branch.value:
        current_branch = current_branch.left
      else:
        current_branch = current_branch.right

    if current_branch:
      return True

    return False


  def get_max(self):
    # seems like for this one, we take all the right turns
    # until we run out

    current_branch = self
    while current_branch.right:
      current_branch = current_branch.right

    return current_branch.value

  def for_each(self, cb):
    # call the callback with this value
    cb(self.value)

    # now call for_each on whichever branches exist
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)
