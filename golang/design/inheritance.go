package main

import (
	"fmt"
)

// Base struct
type Pet struct {
	name string
}

// Method of the base struct
func (pet *Pet) GetName() string {
	return pet.name
}

// Derived struct Dog
type Dog struct {
	Pet
	weight int
}

// Method specific to Dog
func (dog *Dog) Bark() string {
	return "Woof!"
}

// Derived struct Cat
type Cat struct {
	Pet
	color string
}

// Method specific to Cat
func (cat *Cat) Meow() string {
	return "Meow!"
}

func main() {
	dog := Dog{
		Pet: Pet{name: "Charlie"},
		weight: 3,
	}
	cat := Cat{
		Pet: Pet{name: "Whiskers"},
		color: "Black",
	}

	// Accessing inherited method from Pet
	fmt.Println("Dog's name:", dog.GetName())
	// Accessing Dog's specific method
	fmt.Println("Dog's bark:", dog.Bark())
	// Accessing field from Dog
	fmt.Println("Dog's weight:", dog.weight)

	// Accessing inherited method from Pet
	fmt.Println("Cat's name:", cat.GetName())
	// Accessing Cat's specific method
	fmt.Println("Cat's meow:", cat.Meow())
	// Accessing field from Cat
	fmt.Println("Cat's color:", cat.color)
}
