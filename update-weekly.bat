@echo off
git fetch --all
git reset --hard origin/main
git pull
python shakalizer.py
git add weekly.webp
git add weeklyHD.webp
git commit -m "updated weekly image via .bat file"
git push
