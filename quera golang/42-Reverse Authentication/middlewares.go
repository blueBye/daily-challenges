package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func authMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		username := c.Request.Header.Get("username")
		password := c.Request.Header.Get("password")

		if len(username) < 4 {
			c.JSON(http.StatusUnauthorized, gin.H{"message": "Unauthorized"})
			c.Abort()
			return
		}

		if len(username) != len(password) {
			c.JSON(http.StatusUnauthorized, gin.H{"message": "Unauthorized"})
			c.Abort()
			return
		}

		for idx, _ := range username {
			if username[idx] != password[len(password)-idx-1] {
				c.JSON(http.StatusUnauthorized, gin.H{"message": "Unauthorized"})
				c.Abort()
				return
			}
		}

		c.Next()
	}
}
