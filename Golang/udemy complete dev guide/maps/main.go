package main

import "fmt"

type color map[string]string

func main() {
	colors := map[string]string{
		"red":   "ff0000",
		"green": "ff0001",
		"white" : "ffffff",
	}

	colors2 := make(map[string]string)
	colors2["white"] = "ffffff"

	delete(colors2, "white")

	fmt.Println(colors)
	fmt.Println(colors2)

	printMap(colors)
	color(colors).print()

}

func printMap(c map[string]string) {
	for key, value := range c {
		fmt.Println(key, value)
	}
}

func (c color) print() {
	for key, value := range c {
		fmt.Println(key, value)
	}
}