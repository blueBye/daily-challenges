package main

import (
	"errors"
	"strconv"
	"strings"
)

type Player struct {
	name    string
	region  *Map
	channel chan string
}

type Message struct {
	sender  Player
	message string
}

type Map struct {
	players map[string]*Player
	channel chan Message
}

type Game struct {
	maps    map[string]*Map
	players map[string]*Player
}

func NewGame(mapIds []int) (*Game, error) { // given a valid list of map IDs, generate a new game
	game := &Game{
		maps:    make(map[string]*Map),
		players: make(map[string]*Player)}

	// check if mapIds are invalid, if not add them to game.maps
	for _, mapId := range mapIds {
		if mapId <= 0 {
			return nil, errors.New("map ID must be greater than zero")
		}
		if game.maps[strconv.Itoa(mapId)] != nil {
			return nil, errors.New("duplicate map IDs")
		}
		m := &Map{
			channel: make(chan Message, 100),
			players: make(map[string]*Player),
		}
		game.maps[strconv.Itoa(mapId)] = m

		// intitiate FanOut
		m.FanOutMessages()
	}

	return game, nil
}

func (g *Game) ConnectPlayer(name string) error { // given a name, add a new player to the game if no player with the same name already exists
	// warning: most likely nees a mutex to prevent multiple users from concurrently being connected

	// generate key name for game.players map by lower-casing the name
	lowerCaseName := strings.ToLower(name)

	// handling race condition while keeping the lock time minimum
	if g.players[lowerCaseName] != nil {
		return errors.New("player already exists")
	}

	player := &Player{
		name:    name,
		region:  nil,
		channel: make(chan string, 100),
	}

	g.players[lowerCaseName] = player
	return nil
}

func (g *Game) SwitchPlayerMap(name string, mapId int) error { // given a name and a map ID, switch the player's region to the map with the given (ignored) map
	// checking whether both player and map exist
	lowerCaseName := strings.ToLower(name)
	targetMap, _ := g.GetMap(mapId)
	targetPlayer, _ := g.GetPlayer(lowerCaseName)
	// handle invalid map ID
	if targetMap == nil {
		return errors.New("map not found")
	}

	// handle invalid player name
	if targetPlayer == nil {
		return errors.New("player not found")
	}

	// lock the player and map before changing the map
	if targetPlayer.region != nil {
		if targetPlayer.region == targetMap {
			return errors.New("player is already in this map")
		}
		// remove the player from current map
		delete(targetPlayer.region.players, lowerCaseName)
	}
	targetPlayer.region = targetMap
	targetMap.players[lowerCaseName] = targetPlayer
	return nil
}

func (g *Game) GetPlayer(name string) (*Player, error) { // given a name, return a pointer to the player with that name (ignore case)
	// since players can't be removed, we don't need to worry about race conditions
	lowerCaseName := strings.ToLower(name)
	player, ok := g.players[lowerCaseName]
	if ok {
		return player, nil
	}
	return nil, errors.New("player not found")
}

func (g *Game) GetMap(mapId int) (*Map, error) { // given a map ID, return a pointer to the map with that ID
	// since maps can't be removed, we don't need to worry about race conditions
	region, ok := g.maps[strconv.Itoa(mapId)]
	if ok {
		return region, nil
	}
	return nil, errors.New("map not found")
}

func (m *Map) FanOutMessages() { // forwards the messages from the map's channel to all the players in the map
	go func() {
		for {
			message := <-m.channel
			for _, player := range m.players {
				if player.GetName() != message.sender.GetName() {
					player.channel <- message.message
				}
			}
		}
	}()
}

func (p *Player) GetChannel() <-chan string { // given a player, return a channel to send messages to that player
	return p.channel
}

func (p *Player) SendMessage(msg string) error {
	if p.region == nil {
		return errors.New("player is not in a map")
	}

	message := strings.Title(strings.ToLower(p.name)) + " says: " + msg

	p.region.channel <- Message{sender: *p, message: message}

	return nil
}

func (p *Player) GetName() string {
	return p.name
}
