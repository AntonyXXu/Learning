package main

func main() {
	// := only for new vars
	cards := newDeck()
	hand, remainingDeck := deal(cards, 5)
	hand.print()
	remainingDeck.print()
	cards.saveToFile("my_cards")
}
