'''
You are given an array of integer arr[] where each number represents a vote to a candidate. 
Return the candidates that have votes greater than one-third of the total votes, If there's 
not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.
'''

class Solution:
    def findMajority(self, arr):
        n = len(arr)

        count = {item:arr.count(item) for item in arr}
        result = []
        
        for key, value in count.items():
            if value > n // 3:
                result.append(key)
        
        return result

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    solution = Solution()
    result = solution.findMajority(arr)
    print(result)
    
    arr2 = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
    result2 = solution.findMajority(arr2)
    print(result2)
        