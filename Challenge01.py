# Challenge 1: The AI Token Cost Calculator 
# 🤖Write a script that calculates the estimated cost of sending an API request to an AI model.   
# Requirements:Ask the user for the Model Name (e.g., Gemini Pro or GPT-4).
# Ask for the Number of Input Tokens (e.g., 1500).Ask for the Cost per Token (e.g., 0.00002).
# Calculate the total cost: $\text{Total Cost} = \text{Tokens} \times \text{Cost per Token}$.
# Print a formatted summary message using f-strings.
print("The AI Token Cost Calculator")
model_name = input("Enter the Model Name (e.g., Gemini Pro or GPT-4): ")
num_of_tokens = int(input("Enter the Number of Input Tokens(e.g., 1500): "))
cost_per_token = float(input("Enter the cost per Token (e.g., 0.00002): "))
total_cost = num_of_tokens * cost_per_token
print(f"The estimated cost of sending an API request to the {model_name} model with {num_of_tokens} input tokens at a cost of ${cost_per_token:.5f} per token is: ${total_cost:.5f}")