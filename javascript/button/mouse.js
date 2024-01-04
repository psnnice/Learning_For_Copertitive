const digits = document.querySelectorAll('#b1, #b2, #b3, #b4, #b5, #b6, #b7, #b8, #b9, #b0, #bC, #bplus, #bminus, #bdivide, #bmultiply, #bequal ,#bdot')
const display = document.getElementById('display')

digits.forEach((digit, index) => {
    number = parseInt(digit.innerText)

    digit.addEventListener('click', () => {
        if (digit.innerText == "C")
        {
            display.innerText = "0"
        }
        else {
            if (display.innerText == "0")
            {
                display.innerText = ""
                
            }
            if (display.innerText == "+")
            {
                
            }
            display.textContent += digit.innerText
            
        }

    })
})
