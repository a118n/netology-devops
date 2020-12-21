package main
import "fmt"

func main() {
	array := []int{48,96,86,68,57,82,63,70,37,34,83,27,19,97,9,17,}

 	smallestNumber := array[0]
 	for _, element := range array {
		if element < smallestNumber {
			smallestNumber = element
		}
	}
	fmt.Println("Smallest number is ", smallestNumber)
}
