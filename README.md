# Interactive Prompt Playground

A Python-based tool for experimenting with OpenAI API parameters and analyzing how different settings affect model outputs. This playground systematically tests various combinations of temperature, token limits, and penalty parameters to help understand their impact on AI-generated content.

## Features

- **Parameter Control**: Test different combinations of:
  - Temperature (0.0, 0.7, 1.2)
  - Max tokens (50, 150, 300)
  - Presence penalty (0.0, 1.5)
  - Frequency penalty (0.0, 1.5)
  - Model selection (gpt-3.5-turbo)

- **Automated Testing**: Runs through all parameter combinations automatically
- **CSV Export**: Saves results to `prompt_outputs.csv` for analysis
- **Error Handling**: Gracefully handles API errors and rate limits
- **Structured Output**: Organizes results in a pandas DataFrame for easy analysis

## Setup and Installation

### Prerequisites
- Python 3.7+
- OpenAI API key

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/interactive-prompt-playground.git
   cd interactive-prompt-playground
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the playground**:
   ```bash
   python prompt_playground.py
   ```

## How to Run

1. Ensure your OpenAI API key is set in the `.env` file
2. Run the script: `python prompt_playground.py`
3. The script will automatically test all parameter combinations
4. Results will be displayed in the console and saved to `prompt_outputs.csv`
5. Open the CSV file to analyze the different outputs

## Output Analysis

### Results Grid

The script generates a comprehensive table showing outputs across different parameter settings. Here's a sample of the results structure:

| Model | Temp | Max Tokens | Presence Penalty | Frequency Penalty | Output |
|-------|------|------------|------------------|-------------------|---------|
| gpt-3.5-turbo | 0.0 | 50 | 0.0 | 0.0 | Discover the revolutionary iPhone - a perfect blend of cutting-edge technology and elegant design that redefines what a smartphone can be. |
| gpt-3.5-turbo | 0.7 | 150 | 0.0 | 0.0 | Experience the future in your hands with the incredible iPhone! This stunning device combines sleek aesthetics with powerful performance... |
| gpt-3.5-turbo | 1.2 | 300 | 1.5 | 1.5 | Behold the magnificent iPhone - where innovation dances with sophistication! This extraordinary device transcends ordinary expectations... |

### Parameter Impact Analysis

**Temperature Effects**: Lower temperatures (0.0) produce consistent, focused outputs that stick closely to conventional product description language. As temperature increases to 0.7, the responses become more varied and creative while maintaining relevance. At the highest temperature (1.2), outputs show maximum creativity with more unique word choices and expressive language, though sometimes at the cost of conventional marketing tone.

**Token and Penalty Interactions**: Max token limits directly control output length, with 50 tokens producing concise descriptions and 300 tokens allowing for detailed, comprehensive copy. Presence penalties (1.5) encourage the model to explore diverse topics and avoid repetition, leading to more varied product features being highlighted. Frequency penalties (1.5) reduce word repetition, resulting in richer vocabulary usage and more sophisticated language patterns. The combination of high penalties with higher temperatures creates the most creative and diverse outputs, while low penalties with low temperatures produce the most consistent and predictable marketing copy.

## File Structure

```
interactive-prompt-playground/
├── prompt_playground.py  # Main script
├── README.md             # This file
├── .env                  # Environment variables (create this)
├── prompt_outputs.csv    # Generated results (after running)
├── requirements.txt      # Python dependencies
└── .gitignore           # Git ignore file
```

## Configuration

You can modify the following variables in `playground.py` to customize your testing:

- `temperatures`: List of temperature values to test
- `max_tokens_list`: List of token limits to test
- `presence_penalties`: List of presence penalty values
- `frequency_penalties`: List of frequency penalty values
- `models`: List of models to test
- `system_prompt`: The system message for context
- `user_prompt`: The user message/prompt to test

## API Key Security

⚠️ **Important**: Never commit your actual API key to version control. The `.env` file is included in `.gitignore` to prevent accidental exposure.

## Dependencies

Create a `requirements.txt` file with:
```
openai>=1.0.0
pandas>=1.3.0
python-dotenv>=0.19.0
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Troubleshooting

**Common Issues**:
- **API Key Error**: Ensure your OpenAI API key is correctly set in the `.env` file
- **Rate Limits**: The script includes basic error handling for API rate limits
- **Module Not Found**: Run `pip install -r requirements.txt` to install dependencies

**Getting Help**:
- Check the OpenAI API documentation for parameter details
- Review the CSV output to understand parameter effects
- Modify the prompts and parameters to suit your specific use case
