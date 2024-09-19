import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import pytest

# Constants
API_URL = "https://jsonplaceholder.typicode.com/posts"  # Example placeholder API for demonstration
WEB_FORM_URL = "https://example.com/contact-form"  # Replace with an actual URL that you want to use

@pytest.fixture
def setup():
  driver = webdriver.Chrome() # Ensure the Chrmoe WebDriver is in your PATH
  driver.maximize_window()
  yield driver
  driver.quit()

def test_api_get_request():
  """Fetch data from API, and validate the response."""
  response = requests.get(API.URL)
  assert response.status_code == 200, "API GET request failed."
  data = response.json()
  assert isinstance(data, list), "The expected list of posts"
  print(f"API returned {len(data)} items.")

def test_form_submission_with_api(setup):
    """Fill form using Selenium and validate with API data."""
    driver = setup
    
    # Read sample data from JSON
    with open('../resources/sample_form.json', 'r') as file:
        form_data = json.load(file)
    
    # Submit form using API request
    response = requests.post(API_URL, json=form_data)
    assert response.status_code == 201, "API POST request failed."
    api_response_data = response.json()
    print(f"Submitted data via API: {api_response_data}")

    # Simulate form submission using Selenium
    driver.get(WEB_FORM_URL)
    
    # Fill out the form using data from the sample JSON
    driver.find_element(By.NAME, "name").send_keys(form_data["name"])
    driver.find_element(By.NAME, "email").send_keys(form_data["email"])
    driver.find_element(By.NAME, "message").send_keys(form_data["message"])
    driver.find_element(By.ID, "submit").click()
    
    # Validate submission on frontend (e.g., check for a success message)
    success_message = driver.find_element(By.ID, "success").text
    assert "Thank you" in success_message, "Form submission failed on frontend."

    print("Form submitted successfully via Selenium, and validated on frontend!")
