package main

import (
	"fmt"
)

type Animal interface {
    Voice() string
}

type dog struct {
    name string
}

func (m *dog) Voice() string {
    return "Bark"
}

func (m *dog) GetName() string{
    return m.name
}

func NewDog(name string) Animal {
    dog:=dog{name}
    return &dog
}

type cat struct {
    name string
}

func (m *cat) Voice() string {
    return "Meow"
}

func (m *cat) GetName() string{
    return m.name
}

func NewCat(name string) Animal {
    cat := cat{name}
    return &cat
}



func main() {
    a1 := NewDog("Charlie")
    realDog, ok := a1.(*dog)
    fmt.Println(ok, realDog.name)
    fmt.Println(a1.Voice())

    a2 := NewCat("Fluffy")
    realCat, ok := a2.(*cat)
    fmt.Println(ok, realCat.name)
    fmt.Println(a2.Voice())
}
