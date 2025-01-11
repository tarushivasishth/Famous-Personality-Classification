import base64
with open(r".\test_images\virat1.jpg", "rb") as img_file:
    encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
print(encoded_string)
