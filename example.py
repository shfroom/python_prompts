#!/usr/bin/env python3

import python_prompts as prompts

age = prompts.IntegerPrompt('Age', '>=', 'What\'s your age?', 7, 'Hey!', False)
name = prompts.StringPrompt('Name', 'What\'s your name?', 'Shaunak', 'Hey!', False)

choices = ["Cheese", "Tomato"]
question3 = prompts.MultipleChoicePrompt('Choice', 'What do you pick?', 0, 'Hey!', choices, False)
question4 = prompts.IntegerPrompt('Hobbies', '>=', 'How many hobbies do you have?', 1, 'Hey!', False)
chain = [age, name, question3, question4]
prompts.PromptChain(chain)

print(prompts.return_prompt_variable(age))
print(prompts.return_prompt_variable(name))
print(prompts.return_prompt_variable(question3))
print(prompts.return_prompt_variable(question4))
