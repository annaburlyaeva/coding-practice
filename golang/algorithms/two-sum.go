// Given an array of integers nums and an integer target,
// return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.
// You can return the answer in any order.

package main

import "fmt"

func twoSum(nums []int, target int) []int {
    numsMap := map[int]int{}
    for i, num := range nums {
        diff := target - num
        if diffIdx, ok := numsMap[diff]; ok {
            return []int{diffIdx, i}
        }
        numsMap[num] = i
    }
    return []int{}
}


func main() {
    nums := []int{3, 2, 4}
    target := 6
    fmt.Println(twoSum(nums, target))
}

// Time: O(n)
// Space: O(n)