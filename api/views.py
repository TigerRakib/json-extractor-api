from PIL import Image, UnidentifiedImageError
import base64
import io
from io import BytesIO
import json
from pyzbar.pyzbar import decode as decode_qr
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ExtractJSONFromImageView(APIView):
    def post(self, request):
        image_base64 = request.data.get("imageBase64")

        if not image_base64:
            return Response({
                "success": False,
                "data": None,
                "message": "Missing 'imageBase64' field"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            base64_data = image_base64.split(',')[1]

            # Fix padding if needed
            base64_data += '=' * (-len(base64_data) % 4)

            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_data)

            # Convert to string and parse JSON
            decoded_str = decoded_bytes.decode('utf-8')
            parsed_json = json.loads(decoded_str)
            return Response({
                "success": True,
                "data": parsed_json,
                "message": "Successfully extracted JSON from image"
            })

        except Exception as e:
            print("❌ ERROR:", str(e))
            return Response({
                "success": False,
                "data": None,
                "message": f"Error processing image: {str(e)}"
            }, status=400)
