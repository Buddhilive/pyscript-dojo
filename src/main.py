import arrr
import numpy as np
from pyscript import document

def load_ui():
    root_container = document.querySelector("#app-root")
    div_container = document.createElement("div")
    div_container.style = "display: flex; flex-direction: column; gap: 8px; width: 20%;"
    ui_input = r'<input type="text" name="english" id="english" placeholder="Type English here..." />'
    ui_button = r'<button py-click="translate_english">Translate</button>'
    ui_output = r'<textarea id="output"></textarea>'
    div_container.insertAdjacentHTML("afterbegin", ui_input + ui_button + ui_output)
    root_container.innerHTML = ""
    root_container.append(div_container)

def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    np_array = np.array([1, 2, 3, 4, 5, 6])
    output_div.innerText = arrr.translate(english)
    print(np_array)

def main():
    load_ui()

if __name__ == "__main__":
    main()