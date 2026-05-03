class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #short cut
        return Counter(s) == Counter(t)
        #LOGICAL METHOD ⬇
        #check for length
        """
        if len(s)!= len(t):
            return False
    #creating hashmap i.e dict        
        countS , countT = {},{} 

        for i in range (len(s)):
            countS[s[i]] = 1+ countS.get(s[i] ,0)   #s.i i key in dict, if not present .get (s.i, o) this 0 is fefault value
            countT[t[i]] = 1+ countT.get(t[i] ,0) 
        # return countS == countT  or   
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True              
        
     """