
# Running the tools that use the GitHub REST API

## Get a github token

- Go to https://github.com/settings/tokens

- Create a 'classic' token
- Copy the token somewhere, you will not have access to it later
- Select `repo` so you can query the repo with the token
- Click `Configure SSO` and authorise `ecmwf` (That step may only be needed to update the repo)


## Install the token

Add the token to `~/.env`:

```
GITHUB_TOKEN=xxxxx
```
