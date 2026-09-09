func hasDuplicate(nums []int) bool {
    if len(nums)==0{
        return false
    }
    seen:=make(map[int]bool)
    for i:=0;i<len(nums);i++{
        if _,ok:=seen[nums[i]];ok{
            return true
        }
        seen[nums[i]]=true
    }
    return false
}
