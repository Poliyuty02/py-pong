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
1. Go to [github.com](https://github.com)
2. Click "Sign up" (it's free!)
3. Verify your email address

### Step 2: Install Required Software
- **VS Code**: Download from [code.visualstudio.com](https://code.visualstudio.com)
- **Python**: Download from [python.org](https://python.org) (version 3.8 or higher)

## 🎯 Workshop Milestone Checklist (90 minutes)

Use this checklist to track your progress:

- [ ] **GitHub Account created** (5 min)
- [ ] **Repository forked to your account** (2 min)
- [ ] **Repository cloned to your computer** (3 min)
- [ ] **Project opened in VS Code** (2 min)
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

### Phase 2: Set Up & Run (10 min)

#### 3. Open Terminal in VS Code
- `Terminal → New Terminal` from the menu
- You should see your project folder path

#### 4. Install Pygame
```bash
pip install pygame
```

If you see a permission error, try:
```bash
pip install --user pygame
```

#### 5. Run the Game!
```bash
python main.py
```

If that doesn't work, try:
```bash
python3 main.py
```

The game window should appear! Use:
- Left player: **W** (up) and **S** (down)
- Right player: **↑** (up arrow) and **↓** (down arrow)

**Close the game window** when you're ready to continue.

### Phase 3: Customize! (40 min)

Now for the fun part - make this game YOURS! Open `main.py` and find each `# TODO` comment.

#### Challenge 1: Change Window Size (Easy)
Find `# TODO: STUDENT CHALLENGE 1` and change:
```python
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
```
Try `SCREEN_WIDTH = 1024` and `SCREEN_HEIGHT = 768` for a bigger game!

#### Challenge 2: Change Colors (Easy)
Find `# TODO: STUDENT CHALLENGE 2` and experiment:
- Change `BLACK` to `(50, 50, 150)` for a blue background
- Change `WHITE` to `(255, 200, 0)` for gold paddles
- Change `BALL_COLOR` to `(255, 0, 255)` for a purple ball

#### Challenge 3: Change Winning Score (Easy)
Find `# TODO: STUDENT CHALLENGE 3` and change:
```python
WINNING_SCORE = 5
```
Try `3` for a quicker game or `10` for a longer challenge.

#### Challenge 4: Add Your Name (Super Easy)
Find `# TODO: Add your name!` and replace "Your Name Here":
```python
pygame.display.set_caption("PONG - Your Name Here")
```

#### Challenge 5: Change Paddle Color (Easy)
Find `# TODO: STUDENT CHALLENGE 4` inside the `Paddle` class. Change:
```python
self.color = WHITE
```
To something like `self.color = (0, 255, 0)` for a green paddle!

#### Challenge 6: Change Ball Speed (Medium)
Find `# TODO: STUDENT CHALLENGE 5` inside the `Ball` class `__init__` method. Look for:
```python
self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 8, 4, 4)
```
The last two numbers `(4, 4)` are the speed. Try `(6, 6)` for a faster ball!

#### Challenge 7: Random Direction on Reset (Advanced)
Find `# TODO: STUDENT CHALLENGE 6` inside the `reset` method. Add this code:
```python
import random
self.speed_x = random.choice([-4, 4])
self.speed_y = random.choice([-4, 4])
```

#### Challenge 8: Add Sound Effects (Bonus)
Find `# TODO: STUDENT CHALLENGE 7` inside `handle_collisions`. You'll need a `beep.wav` file, or try:
```python
import pygame
pygame.mixer.init()
beep = pygame.mixer.Sound(pygame.mixer.Sound(buffer=bytes([0]*1000)))  # Silent placeholder
beep.play()
```

### Phase 4: Save Your Work with Git (15 min)

#### 6. See What Changed
```bash
git status
```
This shows which files you modified.

#### 7. Stage Your Changes
```bash
git add main.py
```
Or to stage ALL changes:
```bash
git add .
```

#### 8. Commit with a Message
```bash
git commit -m "Customized colors and game speed"
```

#### 9. Push to GitHub
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

1. **Change paddle speed** - Find `Paddle(..., 7)` and change the last number (speed)
2. **Change paddle size** - Find `Paddle(..., 15, 120, 7)` and change the width (15) or height (120)
3. **Change ball radius** - Find `Ball(..., 8, 4, 4)` and change the 8 to something like 12
4. **Add a second ball** - Create another ball object and update it in the game loop

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| "pip is not recognized" | Reinstall Python and check "Add to PATH" |
| "pygame not found" | Run `pip install pygame` again |
| Game runs super fast/slow | Check `FPS = 60` in main.py |
| Can't push to GitHub | Make sure you forked (not cloned directly from instructor) |
| VS Code can't find Python | `Ctrl+Shift+P` → "Python: Select Interpreter" → choose the one with Python 3.8+ |
| "python" command not found | Try `py` or `python3` instead |
| Game window is blank | Make sure you didn't delete `screen.fill(BLACK)` |

## 📚 Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [RGB Color Picker](https://rgbcolorpicker.com/)
