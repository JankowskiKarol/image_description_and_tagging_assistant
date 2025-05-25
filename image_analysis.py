import requests
from config import azure_key, azure_endpoint

def analyze_image_azure(image_bytes):
    """
    Sends an image to the Azure Computer Vision API for analysis and returns a descriptiion and tags.

    This function uses the Azure Cognitive Services Computer Vision API
    to analyze the visual content of the given image. It extracts a textual description
    and a list of tags that represent the content of the image.

    Parameters:
        image_bytes (bytes): the image data.

    Returns:
        tuple:
            - description (str): a textual short caption describing the main content of the image.
            - tags (list): a list of tags, each representing a recognized element in the image.
              Each tag typically contains a 'name' and a 'confidence' value.

    Raises:
        requests.exceptions.HTTPError: if the API call fails or returns an error status code.
    """
    analyze_url = azure_endpoint + "vision/v3.2/analyze"
    
    params = {
        "visualFeatures": "Description,Tags",
        "language": "en"
    }
    
    headers = {
        "Ocp-Apim-Subscription-Key": azure_key,
        "Content-Type": "application/octet-stream"
    }
    
    response = requests.post(analyze_url, headers=headers, params=params, data=image_bytes)
    response.raise_for_status()
    analysis = response.json()
    description = analysis["description"]["captions"][0]["text"]
    tags = analysis["tags"]
    
    return description, tags