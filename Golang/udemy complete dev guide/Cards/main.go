package main

import "fmt"

func main() {
	// := only for new vars
	cards := newDeck()
	hand, remainingDeck := deal(cards, 5)
	hand.print()
	remainingDeck.print()
	fmt.Println(cards.toString())
}
