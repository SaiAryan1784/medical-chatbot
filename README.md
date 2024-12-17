# Medical Chatbot

This is a medical chatbot built using Gradio and Hugging Face's models, powered by the `InferenceClient` from the Hugging Face Hub. The chatbot provides information on medical topics and can assist with general health inquiries. It is designed to be a helpful tool for users to get suggestions based on their symptoms, but **it is not a substitute for professional medical advice**.

## Features

- **Medical Q&A**: Users can ask medical questions, and the chatbot will provide helpful information and suggestions.
- **Streaming Responses**: The chatbot supports streaming responses to ensure a smooth and interactive experience.
- **Gradio Interface**: A simple and user-friendly web interface for interacting with the chatbot.

## Prerequisites

To run the chatbot locally, you need to have the following:

- Python 3.7 or later
- Hugging Face API key (sign up at [Hugging Face](https://huggingface.co/))

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/SaiAryan1784/medical-chatbot.git
    cd medical-chatbot
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set your Hugging Face API key:

    You can set your Hugging Face API token as an environment variable or in a `.env` file:

    ```bash
    export HF_API_KEY="your_huggingface_api_key"
    ```

    Or add it directly in the code where `InferenceClient` is initialized (not recommended for production).

## Usage

To run the chatbot:

1. Run the Python script:

    ```bash
    python app.py
    ```

2. The Gradio interface will be launched locally, and you can interact with the chatbot through your browser.

3. Open your browser and go to `http://127.0.0.1:7860` to start chatting with the medical chatbot.

## Example Interaction

**User**: I have a fever, suggest a cure.  
**Bot**: Here are some suggestions to help manage a fever:
- Drink plenty of fluids to stay hydrated.
- Take over-the-counter medication like acetaminophen or ibuprofen.
- Rest and monitor your symptoms.
- Seek medical attention if the fever persists or is very high.

## Contributing

Feel free to open issues or submit pull requests if you have improvements, bug fixes, or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This chatbot is meant for general informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a healthcare provider for any medical concerns.
