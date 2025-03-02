package main

import (
    "net/http"
    "log"
)

func main() {
    http.HandleFunc("/", handler)
    log.Println("Server starting on :8080")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatal(err)
    }
}

func handler(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Welcome to the Atlas-X server!"))
}