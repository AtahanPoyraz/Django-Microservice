from __future__ import absolute_import, unicode_literals

import sys
from email_service.celery import app
from .sender import send_verify_email, send_password_reset

@app.task
def verify_email_task(to, subject, jwt):
    try:
        sys.stdout.write(f"Sending email to: {to} | Subject: {subject} | Jwt: {jwt}\n")
        response = send_verify_email(to, subject, jwt)

        sys.stdout.write(f"Email Task Response: {response}\n")
        if response["status_code"] in [200, 202]:
            return {"status_code": response["status_code"], "message": response.get("message", "Email sent successfully")}

        return {"status_code": response["status_code"], "error": response.get("error", "An error occurred")}

    except Exception as e:
        sys.stderr.write(f"An error occurred: {str(e)}\n")
        return {"status_code": 500, "error": f"Error occurred during email sending: {str(e)}"}

@app.task
def reset_password_email_task(to, subject, jwt):
    try:
        sys.stdout.write(f"Sending email to: {to} | Subject: {subject} | Jwt: {jwt}\n")
        response = send_password_reset(to, subject, jwt)

        sys.stdout.write(f"Email Task Response: {response}\n")
        if response["status_code"] in [200, 202]:
            return {"status_code": response["status_code"], "message": response.get("message", "Email sent successfully")}

        return {"status_code": response["status_code"], "error": response.get("error", "An error occurred")}

    except Exception as e:
        sys.stderr.write(f"An error occurred: {str(e)}\n")
        return {"status_code": 500, "error": f"Error occurred during email sending: {str(e)}"}
