## python_prompts

*Lightweight prompt system for python based on:  
[terkelg prompts](https://github.com/terkelg/prompts)*

### Usage

**IMPORTANT**  
remember to ```import python_prompts as prompts``` before you start and make sure that the python_prompts.py file is in the same location as your project.

Initialize your prompt like this:  
``` python
age = prompts.IntegerPrompt('Age', '>=', 'What\'s your age?', 7, 'Hey!', False)
```
If you want to chain multiple prompts together, do it like this:  
``` python
chain = [question1, question2, question3, question4]
prompts.PromptChain(chain)
```
**Remember - When a prompt validtation is not met, the prompt chain will exit and break the program.**

To recall the prompt answers:
``` python
print(prompts.return_prompt_variable(age))
```

### Types

*prompts.IntegerPrompt*  
prompt the user with an expected integer.

**Usage**
``` python
prompts.IntegerPrompt(String*variable name*, String*type*, String*question*, Integer*answer*, String*error_msg*, Boolean*show/flush_output*)
```
types: <, >, <=, >=, =

*prompts.StringPrompt*  
prompt the user with an expected string.

**Usage**
``` python
prompts.StringPrompt(String*variable name*, String*question*, String*answer*, String*error_msg*, Boolean*show/flush_output*)
```

*prompts.MultipleChoicePrompt*  
prompt the user with an expected integer question number (multiple choice).

**Usage**
``` python
prompts.MultipleChoicePrompt(String*variable name*, String*question*, Integer*answer*, String*error_msg*, Array*options*, Boolean*show/flush_output*)
```
**Important Note -** The integer answer starts from 0 for the first question (reflecting python lists)
