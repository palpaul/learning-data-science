# Learning Data Science

A small repo to collect notes, examples and exercises for learning data science.

## How to add this README and push to GitHub (commands)

Run these commands from the repository root (PowerShell-ready):

```powershell
git init
git add README.md
git commit -m "Add README"
git branch -M main
git remote add origin https://github.com/palpaul/learning-data-science.git
git push -u origin main
```

## Do I need to run these commands if I'm using GitHub Desktop?

Short answer: No — GitHub Desktop provides GUI equivalents for all these steps. Use the Desktop app to:

- Add or open the local repository (File → Add Local Repository).
- Stage and commit changes using the Changes tab (select files, enter a commit message, Commit to main).
- If the repo is not yet published, click "Publish repository" in the toolbar to create the remote and push.
- If the remote already exists, click "Push origin" to push commits.

Notes:
- If your folder isn't a git repository yet, GitHub Desktop will initialize it for you when you add it.
- If a remote named `origin` already exists, you don't need to run `git remote add origin` — Desktop manages remotes.
- The commands are useful if you prefer the terminal or need to script the process, but they're optional when using the Desktop app.

If you'd like, I can add a short section with GitHub Desktop screenshots or step-by-step GUI instructions.
