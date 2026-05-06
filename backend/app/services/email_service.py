import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from html import escape

from app.config import settings
from app.utils.logger import logger


async def send_confirmation_email(to_email: str, token: str, full_name: str = "") -> bool:
    try:
        confirmation_url = f"{settings.FRONTEND_URL}/confirm/{token}"
        subject = "Email Confirmation"
        greeting = f"Hello {escape(full_name)}," if full_name else "Hello,"
        html_content = f"""
        <html>
            <body>
                <h2>Email Confirmation</h2>
                <p>{greeting}</p>
                <p>Please click the link below to confirm your email:</p>
                <a href="{confirmation_url}">Confirm Email</a>
                <p>Or copy this link: {confirmation_url}</p>
                <p>This link will expire in 24 hours.</p>
            </body>
        </html>
        """

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = settings.SENDER_EMAIL
        message["To"] = to_email

        part = MIMEText(html_content, "html")
        message.attach(part)

        async with aiosmtplib.SMTP(hostname=settings.SMTP_SERVER, port=settings.SMTP_PORT) as smtp:
            await smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            await smtp.send_message(message)

        logger.info(f"Confirmation email sent to {to_email}")
        return True
    except Exception as e:
        logger.error(f"Failed to send confirmation email: {str(e)}")
        return False


async def send_welcome_email(to_email: str, full_name: str) -> bool:
    try:
        subject = "Welcome to Email Confirmation System"
        escaped_name = escape(full_name)
        html_content = f"""
        <html>
            <body>
                <h2>Welcome, {escaped_name}!</h2>
                <p>Your email has been successfully confirmed.</p>
                <p>You can now access your dashboard.</p>
            </body>
        </html>
        """

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = settings.SENDER_EMAIL
        message["To"] = to_email

        part = MIMEText(html_content, "html")
        message.attach(part)

        async with aiosmtplib.SMTP(hostname=settings.SMTP_SERVER, port=settings.SMTP_PORT) as smtp:
            await smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            await smtp.send_message(message)

        logger.info(f"Welcome email sent to {to_email}")
        return True
    except Exception as e:
        logger.error(f"Failed to send welcome email: {str(e)}")
        return False
