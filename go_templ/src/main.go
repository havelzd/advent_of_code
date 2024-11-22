package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("Hello, World!")

	dat, err := os.ReadFile("../inputs/input.txt")

	if err != nil {
		fmt.Println("Error reading file")
		return
	}

	data_string := string(dat)

	fmt.Println(data_string)
}
