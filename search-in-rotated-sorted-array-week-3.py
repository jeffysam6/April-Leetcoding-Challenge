class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        
        if(len(arr) == 0):
            return -1

        left = 0

        right = len(arr) -1

        while(left < right):

            mid = left + (right - left)//2

            if(arr[mid] > arr[right]):
                left = mid + 1

            else:
                right = mid



        initial = left

        left = 0
        right = len(arr) - 1

        if(target >= arr[initial] and target <= arr[right]):
            left = initial

        else:
            right = initial - 1
            
            
        


        while(left <= right):

            mid = left + (right - left)//2

            if(arr[mid] == target):
                return (mid)

            elif(target > arr[mid]):
                left = mid + 1

            else:
                right = mid - 1


        return -1
