        for i in range(len(nums)):
            if target == nums[i] and len(nums)>1:
                return i
            elif len(nums)==1 and nums[i]==target:
                return 0
            elif len(nums)==1 and nums[i]!=target:
                return -1
            elif target not in nums:
                return -1
