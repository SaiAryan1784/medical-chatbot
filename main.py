import gradio as gr
from huggingface_hub import InferenceClient

# Initialize the InferenceClient with your Hugging Face API key
client = InferenceClient(api_key="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")

def query_huggingface_api(payload):
    """
    Sends a request to Hugging Face API using InferenceClient for a streaming response.
    
    Args:
        payload (dict): The input payload for the model.
    
    Returns:
        str: The model's response or an error message.
    """
    try:
        # Define the messages for the chat completion
        messages = [{"role": "user", "content": payload['inputs']}]

        # Streaming the response from the model
        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct", 
            messages=messages, 
            temperature=0.6,
            max_tokens=1024,
            top_p=0.7
        )

        # Collecting and extracting the response content
        response_text = completion.choices[0].message['content']

        return response_text

    except Exception as e:
        return f"Error: {str(e)}"

def medical_chatbot(input_text):
    """
    Handles user input, queries the Hugging Face model, and returns the response.

    Args:
        input_text (str): The user's question or input.

    Returns:
        str: The chatbot's response.
    """
    # Define the payload for the API
    payload = {"inputs": input_text}

    # Query the Hugging Face API and return the response
    return query_huggingface_api(payload)

# Create the Gradio interface for the chatbot
interface = gr.Interface(
    fn=medical_chatbot,
    inputs=gr.Textbox(label="Enter your medical question or query"),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Medical Chatbot",
    description="This chatbot provides information on medical topics. For professional advice, consult a healthcare provider.",
)

# Launch the chatbot
if __name__ == "__main__":
    interface.launch(share=True)
