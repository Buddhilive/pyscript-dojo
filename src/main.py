import arrr
import numpy as np
import pandas as pd
from pyscript import document
from io import BytesIO

def load_ui():
    root_container = document.querySelector("#app-root")
    div_container = document.createElement("div")
    div_container.style = "display: flex; flex-direction: column; gap: 8px; width: 20%;"
    ui_input = r'<input type="text" name="english" id="english" placeholder="Type English here..." />'
    ui_button = r'<button py-click="translate_english">Translate</button>'
    ui_output = r'<textarea id="output"></textarea>'
    upload_btn = r'<input type="file" py-change="get_file" />'
    console_div = r'<div id="console"></div>'
    div_container.insertAdjacentHTML("afterbegin", ui_input + ui_button + ui_output + upload_btn + console_div)
    root_container.innerHTML = ""
    root_container.append(div_container)

def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    np_array = np.array([1, 2, 3, 4, 5, 6])
    output_div.innerText = arrr.translate(english)
    print(np_array)

async def get_file(event):
    file_list = event.target.files
    first_item = file_list.item(0)

    file_bytes: bytes = await get_bytes_from_file(first_item)
    print(file_bytes[0]) # Do something with file contents

    csv_file = BytesIO(file_bytes) # Wrap in Python BytesIO file-like object

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert each row to a list and store them in an array
    rows_array = df.values.tolist()

    # Now, 'rows_array' contains each row of the CSV file as a list
    console_div = document.querySelector("#console")
    console_div.innerHTML = rows_array

async def get_bytes_from_file(file):
    array_buf = await file.arrayBuffer()
    return array_buf.to_bytes()

def main():
    load_ui()

if __name__ == "__main__":
    main()