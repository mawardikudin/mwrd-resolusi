# validasi email
def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]

