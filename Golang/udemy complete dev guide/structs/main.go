package main

import "fmt"

type person struct {
	firstName string
	lastName  string
}

func main() {
	p := person{"Antony", "X"}
	p2 := person{firstName: "Bob", lastName: "X"}
	fmt.Println(p)
	fmt.Println(p2)

	var alex person
	fmt.Printf("%+v", alex)
	alex.firstName = "alex"
	alex.lastName = "bob"
	fmt.Printf("%+v", alex)
}