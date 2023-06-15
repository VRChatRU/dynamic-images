@echo off
python shakalizer.py
git reset --soft HEAD~
git add weekly.webp
git commit -m "updated weekly image via .bat file"
git push -f
