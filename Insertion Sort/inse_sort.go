package main

import "fmt"

// Basic insertion sort
func insertionSort(arr []int) []int {
    result := make([]int, len(arr))
    copy(result, arr)
    for i := 1; i < len(result); i++ {
        key := result[i]
        j := i - 1
        for j >= 0 && result[j] > key {
            result[j+1] = result[j]
            j--
        }
        result[j+1] = key
    }
    return result
}
// Optimized insertion sort with performance tracking
func insertionSortOptimized(arr []int) ([]int, int, int) {
    if len(arr) <= 1 {  return arr, 0, 0 }
    result := make([]int, len(arr))
    copy(result, arr)
    comparisons := 0
    shifts := 0
    
    for i := 1; i < len(result); i++ {
        key := result[i]
        j := i - 1
        
        // Early exit: if key is already in correct position
        if result[j] <= key {
            comparisons++
            continue
        }
        
        // Shift elements and count operations
        for j >= 0 && result[j] > key {
            result[j+1] = result[j]
            comparisons++
            shifts++
            j--
        }
        
        result[j+1] = key
    }
    
    return result, comparisons, shifts
}

// Binary insertion sort
func binaryInsertionSort(arr []int) []int {
    result := make([]int, len(arr))
    copy(result, arr)
    
    // Binary search helper function
    var binarySearch func([]int, int, int, int) int
    binarySearch = func(arr []int, val, start, end int) int {
        if start == end {
            if arr[start] > val {
                return start
            }
            return start + 1
        }
        
        if start > end {
            return start
        }
        
        mid := (start + end) / 2
        
        if arr[mid] < val {
            return binarySearch(arr, val, mid+1, end)
        } else if arr[mid] > val {
            return binarySearch(arr, val, start, mid-1)
        } else {
            return mid
        }
    }
    
    for i := 1; i < len(result); i++ {
        key := result[i]
        // Find insertion point using binary search
        insertionPos := binarySearch(result, key, 0, i-1)
        
        // Shift elements
        for j := i; j > insertionPos; j-- {
            result[j] = result[j-1]
        }
        
        result[insertionPos] = key
    }
    
    return result
}

func main() {
    numbers := []int{5, 2, 4, 6, 1, 3}
    fmt.Println("Original array:", numbers)
    
    // Test basic insertion sort
    sortedArray := insertionSort(numbers)
    fmt.Println("Basic insertion sort:", sortedArray)
    
    // Test optimized insertion sort
    optimizedArray, comps, shifts := insertionSortOptimized(numbers)
    fmt.Printf("Optimized insertion sort: %v\n", optimizedArray)
    fmt.Printf("Performance: %d comparisons, %d shifts\n", comps, shifts)
    
    // Test binary insertion sort
    binaryArray := binaryInsertionSort(numbers)
    fmt.Println("Binary insertion sort:", binaryArray)
    
    // Verify original array is unchanged
    fmt.Println("Original unchanged:", numbers)
}
