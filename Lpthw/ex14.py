#-- coding: utf-8 --
from sys import argv

script, user_name = argv
prompt = '<>'

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
like = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)


