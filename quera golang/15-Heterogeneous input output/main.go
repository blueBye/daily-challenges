package main

import (
	"sync/atomic"
	"time"
)

type FutureResult struct {
	Done       atomic.Bool
	ResultChan chan string
}

type Task func() string

func Async(t Task) *FutureResult {
	// this is going to execute one Task without waiting for it to complete
	result := &FutureResult{ResultChan: make(chan string, 1)}
	result.Done.Store(false)

	go func() {
		execution_result := t()
		if !result.Done.Load() {
			result.Done.Store(true)
			result.ResultChan <- execution_result
		}
	}()

	return result
}

func AsyncWithTimeout(t Task, timeout time.Duration) *FutureResult {
	// this is going to execute one Task without waiting for it to complete within a time limit
	result := Async(t)

	go func() {
		select {
		case msg := <-result.ResultChan:
			result.ResultChan <- msg
		case <-time.After(timeout):
			if !result.Done.Load() {
				result.Done.Store(true)
				result.ResultChan <- "timeout"
			}
		}
	}()

	return result
}

func (fResult *FutureResult) Await() string {
	return <-fResult.ResultChan
}

func CombineFutureResults(fResults ...*FutureResult) *FutureResult {
	futureResult := &FutureResult{ResultChan: make(chan string, len(fResults))}
	for _, i := range fResults {
		futureResult.ResultChan <- i.Await()
	}
	return futureResult
}
