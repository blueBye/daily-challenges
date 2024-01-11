package main

import (
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

func simpleTask() string {
	time.Sleep(1 * time.Second)
	return "result"
}

func TestSimple(t *testing.T) {
	fResult := Async(simpleTask)
	assert.False(t, fResult.Done.Load())
	result := fResult.Await()
	assert.Equal(t, "result", result)
	assert.True(t, fResult.Done.Load())
}

func handleTimeout(d time.Duration, t *testing.T) func() {
	start := time.Now()
	return func() {
		elapsed := time.Since(start)
		if elapsed > d {
			t.FailNow()
		}
	}
}

func TestMultiple(t *testing.T) {
	defer handleTimeout(1100*time.Millisecond, t)()

	fResult1 := Async(simpleTask)
	fResult2 := Async(simpleTask)

	res1 := fResult1.Await()
	res2 := fResult2.Await()

	assert.Equal(t, "result", res1)
	assert.Equal(t, "result", res2)
}

func TestCombine(t *testing.T) {
	fResult1 := Async(simpleTask)
	fResult2 := Async(simpleTask)

	combinedFResult := CombineFutureResults(fResult1, fResult2)

	// first item
	select {
	case <-time.After(1100 * time.Millisecond):
		t.FailNow()

	case res := <-combinedFResult.ResultChan:
		assert.Equal(t, "result", res)
	}

	// second item should be availble fast
	select {
	case <-time.After(100 * time.Millisecond):
		t.FailNow()

	case res := <-combinedFResult.ResultChan:
		assert.Equal(t, "result", res)
	}
}

func TestMassiveCombine(t *testing.T) {
	count := 100
	fResults := []*FutureResult{}
	for i := 0; i < count; i++ {
		fResults = append(fResults, Async(simpleTask))
	}

	combinedFResult := CombineFutureResults(fResults...)

	// first item
	select {
	case <-time.After(1100 * time.Millisecond):
		t.FailNow()

	case res := <-combinedFResult.ResultChan:
		assert.Equal(t, "result", res)
	}

	// other items
	for i := 1; i < count; i++ {
		select {
		case <-time.After(100 * time.Millisecond):
			t.FailNow()

		case res := <-combinedFResult.ResultChan:
			assert.Equal(t, "result", res)
		}
	}
}

func TestTimeout(t *testing.T) {
	fResult := AsyncWithTimeout(simpleTask, 1200*time.Millisecond)

	select {
	case <-time.After(1800 * time.Millisecond):
		t.FailNow()

	case res := <-fResult.ResultChan:
		assert.Equal(t, "result", res) // timeout is reached before 800ms
		assert.True(t, fResult.Done.Load())
	}
}

func TestTimeoutFail(t *testing.T) {
	fResult := AsyncWithTimeout(simpleTask, 700*time.Millisecond)

	select {
	case <-time.After(800 * time.Millisecond):
		t.FailNow()

	case res := <-fResult.ResultChan:
		assert.Equal(t, "timeout", res) // timeout is reached before 800ms
	}
}

func TestCombineWithTimeout(t *testing.T) {
	fResult1 := AsyncWithTimeout(simpleTask, 700*time.Millisecond)
	fResult2 := AsyncWithTimeout(simpleTask, 1200*time.Millisecond)

	combinedFResult := CombineFutureResults(fResult1, fResult2)

	// first item
	select {
	case <-time.After(1100 * time.Millisecond):
		t.FailNow()

	case res := <-combinedFResult.ResultChan:
		assert.Equal(t, "timeout", res)
	}

	// second item should be availble fast
	select {
	case <-time.After(100 * time.Millisecond):
		t.FailNow()

	case res := <-combinedFResult.ResultChan:
		assert.Equal(t, "result", res)
		assert.True(t, fResult2.Done.Load())
	}
}

// func TestMassiveCombineWithTimeout(t *testing.T) {
// 	count := 10
// 	fResults := []*FutureResult{}

// 	start := time.Now()
// 	for i := 0; i < count; i++ {
// 		fResults = append(fResults, AsyncWithTimeout(simpleTask, 700*time.Millisecond))
// 	}
// 	fmt.Printf(">>>> it took %f seconds to finish loop\n", time.Since(start).Seconds())
// 	combinedFResult := CombineFutureResults(fResults...)
// 	fmt.Printf(">>>> it took %f seconds to combine results\n", time.Since(start).Seconds())

// 	// first item
// 	select {
// 	case <-time.After(1100 * time.Millisecond):
// 		t.FailNow()

// 	case res := <-combinedFResult.ResultChan:
// 		assert.Equal(t, "timeout", res)
// 	}

// 	// other items
// 	for i := 1; i < count; i++ {
// 		select {
// 		case <-time.After(100 * time.Millisecond):
// 			t.FailNow()

// 		case res := <-combinedFResult.ResultChan:
// 			assert.Equal(t, "timeout", res)
// 			assert.False(t, fResults[i].Done.Load())
// 		}
// 	}
// }
