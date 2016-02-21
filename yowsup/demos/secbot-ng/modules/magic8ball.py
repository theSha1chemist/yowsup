import random

def magic8ball(query):
    if query.split(' ')[0] == "help":
        h = "Magic 8 Ball has the answers to all the questions..."
        return h

    else:
        print query 
        answer = ["It is certain",
                "It is decidedly so",
                "Without a doubt",
                "Yes, definitely",
                "You may rely on it",
                "As I see it, yes",
                "Most likely",
                "Outlook good",
                "Yes",
                "Signs point to yes",
                "Reply hazy try again",
                "Ask again later",
                "Better not tell you now",
                "Cannot predict now",
                "Concentrate and ask again",
                "Don't count on it",
                "My reply is no",
                "My sources say no",
                "Outlook not so good",
                "Very doubtful"]
        return (random.choice(answer))
