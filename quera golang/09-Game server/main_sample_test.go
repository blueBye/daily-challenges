package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSampleGameCreation(t *testing.T) {
	g, err := NewGame([]int{})
	assert.Nil(t, err)
	assert.NotNil(t, g)
}

func TestSampleAddPlayer(t *testing.T) {
	g, err := NewGame([]int{1, 2, 3})
	assert.Nil(t, err)

	err = g.ConnectPlayer("Cyn")
	assert.Nil(t, err)
}

func TestSampleGetPlayer(t *testing.T) {
	g, err := NewGame([]int{1, 2, 3})
	assert.Nil(t, err)

	err = g.ConnectPlayer("Cyn")
	assert.Nil(t, err)

	p, err := g.GetPlayer("CyN")
	assert.Nil(t, err)
	assert.NotNil(t, p)
}

func TestInvalidMaps(t *testing.T) {
	g, err := NewGame([]int{1, 1, 3})
	assert.NotNil(t, err)
	assert.Nil(t, g)

	g, err = NewGame([]int{0, 1, 3})
	assert.NotNil(t, err)
	assert.Nil(t, g)
}

func TestGetMaps(t *testing.T) {
	g, _ := NewGame([]int{1, 2, 3})
	_, err := g.GetMap(1)
	assert.Nil(t, err)

	_, err = g.GetMap(0)
	assert.NotNil(t, err)

	_, err = g.GetMap(4)
	assert.NotNil(t, err)
}

func TestSwitchMap(t *testing.T) {
	g, _ := NewGame([]int{1, 2, 3})

	g.ConnectPlayer("alice")
	alice, _ := g.GetPlayer("ALiCe")

	err := g.SwitchPlayerMap("Alice", 1)
	assert.Nil(t, err)

	err = g.SwitchPlayerMap("Alice", 1)
	assert.NotNil(t, err)

	err = g.SwitchPlayerMap("Alice", 4)
	assert.NotNil(t, err)

	err = g.SwitchPlayerMap("Alice", 2)
	assert.Nil(t, err)

	m, _ := g.GetMap(2)
	contains := false
	for _, p := range m.players {
		if p == alice {
			contains = true
		}
	}
	assert.True(t, contains)
}

func TestMessaging(t *testing.T) {
	g, _ := NewGame([]int{1, 2, 3})
	g.ConnectPlayer("alice")
	g.ConnectPlayer("bob")

	alice, _ := g.GetPlayer("alice")
	bob, _ := g.GetPlayer("bob")

	g.SwitchPlayerMap("alice", 1)
	g.SwitchPlayerMap("bob", 1)

	bob.SendMessage("hi alice!")
	bob.SendMessage("hi again!")

	message := <-alice.channel
	assert.Equal(t, message, "Bob says: hi alice!")

	message = <-alice.channel
	assert.Equal(t, message, "Bob says: hi again!")
}
