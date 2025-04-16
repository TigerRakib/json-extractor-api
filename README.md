
# 📦 JSON Extractor API from Base64-Encoded PNG (QR Embedded)

This project is a **Django REST API** that accepts a base64-encoded PNG image containing a QR code and extracts structured JSON data embedded in that QR code. It returns a clean JSON response with the extracted data.

---

## 🚀 Features

- ✅ Accepts base64-encoded PNG images via a POST endpoint
- 🔍 Decodes QR code embedded in the image
- 🧠 Parses and returns the extracted JSON data
- 📦 Clean and structured API response
- 🛠 Built using Django Rest Framework, Pillow, and pyzbar

---

## 📬 API Endpoint

### `POST /api/extract-data/`

#### Request Body

```json
{
  "imageBase64": "data:image/png;base64,<your-base64-encoded-image>"
}
```

#### Successful Response

```json
{
  "success": true,
  "data": {
    "name": "Jane Smith",
    "organization": "Beta Inc",
    "address": "456 Elm Ave",
    "mobile": "+1 555 5678"
  },
  "message": "Successfully extracted JSON from image"
}
```

#### Error Response

```json
{
  "success": false,
  "data": null,
  "message": "Error message here"
}
```

---

## 🧪 Testing the API

You can test the API using:

- **Postman**: Import the provided collection or send a `POST` request to `/api/extract-data/` with the base64 image.
- **Frontend UI**: A UI is provided to upload images and test the API visually (if hosted).

> ⚠️ *Due to personal constraints, testing on the hosted UI was not completed. However, the API has been thoroughly tested via Postman and works as expected.*

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/json-extractor-api.git
   cd json-extractor-api
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Server**
   ```bash
   python manage.py runserver
   ```

---

## 📦 Dependencies

- Django
- Django Rest Framework
- Pillow (PIL)
- pyzbar (QR code decoder)

---

## ✨ Example Base64 (for testing)

If you'd like a sample base64-encoded PNG image with embedded JSON QR code, you can generate it using any QR generator and convert the PNG to base64 using online tools.

---

## 🙋 Author Note

> I built this project as part of a coding challenge. Due to my father's illness and limited time, I was unable to complete testing on the hosted UI. However, the API has been fully validated using Postman and is functioning as expected.

---

## 📄 License

This project is licensed under the MIT License.
