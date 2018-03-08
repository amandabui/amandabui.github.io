class Pet(object):
	def __init__(self, name, owner):
		self.is_alive = True
		self.name = name
		self.owner = owner
	def eat(self, thing):
		print(self.name + ' ate a ' + str(thing) + '!')
	def talk(self):
		print(self.name)

class Dog(Pet):
	def talk(self):
		print(self.name + 'says woof!')

class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		### do something
		Pet.__init__(self, name, owner)
		## super().__init__(name, owner)
		self.lives = lives 

	def talk(self):
		"""A cat says meow! when asked to talk."""
		print("meow!")

	def lose_life(self):
		"""A cat can only lose a life if they have at least one life. 
		When lives reaches zero, is_alive becomes False."""
		if self.lives >= 1:
			self.lives -= 1 
			if self.lives == 0:
				self.is_alive = False 


class NoisyCat(Cat): # fill this line in 
	""" A cat that repeats things twice. """
	def __init__(self, name, owner, lives=9):
		# Is this method necessary? Why or why not?
		Cat.__init__(self, name, owner, lives)
		# not necessary because it will automatically
		# call your parent class's constructor for you

	def talk(self):
		"""Repeat what a Cat says twice."""
		# print("meow!")
		# print("meow!")
		Cat.talk(self)
		Cat.talk(self)

class Email:
	"""Every email object has 3 instance attr: 
	message, sender name, recipient name"""
	def __init__(self, msg, sender_name, recipient_name):
		self.msg = msg
		self.sender_name = sender_name
		self.recipient_name = recipient_name 

class Mailman:
	def __init__(self):
		self.clients = {}

	def send(self, email):
		""" Take an email and put it in the inbox of the client
		it is addressed to """
		client = self.clients[email.recipient_name]
		client.receive(email)

	def register_client(self, client, client_name):
		""" Takes a client object and client_name and adds it
		to the clients instance attribute. """
		self.clients[client_name] = client 

class Client:
	def __init__(self, mailman, name):
		self.inbox = []
		self.mailman = mailman 
		self.name = name 
		mailman.register_client(self, name)

	def compose(self, msg, recipient_name):
		""" Send an email with the given message msg to the 
		given recipient client. """
		email = Email(msg, self.name, recipient_name)
		self.mailman.send(email)

	def receive(self, email):
		""" Take an email and add it to the inbox of this
		client. """
		self.inbox.append(email)
