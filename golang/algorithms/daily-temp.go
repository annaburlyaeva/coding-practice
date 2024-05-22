// Given an array of integers temperatures represents the daily temperatures,
// return an array answer such that answer[i]
// is the number of days you have to wait after the ith day
// to get a warmer temperature.
// If there is no future day for which this is possible,
// keep answer[i] == 0 instead.

package main

import (
    "fmt"
)

func dailyTemp(temps []int) []int {
    res := make([]int, len(temps))
    stack := [][]int{}

    for i, t := range temps {
        for len(stack) != 0 && t > stack[len(stack)-1][0] {
            stackIdx := stack[len(stack)-1][1]
            stack = stack[:len(stack)-1]
            res[stackIdx] = i - stackIdx
        }
        stack = append(stack, []int{t, i})
    }
    return res
}

func main() {
    temps := []int{73,74,75,71,69,72,76,73}
    fmt.Println(dailyTemp(temps))
}

// Time: O(n)
// Space: O(n)