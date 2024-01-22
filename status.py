# Assuming color_code is a dictionary mapping status codes to color codes
color_code = {200: "\033[92m", 404: "\033[91m", 500: "\033[91m"}

def display_status(response):
    status = (
        f"{color_code.get(response.status_code, '')}Status: [{response.status_code}]\033[0m"
    )
    print(status)

# Example usage:
# Assuming you have a response object, replace it with the actual response object you have.
# For demonstration purposes, I'm using a dummy object with status code 200.
class DummyResponse:
    def __init__(self, status_code):
        self.status_code = status_code

response = DummyResponse(200)
display_status(response)
