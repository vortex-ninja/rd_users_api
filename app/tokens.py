from rest_framework_jwt.settings import api_settings

# Handlers for creating token manually

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER