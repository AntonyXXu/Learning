package main

import "fmt"

type contactInfo struct {
	email string
	zipCode int
}

type person struct {
	firstName string
	lastName  string
	contact contactInfo
}

type personV2 struct {
	firstName string
	contactInfo
	// same as declaring:
	// contactInfo contactInfo

}

func (p person) print() {
	fmt.Printf("%+v", p)
}

func (p person) updateName(newName string) {
	p.firstName = newName
}

func main() {
	p := person{"Antony", "X", contactInfo{"a@a.ca", 00000}}
	p2 := person{firstName: "Bob", lastName: "X",
		contact: contactInfo{
			email: "b@b.ca",
			zipCode: 00001,
		}}


	p.print()
	p2.print()

	var alex person
	fmt.Printf("%+v", alex)
	alex.firstName = "alex"
	alex.lastName = "bob"
	fmt.Printf("%+v", alex)

	

}