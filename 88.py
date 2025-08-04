class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        i,m,n=0,0,0
        list1=[]
        list2=[]
        while nums1 and nums2:
            if nums1[i]>0:
                m+=1
                list1.append(nums1[i])
            if nums2[i]>0:
                n+=1
                list2.append(nums2[i])
        a=list1+list2
        for x in range(1,len(a)):
            y=x
            while y>0 and a[y-1]>a[y]:
                a[y],a[y-1]=a[y-1],a[y]
                y-=1
        return a"""
       
        i = 0 
        j = 0  
        merged = [] 
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        
        while i < m:
            merged.append(nums1[i])
            i += 1
        
      
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        
        for k in range(len(merged)):
            nums1[k] = merged[k] 
