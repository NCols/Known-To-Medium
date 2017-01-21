## This is a tool that allows users to easily cross-post their Known posts to their Medium account.

Attention: this is designed to work with Known posts only, statuses, bookmarks etc. have not been tested.

Help:
> python knownToMedium.py -h

Make sure the medium folder is in the same folder as the knownToMedium.py file.

The program stores your API connection variables and your Known site URL in a JSON file. If the file doesn't exist in the same folder as the script, the program will ask you to paste the information and will create the file, that will be loaded at program startup the next times.

You will be asked for:

1. Insert URL of your Known posts
   * It should look something like https://yourdomain.com/content/posts/.
   * Be careful to include the "/" at the end.

2. Insert Medium integration token
   * This token can only be used by your account and has no expiry date.
   * You can generate one at https://medium.com/me/settings.

3. Insert Medium app credentials
   * From the Medium settings menu, go to 'Manage applications' and create a new app.
   * Copy/paste the generated 'Client ID' when prompted.
   * Copy/paste the generated 'Client Secret' when prompted.

By default, Medium creates post drafts. You still have to manually confirm publication.

To directly publish instead of creating a draft, use "-t public".

You're ready to go!
