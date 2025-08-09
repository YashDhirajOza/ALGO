package main
import "fmt"

func sillySort(arr []int) []int {
    n := len(arr)
    // Create a copy to avoid modifying original slice
    result := make([]int, len(arr))
    copy(result, arr)
    // Selection sort implementation
    for i := 0; i < n; i++ {
        minIdx := i  // Index of minimum element
        // Find minimum element in remaining unsorted array
        for j := i + 1; j < n; j++ {
            if result[j] < result[minIdx] {
                minIdx = j
            }
        }
        // Swap minimum element with first element of unsorted portion
        if minIdx != i {
            result[i], result[minIdx] = result[minIdx], result[i]
        }
    }
    return result
}
func main() {
    numbers := []int{64, 25, 12, 22, 11}
    fmt.Println("Original array:", numbers)
    sorted := sillySort(numbers)
    fmt.Println("Sorted array:", sorted)
    fmt.Println("Original unchanged:", numbers)
}
