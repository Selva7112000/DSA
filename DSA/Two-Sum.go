func twoSum(nums []int, target int) []int {
    data := map[int]int{}
    for k,v := range nums {
        data[v] = k
    }
    fmt.Println(data)
    for k,v := range nums {
        value := target -  v
        if exist, ok := data[value]; ok && exist != k {
            return []int{exist, k}
        }
    }
    return []int{}


    // for i := 0; i < len(nums); i++{
    //     for j:= i+1; j < len(nums); j++{
    //         if nums[i] + nums[j] == target{
    //             return []int{i,j}
    //         }
    //     }
    // }
    // return []int{}
    
}