package main

import "fmt"

func main() {
	mySlice := []string {"hi", "there"}
	updateSlice(mySlice)
	fmt.Println(mySlice)
}

func updateSlice( s []string) {
	s[0] = "bye"
}