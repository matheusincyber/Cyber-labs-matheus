# Git push instructions (for your GitHub repo)
# Assuming you unzipped this scaffold into a folder and are inside it:

git init -b main
git add .
git commit -m "Scaffold + integrated notes"
git remote add origin git@github.com:matheusincyber/Cyber-labs-matheus.git
# create a branch for review:
git checkout -b scaffold-with-scripts
git push -u origin scaffold-with-scripts

# Then open a Pull Request on GitHub from scaffold-with-scripts → main
