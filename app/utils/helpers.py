def format_response(data):
    # Function to format the response data
    return {"data": data}


def handle_error(error):
    # Function to handle errors and return a standardized error response
    return {"error": str(error)}


def log_message(message):
    # Function to log messages for debugging or information purposes
    print(message)
