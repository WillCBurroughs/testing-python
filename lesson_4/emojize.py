import requests
import emoji

def main():
    given_input = ""
    while given_input != "q":
        given_input = input("input to turn to emoji? Press q to quit ")
        output = make_request(given_input)
        print(output)

def make_request(input_to_emoji):
    r = emoji.emojize(input_to_emoji)
    return r

main()