package main

import (
    "log"
    "net/http"
)

func main() {
    // Initialize the server
    http.HandleFunc("/", handler)
    log.Println("Starting server on :8080")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatal(err)
    }
}

// handler function to handle incoming requests
func handler(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Welcome to the Atlas-X Go server!"))
}