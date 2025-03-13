import os
import sys
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, TrackingSettings, ClickTracking
from django.conf import settings

def load_html_template(template):
    try:
        if not str(template).endswith(".html"):
            template = f"{template}.html"
        
        with open(os.path.join("email_app", 'templates', template), 'r', encoding='utf-8') as file:
            return file.read()
    
    except FileNotFoundError as e:
        sys.stderr.write(f"Template file '{template}' not found: {str(e)}\n")
        return None

    except Exception as e:
        sys.stderr.write(f"Error loading template '{template}': {str(e)}\n")
        return None

def send_verify_email(to, subject, jwt):
    try:
        if not settings.FROM_EMAIL or not settings.API_KEY:
            raise ValueError("SendGrid credentials are missing!")

        html_template = load_html_template("account-verification")
        
        if html_template is None:
            return {"status_code": 500, "error": "Template 'verify-account' could not be loaded."}

        html_content = html_template.replace("{{ verification_link }}", f"{settings.API_GATEWAY_EXTERNAL_URL}/auth/api/v1/verify/{jwt}")

        message = Mail(from_email=settings.FROM_EMAIL, to_emails=to, subject=subject, html_content=html_content)
        message.tracking_settings = TrackingSettings(click_tracking=ClickTracking(enable=False, enable_text=False))
        
        response = SendGridAPIClient(settings.API_KEY).send(message)
        
        sys.stdout.write(f"SendGrid response status code: {response.status_code}\n")
        if response.status_code not in [200, 202]:
            return {"status_code": response.status_code, "error": f"Failed to send email. SendGrid response: {response.body}"}

        return {"status_code": response.status_code, "message": "Email sent successfully"}

    except Exception as e:
        sys.stderr.write(f"An error occurred: {str(e)}\n")
        return {"status_code": 500, "error": str(e)}
    
def send_password_reset(to, subject, jwt):
    try:
        if not settings.FROM_EMAIL or not settings.API_KEY:
            raise ValueError("SendGrid credentials are missing!")

        html_template = load_html_template("password-reset")
        
        if html_template is None:
            return {"status_code": 500, "error": "Template 'verify-account' could not be loaded."}

        html_content = html_template.replace("{{ reset_password_link }}", f"{settings.API_GATEWAY_EXTERNAL_URL}/auth/api/v1/reset-password/{jwt}")

        message = Mail(from_email=settings.FROM_EMAIL, to_emails=to, subject=subject, html_content=html_content)
        message.tracking_settings = TrackingSettings(click_tracking=ClickTracking(enable=False, enable_text=False))
        
        response = SendGridAPIClient(settings.API_KEY).send(message)
        
        sys.stdout.write(f"SendGrid response status code: {response.status_code}\n")
        if response.status_code not in [200, 202]:
            return {"status_code": response.status_code, "error": f"Failed to send email. SendGrid response: {response.body}"}

        return {"status_code": response.status_code, "message": "Email sent successfully"}

    except Exception as e:
        sys.stderr.write(f"An error occurred: {str(e)}\n")
        return {"status_code": 500, "error": str(e)}

