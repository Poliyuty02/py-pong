# 🎮 Pong Game Workshop: Your First Git & Python Project 

**Duration:** 90 minutes
**Goal:** Learn Git/GitHub workflow while customizing a working Pong game

## 📋 What You'll Learn Today
- How to use Git for version control
- How to fork and clone a GitHub repository
- How to make changes, commit them, and push back to GitHub
- Basic Python game development with Pygame

## 🛠️ Before You Start (5 min)

### Step 1: Create a GitHub Account
If you don't have one:
1. Go to [github.com](<https://github.com>)
2. Click "Sign up" (it's free!)
3. Verify your email address

### Step 2: Install Required Software
- **VS Code**: Download from [code.visualstudio.com](<https://code.visualstudio.com>)
- **Python**: Download from [python.org](<https://python.org>) (version 3.8 or higher)

## 🎯 Workshop Milestone Checklist (90 minutes)

Use this checklist to track your progress:

- [ ] **GitHub Account created** (5 min)
- [ ] **Repository forked to your account** (2 min)
- [ ] **Repository cloned to your computer** (3 min)
- [ ] **Project opened in VS Code** (2 min)
- [ ] **Virtual environment created** (5 min)
- [ ] **Pygame installed** (2 min)
- [ ] **Game runs successfully first time** (3 min)
- [ ] **Changed at least 2 visual elements** (15 min)
- [ ] **Changed game behavior (speed/score)** (10 min)
- [ ] **Successfully committed changes** (5 min)
- [ ] **Pushed changes back to GitHub** (3 min)
- [ ] **Shared your GitHub repo link** (optional, 2 min)

## 📝 Step-by-Step Instructions

### Phase 1: Fork & Clone (15 min)

#### 1. Fork the Repository
- Go to the workshop template repository (your instructor will provide the link)
- Click the **Fork** button (top-right corner)
- Select your GitHub account as the destination

#### 2. Clone to Your Computer
- On YOUR forked repository, click the green **Code** button
- Copy the HTTPS URL (looks like: `https://github.com/YOUR_USERNAME/pong-workshop.git`)
- Open **VS Code**
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
- Type "Git: Clone" and select it
- Paste the URL
- Choose a folder on your computer (e.g., Desktop)
- Click "Open" when cloning completes

### Phase 2: Set Up & Run (15 min)

#### 3. Open Terminal in VS Code
- `Terminal → New Terminal` from the menu
- You should see your project folder path

#### 4. Create a Virtual Environment (Windows)
```bash
python -m venv venv
venv\\Scripts\\activate
```
### 4. Create a Virtual Environment (Mac/Linux)

```bash
python3 -m venv venv
source venv/bin/activate
```

*You'll see `(venv)` appear at the beginning of your terminal line*

### 5. Install Pygame

```bash
pip install pygame
```

### 6. Run the Game!

```bash
python main.py
```

The game window should appear! Use:

- Left player: **W** (up) and **S** (down)
- Right player: **↑** (up) and **↓** (down)

**Close the game window** when you're ready to continue.

### Phase 3: Customize! (40 min)

Now for the fun part - make this game YOURS!

### Challenge 1: Change Colors (Easy)

Open `main.py` and find the `# TODO: STUDENT CHALLENGE 2` section. Try:

- Changing `BLACK` to `(50, 50, 150)` for a blue background
- Changing `WHITE` to `(255, 200, 0)` for gold paddles

### Challenge 2: Change Game Speed (Medium)

Find the `Ball` class's `__init__` method. Look for `speed_x=4, speed_y=4`. Try `speed_x=6, speed_y=6` for a faster game!

### Challenge 3: Change Winning Score (Easy)

Find `WINNING_SCORE = 5` and change it to `3` for a shorter game or `10` for a longer challenge.

### Challenge 4: Add Your Name (Super Easy)

Find `pygame.display.set_caption("PONG - Your Name Here")` and replace "Your Name Here" with your actual name!

### Phase 4: Save Your Work with Git (15 min)

### 7. See What Changed

```bash
git status
```

This shows which files you modified.

### 8. Stage Your Changes

```bash
git add main.py
```

Or to stage ALL changes:

```bash
git add .
```

### 9. Commit with a Message

```bash
git commit -m "Customized colors and game speed"
```

### 10. Push to GitHub

```bash
git push origin main
```

### Phase 5: Verify & Share (5 min)

- Go to **your GitHub repository** in a web browser
- Refresh the page - you should see your changes!
- Copy the URL and share with classmates/instructor

## 🎉 Congratulations!

You've successfully:

- Used Git to clone, commit, and push code
- Customized a working Python game
- Published your changes to GitHub

## 🔥 Bonus Challenges (If You Finish Early)

1. **Add a sound effect** when the ball hits a paddle (look for `# TODO 7`)
2. **Make the ball speed increase** each time it hits a paddle
3. **Change the paddle size** (make them longer or shorter)
4. **Add a "Start Game" screen** before the game begins

## 🆘 Troubleshooting

| Problem | Solution |
| --- | --- |
| "pip is not recognized" | Reinstall Python and check "Add to PATH" |
| "pygame not found" | Run `pip install pygame` again after activating venv |
| Game runs super fast/slow | Check `FPS = 60` in [main.py](http://main.py/) |
| Can't push to GitHub | Make sure you forked (not cloned directly from instructor) |
| VS Code can't find Python | `Ctrl+Shift+P` → "Python: Select Interpreter" → choose `./venv` |

## 📚 Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [RGB Color Picker](https://rgbcolorpicker.com/)
