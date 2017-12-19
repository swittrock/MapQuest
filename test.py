import api_handling
import classes_and_output
import input_handling
import urllib.request

print(api_handling.web_result(urllib.request.urlopen('https://www.reddit.com/')))