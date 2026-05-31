package main

import (
	"fmt"
	"time"
)

func main() {
	inicio := time.Now()

	// Un ciclo simple de prueba
	contador := 0
	for i := 0; i < 100000000; i++ {
		contador++
	}

	duracion := time.Since(inicio)
	fmt.Printf("Tiempo en Go: %v\n", duracion)
}
