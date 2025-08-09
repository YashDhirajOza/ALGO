package main

import "fmt"

func bubblesort(arr []int) []int { // function name should match usage in main
	n := len(arr)
	// giving n the size of arr
	// making a new dynamic array( slice)
	// using fucntion make( what type of array we want, what size do we want)
	// in this case we want a slice of int and size of arr arraay
	result := make([]int, len(arr))
	copy(result, arr)
	for i := 0; i < n; i++ {
		for j := 0; j < n-1; j++ {
			if result[j] > result[j+1] {
				result[j], result[j+1] = result[j+1], result[j] // should swap with result[j], not result[i]
			}
		}
	}
	return result
}

// optimize bubble sort
func better_sort(arr []int) []int { // typo: 'fucn' should be 'func'
	n := len(arr)
	result := make([]int, len(arr))
	copy(result, arr)
	for i := 0; i < n; i++ {
		swapped := false
		for j := 0; j < n-i-1; j++ {
			if result[j] > result[j+1] {
				result[j], result[j+1] = result[j+1], result[j]
				swapped = true
			}
		}
		if !swapped { // 'break' should be inside the outer loop, not after it
			break
		}
	}
	return result
}
func main() {
	// Example usage
	numbers := []int{64, 34, 25, 12, 22, 11, 90}
	fmt.Println("Original array:", numbers)

	sortedArray := bubblesort(numbers) // function name should match definition
	fmt.Println("Sorted array (basic):", sortedArray)

	sortedArrayOpt := better_sort(numbers) // function name should match definition
	fmt.Println("Sorted array (optimized):", sortedArrayOpt)

	fmt.Println("Original still unchanged:", numbers)
}
