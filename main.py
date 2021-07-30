from InstaBot import InstaBot as ib
import time

if __name__ == '__main__':
    username = 'username' # username or phone number
    password = 'password'

    account = ib(username, password)
    account.login()
    time.sleep(5)
    account.escape_notification()
    time.sleep(3)

    # list of hashtags to like
    tags = ['python', 'javascript', 'java', 'design', 'graphicdesign','coding','coder','programmer']

    [hako.like_photo(tag) for tag in tags]
    for tag in tags:
        account.like_photo(tags)
        account.go_back_home()