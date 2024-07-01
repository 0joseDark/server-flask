# config.py

class Config:
    SECRET_KEY = 'your_secret_key_here'
    # Configurações de e-mail para Flask-Mail
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your-mailtrap-username'
    MAIL_PASSWORD = 'your-mailtrap-password'
    MAIL_DEFAULT_SENDER = 'your-email@example.com'
