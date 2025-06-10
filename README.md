# Infactoe

A unique twist on the classic Tic-tac-toe game where players can only have 3 active cells at a time.

## 📝 Description

Infactoe is a strategic variation of Tic-tac-toe where players must carefully manage their moves. Each player can only have 3 active cells at a time, and when they make their 4th move, their oldest cell is removed. This creates an interesting strategic element where players must balance maintaining winning combinations while managing their active cells.

## ✨ Features

- 🎮 Classic 3x3 grid gameplay with a twist
- 🔄 Limited to 3 active cells per player
- 🎨 Visual indication of which cell will be removed next (darker color)
- 💫 Modern, clean interface
- 🎯 Smooth animations and visual feedback

## 🎲 Rules

1. Players take turns placing their marks (X or O) on the grid
2. Each player can only have 3 active cells at a time
3. When a player makes their 4th move, their oldest cell is removed
4. The game continues until a player gets 3 of their marks in a row (horizontally, vertically, or diagonally)

## 🎮 How to Play

### Controls
- Click on any empty cell to place your mark
- Press SPACE to restart after a game ends
- Close the window to quit

### Visual Indicators
- X's are shown in red
- O's are shown in blue
- The oldest cell (which will be removed on the next move) appears in a darker shade
- Game over messages show the winner or indicate a draw

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/k0rvu5/infactoe.git
   cd infactoe
   ```

2. Install the required package:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 💡 Strategy Tips

- Plan your moves carefully as older cells will be removed
- Try to maintain a winning combination while managing your active cells
- Watch your opponent's oldest cell to predict their next move
- Sometimes it's better to remove your own cell to prevent your opponent from winning

## 📋 Requirements

- Python 3.x
- Pygame

## 📄 License

This project is open source and available under the MIT License.
