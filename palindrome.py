class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ","").replace("?","").lower()
        
        if list(s.replace(" ","").replace("?","").replace("'","").replace(",","").replace(".","").replace(";","").replace(":","").lower()) == list(reversed(s.replace(" ","").replace("?","").replace("'","").replace(",","").replace(".","").replace(";","").replace(":","").lower())):
            return True
        else:
            return False