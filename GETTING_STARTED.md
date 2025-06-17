# Getting Started with the Codex Repository

This quick guide explains the commands used to clone and set up the Codex repository locally. Later, we'll add more files and code.

## Prerequisites

- Git installed on your machine.
- Network access to GitHub.

## Clone the Repository

Clone the repository into the current directory:

```bash
git clone https://github.com/lecharles/codex.git .
```

## Verify the Remote

Check that the `origin` remote is configured correctly:

```bash
git remote -v
```

Expected output:

```bash
origin  https://github.com/lecharles/codex.git (fetch)
origin  https://github.com/lecharles/codex.git (push)
```

## Next Steps

You now have a local copy of the Codex repository. You can:

- Create or update files for your features.
- Commit your changes using `git add` and `git commit`.
- Push updates to the remote with `git push`.