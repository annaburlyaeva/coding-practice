// A phrase is a palindrome if,
// after converting all uppercase letters into lowercase letters
// and removing all non-alphanumeric characters,
// it reads the same forward and backward.
// Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.

package main

import (
    "fmt"
    "unicode"
)

func isPalindrome(s string) bool {
    chars := []rune{}
    for _, ch := range s {
        if unicode.IsLetter(ch) || unicode.IsNumber(ch) {
            chars = append(chars, unicode.ToLower(ch))
        }
    }
    for start, end := 0, len(chars)-1; start < end; start, end = start + 1, end - 1 {
        if chars[start] != chars[end] {
            return false
        }
    }
    return true
}

func main() {
    str := "A man, a plan, a canal: Panama"
    fmt.Println(isPalindrome(str))
}

// Time: O(n)
// Space: O(n)