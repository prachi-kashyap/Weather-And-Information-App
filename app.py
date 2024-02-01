from flask import Flask, request, render_template
from weather_app import get_coordinates, get_weather  # Import weather functions
from image_generator import generate_image
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key if openai_api_key else "your-openai-api-key-here"

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    The main route for the Flask application. Handles both GET and POST requests.
    On POST request, processes the form data to either fetch weather data or generate text using OpenAI's GPT-3, 
    based on the user's action choice.

    Returns:
    Renders the index.html template with weather data, error messages, or generated text, as applicable.
    """
    weather = None
    error = None
    generated_text = None
    generated_image = None

    if request.method == 'POST':
        address = request.form.get('address')
        action = request.form.get('action')

        if action == 'get_weather':
            # Retrieve weather information
            location = get_coordinates(os.getenv('GOOGLE_MAPS_API_KEY'), address)
            if location:
                weather = get_weather(os.getenv('OPENWEATHER_API_KEY'), location['lat'], location['lng'])
            else:
                error = "Could not get location."
        elif action == 'generate_text_weather':
            # Generate text about the weather
            prompt = "Generate a creative text about weather."
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                n=1
            )
            generated_text = response.choices[0].text
        elif action == 'generate_text_place':
            # Generate text about the place
            if address:
                prompt = f"Generate a creative text about {address}."
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=100,
                    n=1
                )
                generated_text = response.choices[0].text
            else:
                generated_text = "Please enter a location to generate text about."

        elif action == 'generate_image':
            # New functionality to generate an image
            if address:
                image_prompt = f"An artistic representation of {address}"
                generated_image = generate_image(image_prompt)
            else:
                error = "Please enter a location to generate an image about."

    return render_template('index.html', weather=weather, error=error, generated_text=generated_text, generated_image=generated_image)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
