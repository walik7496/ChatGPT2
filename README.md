# GPT-2 ChatBot

A Python-based chatbot powered by **GPT-2** from the Hugging Face Transformers library. This chatbot features a simple graphical user interface (GUI) using Tkinter and provides dynamic, AI-generated responses.

## Features

- **AI-Powered Responses:** Utilizes GPT-2 to generate natural language replies.
- **Scrollable Chat History:** Displays ongoing conversation with scroll support.
- **Keyboard Shortcut:** Press `Enter` to send messages quickly.
- **Simple Interface:** Clean and minimalistic GUI for seamless interaction.

## Prerequisites

- **Python 3.x**
- Required Python Libraries:
  - `tkinter` (comes pre-installed with Python)
  - `transformers`
  - `torch`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/walik7496/ChatGPT2.git
   cd gpt2-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install transformers torch
   ```

3. **Run the application:**
   ```bash
   python chatbot.py
   ```

## Usage

### Instructions:
- Type your message in the input field.
- Click the **Send** button or press **Enter** to send the message.
- The chatbot will generate AI-driven responses using GPT-2.

## File Structure

```
.
├── chatbot.py
├── README.md
└── requirements.txt (optional for dependency management)
```

## Troubleshooting

- **Slow Response:** GPT-2 may take a few seconds to generate responses, especially on CPUs. Consider running on a GPU for faster performance.
- **Out of Memory Error:** For large models, ensure your system has sufficient RAM/VRAM. Try reducing the `max_length` parameter in `generate_response()`.
- **Missing Libraries:** Ensure `transformers` and `torch` are installed correctly.

## Customization

To adjust the chatbot's behavior:
- **Response Length:** Modify `max_length` in the `generate_response` method.
- **Advanced Tuning:** Explore additional parameters for `generate()`, such as `temperature`, `top_k`, or `top_p`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the [MIT License](LICENSE).
