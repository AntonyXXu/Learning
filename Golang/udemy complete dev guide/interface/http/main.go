package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	resp, err := http.Get("http://google.com")
	if err!=nil {
		os.Exit(1)
	}
	data := make([]byte, 99999)
	resp.Body.Read(data)
	fmt.Println(string(data))
}