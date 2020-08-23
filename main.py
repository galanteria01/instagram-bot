# Imported InstaPy to automate instagram
from instapy import InstaPy

# Created session variable consisting of login details of user
session = InstaPy(username='sample',password='********',headless_browser=True)
session.login()

# This is used to prevent disabling of account
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

# The tags consisting of tags written are automatically liked.
session.like_by_tags(["manit", "rubaroo", "ssr","jee","NIT","engineering"],amount=500)

# The tags passed as arguement are not liked as they maybe annoying or inappropriate.
session.dont_like(["naked","nsfw","dirty"])

# The locations passed as list when found in post are automatically liked.
session.comment_by_locations(["vidisha","india","bhopal"],30,"image",True)

# The accounts which posted the post we liked are followed by percentage given.
session.set_do_follow(True,percentage=50)

# The accounts which posted the post we liked are ed by percentage given.
session.set_do_comment(True,percentage=50)

# The comments are passed so that specified comments are passed into the posts.
session.set_comments(["Nice!","Impressive"])
