def validate_email(email):
    if "@" not in email:
          raise ValueError("invalid Error")
    if len(email)>=8:
        return True
    return False
  
