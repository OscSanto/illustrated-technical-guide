# Publish this repository later

1. Unzip the Git-history package (it contains `.git`).
2. Open a terminal inside `illustrated-technical-guide-git-history`.
3. Inspect `git log --oneline --decorate` and `git tag --list`.
4. Create an **empty** GitHub repository (do not initialize it with a README).
5. Run `git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git`.
6. Run `git push -u origin main` and `git push origin --tags`.

The ZIP and Git bundle both preserve the history. This is an archive reconstructed from versioned release packages; commit timestamps do not represent the original build dates. Before publishing, check licenses for third-party assets and conduct a final secrets/sensitive-data review.
