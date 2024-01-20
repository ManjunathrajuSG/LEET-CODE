class Solution:
  def search(self, reader: 'ArrayReader', target: int) -> int:
    l = bisect.bisect_left(range(10**4), target,
                           key=lambda m: reader.get(m))
    return l if reader.get(l) == target else -1
