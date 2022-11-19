import base64
from django.conf import settings as config


def generate_password(formatted_time):

    data_to_encode = (
        config.MPESA_EXPRESS_SHORTCODE + config.MPESA_PASSKEY + formatted_time
    )

    encoded_string = base64.b64encode(data_to_encode.encode())

    decoded_password = encoded_string.decode("utf-8")

    return decoded_password