package main

import "fmt"

type languageBot interface {
	getGreeting() string
}
type englishBot struct{}
type spanishBot struct{}

func (englishBot) getGreeting() string {
	// varied logic
	return "Hello"
}

func (spanishBot) getGreeting() string {
	// varied logic
	return "Hola"
}

func printGreeting(b languageBot) {
	fmt.Println(b.getGreeting())
}

func main() {
	eb := englishBot{}
	sb := spanishBot{}

	printGreeting(eb)
	printGreeting(sb)
}