package main

import (
	"fmt"
	"net/http"
)


func main() {
	// links are running awaiting previous lines, asynchronous
	sites := []string{
		"http://facebook.com",
		"http://google.com",
		"http://amazon.com",
		"http://golang.org",
	}

	c := make(chan string)

	for _, site := range sites {
		// only put go in front of function calls
		go checkLink(site, c)
	}
	for s := range c {
		go checkLink(s, c)
	}
}

func checkLink(site string, c chan string) bool {
	_, err := http.Get(site)
	if err != nil {
		fmt.Println(site, " offline")
		c <- site
		return false
	}

	fmt.Println(site, " online")
	c <- site
	return true
} 