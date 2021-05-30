class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        
        count = 0

        for i in items:
            if ruleKey == "type" and ruleValue == i.pop(0):
                count += 1
            if ruleKey == "color" and ruleValue == i.pop(1):
                count += 1
            if ruleKey == "name" and ruleValue == i.pop(2):
                count += 1

        return count

        # ===============

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        newList = []
        newStr = ""
        count = 0

        for i in s:
            if i == "L":
                count -= 1
                newStr += i
            else:
                count += 1
                newStr += i

            if count == 0:
                newList.append(newStr)
                newStr = ""         

        return len(newList)
                
                
                
        
        
'''

U:

["RLRLRLRL"]
output = 4

["RLLRLLRLRL"]
output = 3

'''        

# ===============

from collections import deque

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        self.arr = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.arr[0] > 0:
            self.arr[0] -= 1
            return True
        elif carType == 2 and self.arr[1] > 0:
            self.arr[1] -= 1
            return True
        elif carType == 3 and self.arr[2] > 0:
            self.arr[2] -= 1
            return True
        else:
            return False
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# ===============

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        newList = []
        
        newList.append(first)
        
        for i in range(len(encoded)):
            newList.append(encoded[i]^newList[i])
                           
        return newList