#!/usr/bin/env python3

# python_prompts
# ==============
# Lightweight prompt system for python based on:
# [https://github.com/terkelg/prompts]
import sys
from time import sleep
from termcolor import colored

def PromptChain(chain):
	for prompt in chain:
		if prompt.prompt() == False:
			break

def scrollTxt(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		sleep(0.03)

class IntegerPrompt:
	def __init__(self, name, _type, msg, validate, error, flush_output):
		self.name = name
		self.type = _type
		self.msg = msg
		self.validate = validate
		self.error = error
		self.flush_output = flush_output

	def prompt(self):
		globals()[self.name] = input(colored('? ', 'cyan') + colored(self.msg, attrs=['bold']) + colored(' › ', 'grey'))
		output_check = False
		# Smaller than
		if self.type == '<':
			if int(globals()[self.name]) > int(self.validate):
				if not self.flush_output: print('\033[0m' + colored('› ', 'grey') + colored(f'\033[3m{self.error}\033[3m', 'red'))
				output_check = False
			else:
				print('\033[0m{ ' + f'{self.name}: ' + colored(globals()[self.name], 'yellow') + ' }')
				output_check = True
		# Larger than
		elif self.type == '>':
			if int(globals()[self.name]) < int(self.validate):
				if not self.flush_output: print('\033[0m' + colored('› ', 'grey') + colored(f'\033[3m{self.error}\033[3m', 'red'))
				output_check = False
			else:
				print('\033[0m{ ' + f'{self.name}: ' + colored(globals()[self.name], 'yellow') + ' }')
				output_check = True
		# Inequality <
		elif self.type == '<=':
			if int(globals()[self.name]) <= int(self.validate):
				if not self.flush_output: print('\033[0m{ ' + f'{self.name}: ' + colored(globals()[self.name], 'yellow') + ' }')
				output_check = True
			else:
				print('\033[0m' + colored('› ', 'grey') + colored(f'\033[3m{self.error}\033[3m', 'red'))
				output_check = False
		# Inequality >
		elif self.type == '>=':
			if int(globals()[self.name]) >= int(self.validate):
				if not self.flush_output: print('\033[0m{ ' + f'{self.name}: ' + colored(globals()[self.name], 'yellow') + ' }')
				output_check = True
			else:
				print('\033[0m' + colored('› ', 'grey') + colored(f'\033[3m{self.error}\033[3m', 'red'))
				output_check = False
		# Equals
		elif self.type == '=':
			if int(globals()[self.name]) != int(self.validate):
				if not self.flush_output: print('\033[0m' + colored('› ', 'grey') + colored(f'\033[3m{self.error}\033[3m', 'red'))
				output_check = False
			else:
				print('\033[0m{ ' + f'{self.name}: ' + colored(globals()[self.name], 'yellow') + ' }')
				output_check = True
		return output_check


class StringPrompt:
    def __init__(self, name, msg, validate, error, flush_output):
        self.name = name
        self.msg = msg
        self.validate = validate
        self.error = error
        self.flush_output = flush_output

    def prompt(self):
        globals()[self.name] = input(colored('? ', 'cyan') + colored(self.msg, attrs=['bold']) + colored(' › ', 'grey'))
        output_check = False
        # For array validation
        if type(self.validate) == type([]):
            for index, validation in enumerate(self.validate):
                if globals()[self.name].casefold() == validation.casefold():
                    if not self.flush_output: print('\033[0m{ ' + f'{self.name}: ' + colored(globals()[self.name], 'yellow') + ' }')
                    output_check = True
                    break
            else:
                print('\033[0m' + colored('› ', 'grey') + colored(f'\033[3m{self.error}\033[3m', 'red'))
                output_check = False
        # For single string validation
        elif type(self.validate) == type(''):
            if globals()[self.name].casefold() == self.validate.casefold():
                if not self.flush_output: print('\033[0m{ ' + f'{self.name}: ' + colored(globals()[self.name], 'yellow') + ' }')
                output_check = True
            else:
                print('\033[0m' + colored('› ', 'grey') + colored(f'\033[3m{self.error}\033[3m', 'red'))
                output_check = False
        return output_check

class MultipleChoicePrompt:
	def __init__(self, name, msg, validate, error, choices, flush_output):
		self.name = name
		self.msg = msg
		self.validate = validate
		self.error = error
		self.choices = choices
		self.flush_output = flush_output

	def prompt(self):
		output_check = False
		for option in self.choices:
			text = '[' + str(self.choices.index(option) + 1) + ']'
			scrollTxt(colored(text, attrs=['bold']) + f' {option}\n')
		globals()[self.name] = input(colored('? ', 'cyan') + colored(self.msg, attrs=['bold']) + colored(' › ', 'grey'))

		if int(globals()[self.name]) - 1 == self.validate:
			choice = self.choices[int(globals()[self.name]) - 1]
			globals()[self.name] = choice
			if not self.flush_output: print('\033[0m{ ' + f'{self.name}: ' + colored(globals()[self.name], 'yellow') + ' }')
			output_check = True
		else:
			print('\033[0m' + colored('› ', 'grey') + colored(f'\033[3m{self.error}\033[3m', 'red'))
			output_check = False
		return output_check



def return_prompt_variable(prompt):
	return globals()[prompt.name]

# age = IntegerPrompt('Age', '>=', 'What\'s your age?', 7, 'Hey!', False)
# name = StringPrompt('Name', 'What\'s your name?', 'Shaunak', 'Hey!', False)

# choices = ["cheese", "tomato"]
# question3 = MultipleChoicePrompt('Choice', 'What do you pick?', 0, 'Hey!', choices, False)
# question4 = IntegerPrompt('Hobbies', '>=', 'How many hobbies do you have?', 1, 'Hey!', False)
# chain = [age, name, question3, question4]
# PromptChain(chain)
