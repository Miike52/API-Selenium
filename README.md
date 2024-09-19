# API-Selenium
Combining API and Selenium for Frontend / Backend validation.

## Overview
This is a simple project that will demonstrate automated testing using Selenium for browser automation, and API testing using the `requests` library.

## Prerequisites
- Python 3.x
- Chrome WebDriver installed and added to PATH
- Required libraries (you can install these with `pip install -r requirements.txt`)

## How to run the Tests
1. Clone the repository.
2. Navigate to the project folder.
3. Install dependencies using:
   ```bash
   pip install -r requirements.txt

Then, just run the tests using ``tests/test_api_integration.py`` :)

## Resources

- `resources/sample_form.json`: Contains sample data for form submissions. This JSON file is used to provide data for both API requests and Selenium form submissions. Example of its contents:

  ```json
  {
    "name": "Test User",
    "email": "testuser@example.com",
    "message": "This is a test message."
  }
