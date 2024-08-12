from js import document

def calculate_currency():
    input_value = document.querySelector(".text-input input").value

    from_unit = document.querySelector(".from_unit").textContent.lower()
    to_unit = document.querySelector(".to_unit").textContent.lower()

    if(from_unit == "azn" and to_unit == "usd"):
        converted_value = float(input_value)*1.7 

    symbol = "$"

    document.querySelector("#converted-value").value = f"{converted_value}{symbol}"

    

convert_button = document.querySelector(".convert-icon")

convert_button.onclick = lambda event: calculate_currency()


