import instaloader

L = instaloader.Instaloader()

# <3
username = "yeahimdodo"
password = "your_secret_password"
L.login(username, password)

print(L.context.username)


def get_user_followers(il: instaloader.Instaloader, un):
    return instaloader.Profile.from_username(il.context, un).get_followers()


def get_user_following(il: instaloader.Instaloader, un):
    return instaloader.Profile.from_username(il.context, un).get_followees()


followers = get_user_followers(L, username)
followers_username = [follower.username for follower in followers]
print("Followers: " + str(followers.count))

followings = get_user_following(L, username)
print("Followings: " + str(followings.count))

count = 0
for following in followings:
    if following.username not in followers_username:
        print(following.username + " (" + following.full_name + ")" + " is not following back you!")
        count += 1

if count == 0:
    print("Everyone following back you!")
else:
    print(str(count) + " people is not following back you!")
