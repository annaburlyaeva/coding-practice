package main

import "fmt"

func twoSum(nums []int, target int) []int {

    m := map[int]int{}

    for idx, num := range nums {
        m[num] = idx
    }

    for indexX, num := range nums {
        if indexY, ok := m[target - num]; ok && indexX != indexY {
            return []int{indexX, indexY}
        }
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