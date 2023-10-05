document.addEventListener("DOMContentLoaded", function () {
    const display = document.querySelector(".calculator__display");
    const buttons = document.querySelectorAll(".calculator-key");
    const operatorButtons = document.querySelectorAll(".operator-key");
    const calculateButton = document.querySelector(".key--equal");
    const clearButton = document.querySelector("[data-action='clear']");

    let currentInput = "";
    let currentOperator = "";
    let currentResult = 0;

    function updateDisplay() {
        display.textContent = currentInput;
    }

    function resetCalculator() {
        currentInput = "";
        currentOperator = "";
        currentResult = 0;
        updateDisplay();
    }

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const value = button.dataset.value;
            if (value === "AC") {
                resetCalculator();
            } else if (value === "+" || value === "-" || value === "×" || value === "÷") {
                currentOperator = value;
                currentResult = parseFloat(currentInput);
                currentInput = "";
            } else if (value === "=") {
                if (currentOperator) {
                    switch (currentOperator) {
                        case "+":
                            currentResult += parseFloat(currentInput);
                            break;
                        case "-":
                            currentResult -= parseFloat(currentInput);
                            break;
                        case "×":
                            currentResult *= parseFloat(currentInput);
                            break;
                        case "÷":
                            if (parseFloat(currentInput) === 0) {
                                alert("Divisão por zero não é permitida.");
                                resetCalculator();
                                return;
                            }
                            currentResult /= parseFloat(currentInput);
                            break;
                    }
                    currentOperator = "";
                    currentInput = currentResult.toString();
                }
            } else {
                currentInput += value;
            }
            updateDisplay();
        });
    });

    clearButton.addEventListener("click", resetCalculator);
});
