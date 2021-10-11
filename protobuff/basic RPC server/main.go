package main

import "fmt"

type Item struct {
	title string
	body  string
}

var database []Item

func GetByName(title string) Item {
	var getItem Item
	for _, val := range database {
		if val.title == title {
			getItem = val
		}
	}
	return getItem
}

func CreateItem(item Item) Item {
	database = append(database, item)
	return item
}

func AddItem(item Item) Item {
	database = append(database, item)
	return item
}

func editItem(title string, edit Item) Item {
	var changedItem Item

	for index, val := range database {
		if val.title == edit.title {
			database[index] = edit
			changedItem = edit
		}
	}

	return changedItem
}

func deleteItem(item Item) Item {
	var delItem Item
	for index, val := range database {
		if val.title == item.title && val.body == item.body {
			database = append(database[:index], database[index+1:]...)
			delItem = item
			break
		}
	}
	return delItem
}

func main() {
	fmt.Println("initial database: ", database)
	a := Item{"first", "a test item"}
	b := Item{"second", "a second item"}
	c := Item{"third", "a third item"}

	AddItem(a)
	AddItem(b)
	AddItem(c)
	fmt.Println("second database: ", database)

	deleteItem(b)
	fmt.Println("third database: ", database)

	editItem("third", Item{"fourth", "a new item"})
	fmt.Println("fourth database: ", database)

	x := GetByName("fourth")
	y := GetByName("first")
	fmt.Println(x, y)
}