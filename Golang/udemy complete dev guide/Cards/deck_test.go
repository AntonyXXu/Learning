package main

import "testing"

func TestNewDeck(t *testing.T) {
	d := newDeck()

	if len(d) < 4 {
		t.Errorf("Expected deck of more than 4 %v", len(d))
	}
}