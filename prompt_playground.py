import os
from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Parameters to test
temperatures = [0.0, 0.7, 1.2]
max_tokens_list = [50, 150, 300]
presence_penalties = [0.0, 1.5]
frequency_penalties = [0.0, 1.5]
models = ["gpt-3.5-turbo"]

# Fixed prompts
system_prompt = "You are a product copywriter."
user_prompt = "Write a compelling product description for an iPhone."

results = []

# Loop through all parameter combinations
for model in models:
    for temp in temperatures:
        for max_tokens in max_tokens_list:
            for presence_penalty in presence_penalties:
                for frequency_penalty in frequency_penalties:
                    try:
                        response = client.chat.completions.create(
                            model=model,
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_prompt}
                            ],
                            temperature=temp,
                            max_tokens=max_tokens,
                            presence_penalty=presence_penalty,
                            frequency_penalty=frequency_penalty
                        )
                        output = response.choices[0].message.content
                        results.append({
                            "Model": model,
                            "Temp": temp,
                            "Max Tokens": max_tokens,
                            "Presence Penalty": presence_penalty,
                            "Frequency Penalty": frequency_penalty,
                            "Output": output.strip()
                        })
                    except Exception as e:
                        print(f"Error: {e}")

# Create table and export to CSV
df = pd.DataFrame(results)
df.to_csv("prompt_outputs.csv", index=False)
print(df)
