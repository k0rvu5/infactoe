import pygame
import sys
from typing import List, Tuple

class Player:
    def __init__(self, symbol: str, color: Tuple[int, int, int]) -> None:
        """Initialize a player with their symbol and color."""
        self.symbol: str = symbol
        self.color: Tuple[int, int, int] = color
        self.active_cells: List[Tuple[int, int]] = []

    def make_move(self, board: List[List[str]], row: int, column: int) -> None:
        """Make a move on the board and track active cells."""
        # Remove the oldest cell if we have 3 active cells
        if len(self.active_cells) == 3:
            old_row, old_col = self.active_cells.pop(0)
            board[old_row][old_col] = " "
        
        # Add the new move
        self.active_cells.append((row, column))
        board[row][column] = self.symbol

    def clear_moves(self) -> None:
        """Clear all active cells for this player."""
        self.active_cells.clear()


class Game:
    def __init__(self) -> None:
        """Initialize the game with pygame and set up the game state."""
        pygame.init()
        self.WIDTH: int = 600
        self.HEIGHT: int = 600
        self.GRID_WIDTH: int = 4
        self.CELL_SIZE: int = self.WIDTH // 3
        
        # Colors
        self.BG_COLOR: Tuple[int, int, int] = (30, 30, 46)
        self.GRID_COLOR: Tuple[int, int, int] = (205, 214, 244)
        self.TEXT_COLOR: Tuple[int, int, int] = (255, 255, 255)
        
        # Initialize display
        self.screen: pygame.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        
        # Initialize game state
        self.board: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]
        self.players: List[Player] = [
            Player("X", (243, 139, 168)),
            Player("O", (116, 199, 236))
        ]
        self.player_turn: bool = False  # False for Player X, True for Player O
        self.game_over: bool = False
        self.winner: str = None

    def clear_board(self) -> None:
        """Reset the game state."""
        # Clear the board
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        # Clear player moves
        for player in self.players:
            player.clear_moves()
        
        # Reset game state
        self.player_turn = False
        self.game_over = False
        self.winner = None

    def draw_grid(self) -> None:
        """Draw the game grid with improved visibility."""
        for i in range(1, 3):
            # Vertical lines
            pygame.draw.rect(
                self.screen,
                self.GRID_COLOR,
                (i * self.CELL_SIZE - self.GRID_WIDTH // 2, 0, self.GRID_WIDTH, self.HEIGHT)
            )
            # Horizontal lines
            pygame.draw.rect(
                self.screen,
                self.GRID_COLOR,
                (0, i * self.CELL_SIZE - self.GRID_WIDTH // 2, self.WIDTH, self.GRID_WIDTH)
            )

    def draw_board(self) -> None:
        """Draw the current state of the board with improved visuals."""
        # Draw all active cells for both players
        for player in self.players:
            for i, (row, col) in enumerate(player.active_cells):
                # Use darker color for the oldest cell (index 0)
                if player.symbol == "X":
                    if i == 0 and len(player.active_cells) == 3:
                        color = tuple(c // 2 for c in player.color)
                    else:
                        color = player.color
                else:
                    if i == 0 and len(player.active_cells) == 3:
                        color = tuple(c // 2 for c in player.color)
                    else:
                        color = player.color
                
                # Draw the symbol with adjusted color
                font = pygame.font.Font(None, 160)
                text = font.render(player.symbol, True, color)
                text_rect = text.get_rect(
                    center=(
                        col * self.CELL_SIZE + self.CELL_SIZE // 2,
                        row * self.CELL_SIZE + self.CELL_SIZE // 2
                    )
                )
                self.screen.blit(text, text_rect)

    def get_cell(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """Convert screen coordinates to board coordinates."""
        row = pos[1] // self.CELL_SIZE
        column = pos[0] // self.CELL_SIZE
        return (row, column)

    def check_winner(self) -> str:
        """Check for a winner and return the winning symbol."""
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def draw_game_over(self) -> None:
        """Draw the game over message with improved visibility."""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(self.BG_COLOR)
        self.screen.blit(overlay, (0, 0))

        # Game over message
        font = pygame.font.Font(None, 74)
        if self.winner:
            text = font.render(f"{self.winner} wins!", True, self.TEXT_COLOR)
        else:
            text = font.render("It's a draw!", True, self.TEXT_COLOR)
        
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(text, text_rect)

        # Restart instructions
        font_small = pygame.font.Font(None, 36)
        restart_text = font_small.render("Press SPACE to restart", True, self.TEXT_COLOR)
        restart_rect = restart_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

    def handle_input(self) -> None:
        """Handle user input with improved controls."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            
            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                cell = self.get_cell(event.pos)
                if 0 <= cell[0] < 3 and 0 <= cell[1] < 3 and self.board[cell[0]][cell[1]] == " ":
                    self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                    self.player_turn = not self.player_turn
            
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.clear_board()
                else:
                    if event.key == pygame.K_1:
                        cell = (0, 0)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_2:
                        cell = (0, 1)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_3:
                        cell = (0, 2)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_4:
                        cell = (1, 0)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_5:
                        cell = (1, 1)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_6:
                        cell = (1, 2)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_7:
                        cell = (2, 0)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_8:
                        cell = (2, 1)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_9:
                        cell = (2, 2)
                        if self.board[cell[0]][cell[1]] == " ":
                            self.players[self.player_turn].make_move(self.board, cell[0], cell[1])
                            self.player_turn = not self.player_turn
                    elif event.key == pygame.K_r:
                        self.clear_board()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit(0)


    def run(self) -> None:
        """Main game loop with improved visuals and responsiveness."""
        clock = pygame.time.Clock()

        while True:
            self.handle_input()
            
            # Clear screen and draw background
            self.screen.fill(self.BG_COLOR)
            
            # Draw game elements
            self.draw_grid()
            self.draw_board()
            
            # Check for game over conditions
            if not self.game_over:
                self.winner = self.check_winner()
                if self.winner or all(cell != " " for row in self.board for cell in row):
                    self.game_over = True
            
            # Draw game over screen if needed
            if self.game_over:
                self.draw_game_over()
            
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
