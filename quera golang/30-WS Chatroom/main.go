package main

import (
	"fmt"

	"github.com/gorilla/websocket"
	"github.com/labstack/echo/v4"
)

type Room struct {
	users map[string]*websocket.Conn
}

var rooms = map[string]Room{}
var upgrader = websocket.Upgrader{}

func wsChatRoom(c echo.Context) error {
	roomId := c.Param("roomId")
	username := c.Param("username")

	ws, err := upgrader.Upgrade(c.Response(), c.Request(), nil)
	if err != nil {
		return err
	}
	defer ws.Close()

	_, ok := rooms[roomId]
	if !ok {
		rooms[roomId] = Room{users: map[string]*websocket.Conn{}}
	}
	rooms[roomId].users[username] = ws

	for {
		_, msg, err := ws.ReadMessage()
		if err != nil {
			break
		}

		room := rooms[roomId]
		message := []byte(fmt.Sprintf("%s: %s", username, msg))

		for user, conn := range room.users {
			if user != username {
				conn.WriteMessage(websocket.TextMessage, message)
			}
		}
	}

	return nil
}

func main() {
	e := echo.New()
	e.GET("/ws/chat/:roomId/user/:username", wsChatRoom)
	e.Logger.Fatal(e.Start(":8080"))
}
