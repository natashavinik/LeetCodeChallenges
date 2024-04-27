class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        nlist = [0]
        highest = 0
        for num in gain:
            alt = nlist[-1] + num
            highest = max(highest, alt)
            nlist.append(alt)
        return highest
        