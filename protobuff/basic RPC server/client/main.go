package main

import (
	"fmt"
	"log"
	"net/rpc"
)

type Item struct {
	Title string
	Body  string
}

func main() {
	var reply Item
	var database []Item

	client, err := rpc.DialHTTP("tcp", "localhost:4040")
	if err != nil {
		log.Fatal("Connection Error: ", err)
	}

	a := Item{"First", "A first Item"}
	b := Item{"Second", "A Second Item"}
	c := Item{"Third", "A Third Item"}

	client.Call("API.AddItem", a, &reply)
	client.Call("API.AddItem", b, &reply)
	client.Call("API.AddItem", c, &reply)
	client.Call("API.GetDatabase", "", &database)
	
	fmt.Println("database: ", database)

	client.Call("API.EditItem", Item{"Second", "A new second item"}, &reply)

	client.Call("API.DeleteItem", c, &reply)
	client.Call("API.GetDB", "", &database)
	fmt.Println("updated Database: ", database)

	client.Call("API.GetByName", "First", &reply)
	fmt.Println("first item: ", reply)
}