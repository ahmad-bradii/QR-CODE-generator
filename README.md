# QR Code Generator 🧾

This Python script generates a QR code from a user-provided website URL and saves it as an image file in a specified folder.

---

## 📌 Features

- Takes a website URL as input.
- Generates a QR code using the `qrcode` library.
- Saves the QR code image to a local folder.
- Automatically names the file based on the domain of the URL.

---

## 🧠 How It Works

1. User is prompted to enter a URL.
2. The QR code is generated using `qrcode.QRCode`.
3. The image is saved to:
./QR CODE generator/QR CODES/

yaml
Copy
Edit
with a filename based on the website’s domain.

---

## 🛠️ Technologies Used

- Python 3
- [qrcode](https://pypi.org/project/qrcode/)
- `os` (built-in module)

---

## ▶️ Usage
To generate a QR code:
1.create a folderin the /QR CODE generator : 
``` bash
cd ./QR CODE generator
mkdir "QR CODES"

```
2. Install the `qrcode` library with PIL support: 
``` bash
pip install qrcode[pil]
```
3. Run your Python script:
   
``` bash
python main.py
```
4. Enter the URL when prompted.

The QR code will be saved in the `QR CODE generator/QR CODES/` directory. For example, entering `https://www.google.com` will save the image as `QR CODE generator/QR CODES/google.png`
