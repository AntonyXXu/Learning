package main

func main() {
	// := only for new vars
	cards := deck{"test", newCard()}
	cards = append(cards, "six")
	cards.print()
}

func newCard() string {
	return "Five of Diamonds"
}