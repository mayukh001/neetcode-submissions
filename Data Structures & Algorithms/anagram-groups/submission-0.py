from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)   # We use defaultdict(list) so that if a key doesn't exist, 
                                  # Python automatically creates an empty list [] for us.
        for s in strs:
            count = [0]*26  #a-z count...initilization count
            for char in s:
                count[ord(char)- ord('a')] +=1   #n-1 logic
            res[tuple(count)].append(s)     #converting list to tuple for the immutabbility as it is used as a dictionary key
        return list(res.values())  #again conversion of tup to list as default dict is list        