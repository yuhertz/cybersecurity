import bleach
# type  "pip install bleach" into terminal or shell


def sanitize_input(user_input):
    # Allow only certain tags and attributes for safety
    allowed_tags = ['a', 'em', 'strong', 'b', 'i', 'u', 'p', 'br', 'ol', 'ul', 'li']
    allowed_attrs = {'a': ['href']}

    # Sanitize user input
    sanitized_input = bleach.clean(user_input, tags=allowed_tags, attributes=allowed_attrs)

    return sanitized_input

# Test the function
user_input = "<script>alert('XSS Attack!');</script>"
sanitized_input = sanitize_input(user_input)
print(sanitized_input)
