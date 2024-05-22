// Given an integer array nums, return true
// if any value appears at least twice in the array,
// and return false if every element is distinct.

package main

import (
    "fmt"
)


func containsDuplicate(nums []int) bool {
    numsMap := map[int]bool{}
    for _, v := range nums {
        if _, ok := numsMap[v]; ok == true {
            return true
        }
        numsMap[v] = true
    }
    return false
}

func main() {
    nums := []int{1, 2, 2}
    fmt.Println(containsDuplicate(nums))
}

// Time: O(n)
// Space: O(n)