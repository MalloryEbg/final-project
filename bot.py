# import form discord library
# import from way of using operating system environment
# import random module
# load environment variables from file .env
# import module from the ec2_metadata
import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

# print the region & instance id
print(ec2_metadata.region)
print(ec2_metadata.instance_id)

# cast any data imported
load_dotenv() 

# assigning client and token
client = discord.Client()
token = os.getenv('TOKEN')


# bound the first argument with the event method
@client.event 
# an asynchronous function allows the program to wait for the completion of a function before moving to the next line of code and print the following format
async def on_ready():
	print("Logged in as a bot {0.user}".format(client))


@client.event
async def on_message(message):
	# get the username in string and revoming anything else from # then after.
	username = str(message.author).split("#")[0]
	# assigning channel
	channel = str(message.channel.name)
	# assigning user message
	user_message = str(message.content)
	# print the message of the user
	print(f'Message {user_message} by {username} on {channel}')

	# checking if the author of the message is the same client then return nothing if true.
	if message.author == client.user:
		return

	# if a channel is named random exists to proceed to the next conditional.
	if channel == "random":
		# if the written message meet any condition in lowercase then proceed.
		if user_message.lower() == "hello" or user_message.lower() == "hi" or user_message.lower() == "hey":
			# await : keybord that tells the program to wait for the completion of the function before moving to the next line of code.
			# a response would follow to print the following message.
			await message.channel.send(f'Hello {username}')
			return
		# conditioning the user's message from the user to be on lowercase
		elif user_message.lower() == "bye":
			# the completion of the function has to be done before moving to next line of code.
			await message.channel.send(f'Bye {username}')
		# codition the user's message to be in lowercase to work
		elif user_message.lower() == "hello world":
			# full wait for the completion of the function then move to the next line of code.
			await message.channel.send(f'Hello {username}')
		# the question asked should be in lowercase to satisfy the condition
		elif user_message.lower() == "tell me about my server":
			# wait for all the function to be done then move to next line of code and print these element as the response.
			await message.channel.send(f'Sooner! {username} \n Public IPv4:{ec2_metadata.public_ipv4} \n Your region:{ec2_metadata.region} \n Availability zone:{ec2_metadata.availability_zone} \n')
		# if the condition meet then a random choice of joke will be picked.
		elif user_message.lower() == "tell me a joke":
			# list of jokes
			jokes = ["Why did the Mexican football team bring rope to the game?\n 'Cus they wanted to tie the score.", "What white boy band should've been a black boy band?\n The Jonas Borthers.", "What did the bee say to his wife when they were running late for dinner?\n Hurry up honey", "What did the power ranger say to his patients when he became a doctor?\n It's morphine time.", "What does a grizzly say when he calls customer service?\n Just bear with me.", "What did the salt say to the pepper?\n Catch you next seasoning.", "I would do a steak joke...\n But they're never well done.", "Why did everyone hate me after I used the bathroom at a party?\n They say U was a party pooper."]
		# halt the function until everything done to move to the next line to randomly pick a joke
		await message.channel.send(random.choice(jokes))

# the function is ran at the end
client.run(token)