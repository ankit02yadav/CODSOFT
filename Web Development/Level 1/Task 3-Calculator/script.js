let display = document.getElementById('display');
let currentInput = '';

function appendValue(val) {
    if (display.innerText === '0' && val !== '.') {
        currentInput = val;
    } else {
        currentInput += val;
    }
    display.innerText = currentInput;
}

function clearDisplay() {
    currentInput = '';
    display.innerText = '0';
}

function calculate() {
    try {
        currentInput = eval(currentInput).toString();
        display.innerText = currentInput;
    } catch {
        display.innerText = 'Error';
        currentInput = '';
    }
}