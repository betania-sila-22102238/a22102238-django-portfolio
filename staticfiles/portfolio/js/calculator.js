document.addEventListener("DOMContentLoaded", function () {
    // Funções da calculadora
    window.Solve = function (val) {
        const display = document.getElementById('res');
        if (display.value === "0") {
            display.value = val;
        } else {
            display.value += val;
        }
    };

    window.Result = function () {
        const display = document.getElementById('res');
        try {
            display.value = eval(display.value);
        } catch (e) {
            display.value = "Erro";
        }
    };

    window.Clear = function () {
        document.getElementById('res').value = "0";
    };

    window.Back = function () {
        const display = document.getElementById('res');
        display.value = display.value.slice(0, -1);
        if (display.value === "") {
            display.value = "0";
        }
    };
});
