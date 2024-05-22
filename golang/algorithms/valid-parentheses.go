package main

import (
	"fmt"
)

func isValid(s string) bool {
	if len(s) == 0 || len(s)%2 == 1 {
		return false
	}

	pairs := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}
	stack := []rune{}

	for _, r := range s {
		if _, ok := pairs[r]; ok {
			stack = append(stack, r)
		} else if len(stack) == 0 || pairs[stack[len(stack)-1]] != r {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}


func main() {
    par1 := "[()]"
    fmt.Println(isValid(par1))
    par2 := "[()"
    fmt.Println(isValid(par2))
}

// Time: O(n)
// Space: O(n)