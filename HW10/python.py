import re
import subprocess

# Define the ReAct prompt
react_prompt = """
You run in a loop of Thought, Action, Observation.
At the end of the loop you output an Answer
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you。
Observation will be the result of running those actions.

Your available actions are:

calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary

call_google:
e.g. call_google: European Union
Returns a summary from searching European Union on google

You can look things up on Google if you have the opportunity to do so, or you are not sure about the query
"""

# Function to process the ReAct prompt
def process_react_prompt(prompt):
    thought = ""
    action = ""
    observation = ""

    # Extract action from the prompt
    action_match = re.search(r'Action:\s*(.*)', prompt)
    if action_match:
        action = action_match.group(1).strip()

    # Perform the action
    if action.startswith("calculate:"):
        try:
            calculation = action.split("calculate:")[1].strip()
            observation = str(eval(calculation))
        except Exception as e:
            observation = f"Error: {str(e)}"
    elif action.startswith("call_google:"):
        try:
            query = action.split("call_google:")[1].strip()
            result = subprocess.check_output(f"google {query}", shell=True).decode("utf-8")
            observation = result.split("Observation: ")[1].strip()
        except Exception as e:
            observation = f"Error: {str(e)}"

    # Output the observation
    print("Observation:", observation)

# Main loop
def main():
    print("Welcome to the ReAct prompt example!")
    print(react_prompt)
    while True:
        user_input = input("Enter your question or action: ").strip()
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        thought = input("Thought: ").strip()
        action = f"Action: {user_input}"
        observation = process_react_prompt(action)
        print("Answer:", observation)
        print()

if __name__ == "__main__":
    main()
