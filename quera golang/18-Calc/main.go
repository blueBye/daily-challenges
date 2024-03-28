package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"math"
	"net/http"
	"strconv"
	"strings"
)

type Server struct {
	Port string `json:"port"`
}

type Data struct {
	Result string `json:"result"`
	Error  string `json:"error"`
}

func NewServer(port string) *Server {
	server := &Server{port}
	return server
}

var ErrOverflow = errors.New("integer overflow")
var InvalidNumbersParam = errors.New("'numbers' parameter missing")

func Add64(left, right int64) (int64, error) {
	if right > 0 {
		if left > math.MaxInt64-right {
			return 0, ErrOverflow
		}
	} else {
		if left < math.MinInt64-right {
			return 0, ErrOverflow
		}
	}

	return left + right, nil
}

func parseParams(params string) ([]int64, error) {
	if params == "" {
		return nil, InvalidNumbersParam
	}

	numbersStr := strings.Split(params, ",")
	var numbers []int64

	for _, number := range numbersStr {
		n, err := strconv.Atoi(number)
		if err != nil {
			return nil, err
		}
		numbers = append(numbers, int64(n))
	}

	return numbers, nil
}

func add(w http.ResponseWriter, r *http.Request) {
	params := r.URL.Query().Get("numbers")
	data := Data{Result: "", Error: ""}
	w.Header().Set("Content-Type", "application/json")

	numbers, err := parseParams(params)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		data.Error = fmt.Sprintf("%v", err)
		json.NewEncoder(w).Encode(data)
		return
	}

	// perform operation
	sum := numbers[0]
	overflow := false
	for i := 1; i < len(numbers); i++ {
		temp, err := Add64(sum, numbers[i])
		if err != nil {
			overflow = true
			break
		}
		sum = temp
	}

	if overflow {
		w.WriteHeader(http.StatusBadRequest)
		data.Error = "Overflow"
	} else {
		data.Result = fmt.Sprintf("The result of your query is: %d", sum)
	}

	json.NewEncoder(w).Encode(data)
}

func sub(w http.ResponseWriter, r *http.Request) {
	params := r.URL.Query().Get("numbers")
	data := Data{Result: "", Error: ""}
	w.Header().Set("Content-Type", "application/json")

	numbers, err := parseParams(params)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		data.Error = fmt.Sprintf("%v", err)
		json.NewEncoder(w).Encode(data)
		return
	}

	// perform operation
	sum := numbers[0]
	overflow := false
	for i := 1; i < len(numbers); i++ {
		temp, err := Add64(sum, -numbers[i])
		if err != nil {
			overflow = true
			break
		}
		sum = temp
	}

	if overflow {
		w.WriteHeader(http.StatusBadRequest)
		data.Error = "Overflow"
	} else {
		data.Result = fmt.Sprintf("The result of your query is: %d", sum)
	}

	json.NewEncoder(w).Encode(data)
}

func (s *Server) Start() {
	http.HandleFunc("/add", add)
	http.HandleFunc("/sub", sub)

	err := http.ListenAndServe(":"+s.Port, nil)
	if err != nil {
		fmt.Println("Error:", err)
	}
}
