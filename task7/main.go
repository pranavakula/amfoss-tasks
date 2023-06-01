package main
//serves entry point for the executable
import (
	"syscall/js"
)
//this imports the js package from the syscall package. This package provides functions for interacting with javascript in a webassembly environment.
var Count int
// global variable to store int value
func reset(this js.Value, args []js.Value) any {
	Count = 0
	document := js.Global().Get("document")
	document.Call("getElementById", "int").Set("innerHTML", Count)
	return 0
}
/* this 'reset' function takes two parameters. 'this js.Values' and 'args[]js.Value'
This function sets the count variable to 0 and updates the HTML element with 
the ID "int" to display the updated value of count*/

func inc(this js.Value, args []js.Value) any {
	Count = Count + 1

	document := js.Global().Get("document")
	document.Call("getElementById", "int").Set("innerHTML", Count)
	return 0

}
/*This function named 'inc' similar to 'reset', it increments the value of 'count'
by 1 and updates the HTML element with the ID "int" to display the updated value of 'count'.*/

func dec(this js.Value, args []js.Value) any {
	Count = Count - 1
	document := js.Global().Get("document")
	document.Call("getElementById", "int").Set("innerHTML", Count)
	return 0
}
/*This function named 'dec' similar to 'reset' and 'inc' it decrements the value or 'count'
by 1 and updates the HTML element with the ID "int" to display the updated value of 'count'.*/

func main() {
	js.Global().Set("reset", js.FuncOf(reset))
	js.Global().Set("inc", js.FuncOf(inc))
	js.Global().Set("dec", js.FuncOf(dec))
	select {}

}
/*This is the 'main' function, which serves as the entry point for the GO program. In this function, we set three JavaSript global 
functions: 'rest','inc' and 'dec'. We use the 'js.Global()' function to access the global object
in the JavaScript environment and attqch our functions to it. These functions are defined using 'js.FuncOf',
which wraps the Go functions 'reset','inc' and 'dec' to make them collable from JavaScript.
select{} which is blocking statement that keeps the Go program running indefinitely.*/
