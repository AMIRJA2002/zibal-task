from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('GOOGLE_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('GOOGLE_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
