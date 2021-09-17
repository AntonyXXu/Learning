package main

import (
	"fmt"
	"strings"
)

type deck []string 

func newDeck() deck {
	var cards deck
	cardSuits := []string {"Spades", "Hearts", "Diamonds", "Clubs"}	
	cardValues := []string {"Ace", "Two", "Three", "Four"}
	for _, cardSuit := range cardSuits {
		for _, cardValue := range cardValues {
			cards = append(cards, cardValue + " of " + cardSuit)
		}
	}
	
	return cards
}

func (d deck) print() {
	for i, card:= range d {
		fmt.Println(i, card)
	}
}

func deal(d deck, handSize int) (deck, deck) {
	return d[:handSize], d[handSize:]
}

func (d deck) toString() string {
	return strings.Join([]string(d), ",")
}