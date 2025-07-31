class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #for r in range(len(digits)):
            #if digits[0]!=0 && digits[-1]<=9:
                #digits[-1]+=1
            #if digits[-1]>9:*/
        #result=[]
        #for r in range(len(digits)):
            #if digits[0]!=0:
                #result.append(digits[r])
            #if digits[-1]<=9:
                #digits[-1]+=1
                #result.append(digits[-1])
            #if digits[-1]>9:
                #digits[-2]+=1
                #result.append(digits[-2])
        #return result
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
