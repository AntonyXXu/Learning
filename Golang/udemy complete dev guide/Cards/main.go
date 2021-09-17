package main

import "fmt"

func main() {
	// := only for new vars
	cards := []string{"test", newCard()}
	cards = append(cards, "six")
	for i, card := range cards {
		fmt.Println(card)
	}
	fmt.Println(cards)

}

func newCard() string {
	return "Five of Diamonds"
}