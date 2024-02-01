# image_generator.py
# This script contains a function to generate images using OpenAI's API.

import openai

def generate_image(prompt):
    """
    Generates an image based on the provided text prompt using OpenAI's Image API.

    Parameters:
    prompt (str): The text prompt to generate the image from.

    Returns:
    str: The URL of the generated image if successful.
    None: If the image generation fails or encounters an error.
    """
    try:
        # Call OpenAI's Image API with the given prompt, requesting one image of specified size
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size="1024x1024"  # Size of the generated image
        )
        # Extract the URL of the generated image from the response
        image_url = response.data[0].url  # Adjust as per actual response structure
        return image_url
    except Exception as e:
        # Print the error message if the API call fails
        print(f"Error generating image: {e}")
        return None
