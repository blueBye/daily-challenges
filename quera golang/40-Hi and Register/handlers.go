package main

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

type Person struct {
	Firstname string `json:"firstname"`
	Lastname  string `json:"lastname"`
	Age       int    `json:"age"`
	Job       string `json:"job"`
}

var users = map[string]Person{}

func register(c *gin.Context) {
	var user Person

	user.Firstname = c.DefaultPostForm("firstname", "")
	user.Lastname = c.DefaultPostForm("lastname", "")
	user.Job = c.DefaultPostForm("job", "Unknown")

	age, err := strconv.Atoi(c.DefaultPostForm("age", "18"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": "age should be integer"})
		return
	}

	user.Age = age

	var header int
	var message string
	switch {
	case user.Firstname == "":
		header = http.StatusBadRequest
		message = "firtname is required"
	case user.Lastname == "":
		header = http.StatusBadRequest
		message = "lastname is required"
	case users[user.Firstname].Lastname == user.Lastname:
		message = fmt.Sprintf("%s %s registered before", user.Firstname, user.Lastname)
		header = http.StatusConflict
	default:
		message = fmt.Sprintf("%s %s registered successfully", user.Firstname, user.Lastname)
		header = http.StatusOK
		users[user.Firstname] = user
	}

	c.JSON(header, gin.H{"message": message})
}

func hello(c *gin.Context) {
	firstname := c.Param("firstname")
	lastname := c.Param("lastname")

	for _, u := range users {
		if u.Firstname == firstname {
			if u.Lastname == lastname {
				message := fmt.Sprintf("Hello %s %s; Job: %s; Age: %d", u.Firstname, u.Lastname, u.Job, u.Age)
				c.String(http.StatusOK, message)
				return
			}
		}
	}

	message := fmt.Sprintf("%s %s is not registered", firstname, lastname)
	c.String(http.StatusNotFound, message)
}
