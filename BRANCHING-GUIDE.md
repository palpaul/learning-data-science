# Branching & remote default — minimal commands and explanations

Purpose: quick, focused list of the specific git commands you need to make a local repo follow a remote branch rename (for example `main` → `develop`). Each command includes what it does and why to use it.

Safety: commit or stash uncommitted work before switching or renaming branches:

```powershell
git status --porcelain
# if output exists: git add .; git commit -m "WIP"  OR  git stash push -m "WIP"
```

1) Update remote refs (fetch + prune)

```powershell
git fetch origin --prune
```
- What it does: downloads updates from the remote and removes local references to remote branches that have been deleted.
- Why use it: ensures your local view of `origin/*` matches the remote (prevents acting on stale branch names).

2) Inspect remote and local branches

```powershell
git branch -a
```
- What it does: lists local and remote-tracking branches.
- Why use it: confirm `remotes/origin/develop` exists before creating or renaming a local branch.

3A) Rename local `main` to `develop` (if you want to reuse the same local branch name)

```powershell
git checkout main            # switch to the branch you will rename
git branch -m develop        # rename local branch main -> develop
git branch --set-upstream-to=origin/develop develop
```
- What they do:
	- `checkout main`: moves you onto the branch that you're renaming.
	- `branch -m develop`: renames the current local branch to `develop`.
	- `--set-upstream-to=origin/develop`: makes the new local `develop` track the remote `origin/develop` so `git pull`/`git push` work.
- Why use them: keeps local history and branch pointer but aligns the name and tracking with the remote.

3B) Create a new local `develop` that tracks `origin/develop` (safer option)

```powershell
git fetch origin --prune
git checkout -b develop origin/develop
```
- What they do:
	- `fetch --prune`: (as above) refreshes remote refs.
	- `checkout -b develop origin/develop`: creates a local branch named `develop` starting from `origin/develop` and sets it to track the remote.
- Why use them: preserves local `main` while creating a proper local branch that follows the remote `develop`.

4) Push and set upstream (if you created/renamed locally and need to push)

```powershell
git push -u origin develop
```
- What it does: pushes the local `develop` branch to `origin` and sets `origin/develop` as the upstream for future pushes/pulls.
- Why use it: needed if the local branch is new or if you want to ensure remote has your branch and tracking is configured.

5) (Optional) Delete local `main` if no longer needed

```powershell
git branch -d main   # safe delete; use -D to force
```
- What it does: deletes the local `main` branch (refuses if it has unmerged commits).
- Why use it: removes confusion if you no longer need the old name locally.

6) (Optional) Update local remote HEAD pointer

```powershell
git remote set-head origin develop
```
- What it does: sets `origin/HEAD` locally to point to `origin/develop` (local metadata only).
- Why use it: helps some tools display the correct remote default branch without changing GitHub settings.

Verification (quick)

```powershell
git branch -vv
git remote show origin
```

That's it — these are the precise commands you need. If you want, I can run them in your repo (tell me to proceed) or give a one-line sequence to paste into PowerShell.
