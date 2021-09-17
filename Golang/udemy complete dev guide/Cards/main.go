package main

func main() {
	// := only for new vars
	cards := newDeckFromFile("my_cards")
	hand, remainingDeck := deal(cards, 5)
	hand.print()
	remainingDeck.print()
}
