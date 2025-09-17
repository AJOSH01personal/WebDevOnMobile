#reverse string pgm in python for pyscript
from pyscript import document

def reverse_string(event):
    input_text = document.querySelector("#text_data")
    text_data = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = text_data[::-1]
    
#print("Python"[::-1])

