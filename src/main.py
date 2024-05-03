import arrr
from pyscript import document

def load_ui():
    root_container = document.querySelector("#app-root")
    ui_temp = r'<input type="text" name="english" id="english" placeholder="Type English here..." />' + r'<button py-click="translate_english">Translate</button>' + r'<div id="output"></div>'

    root_container.insertAdjacentHTML("afterbegin", ui_temp)

def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)

def main():
    load_ui()

if __name__ == "__main__":
    main()