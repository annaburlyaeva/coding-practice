package main

import "fmt"

func Pic(dx, dy int) [][]uint8 {
	res := [][]uint8{}
	for i:=0; i<dy; i+=1 {
		row := []uint8{}
		for j:=0; j<dx; j+=1 {
			row = append(row, uint8(i+j + i*j))
		}
		res = append(res, row)
	}
	return res
}

func main() {
	fmt.Println(Pic())
}