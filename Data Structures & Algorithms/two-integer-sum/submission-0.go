func twoSum(nums []int, target int) []int {
    hashmap := make(map[int]int)

    for i,val := range nums{
        diff := target - val

        if index,ok:=hashmap[diff]; ok {
            return []int{index,i}
        }
        hashmap[val] = i
    }
    return nil
}