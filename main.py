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

        