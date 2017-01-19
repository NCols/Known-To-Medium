This is a tool that allows users to easily cross-post their Known posts to their Medium account.

Help:
python knownToMedium.py -h

Make sure the medium folder is in the same folder as the knownToMedium.py file.

1. Insert URL of your Known posts
It should look something like https://yourdomain.com/content/posts/
Copy the URL in knownToMedium.py (known_posts_url). Be careful to include the "/" at the end.

2. Insert Medium integration token
This token can only be used by your account and has no expiry date.
You can generate one at https://medium.com/me/settings.
Copy the generated token in knownToMedium.py (integration_token).

3. Insert Medium app credentials
From the Medium settings menu, go to 'Manage applications' and create a new app.
Copy the generated 'Client ID' code in knownToMedium.py (client_id).
Copy the generated 'Client Secret' code in knownToMedium.py (client_secret)

You're ready to go!

