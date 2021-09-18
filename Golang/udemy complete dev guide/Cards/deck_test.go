package main

import "testing"

func TestNewDeck(t *testing.T) {
	d := newDeck()

	if len(d) < 4 {
		t.Errorf("Expected deck of more than 4 %v", len(d))
	}
}

func TestSaveToDeckAndNewDeckFromFile(t *testing.T) {
	os.Remove("_deckTesting")

	deck := newDeck()
	d.saveToFile("_deckTesting")

	loadedDeck := newDeckFromFile("_deckTesting")

	if len(loadedDeck) < 4 {
		t.Errorf("Expected deck of more than 4 %v", len(d))
	}

}