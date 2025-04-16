import pygame
import random

# 초기화
pygame.init()

# 화면 크기
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 테트리스 블록 모양
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[1, 1, 1, 1]],
    [[1, 1],
     [1, 1]]
]

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# 게임 속도
clock = pygame.time.Clock()
FPS = 10

# 점수 저장 및 불러오기 함수
def save_score(player_name, score):
    with open("high_score.txt", "w") as file:
        file.write(f"{player_name},{score}")

def get_high_score():
    try:
        with open("high_score.txt", "r") as file:
            data = file.read().split(",")
            return data[0], int(data[1])
    except FileNotFoundError:
        return "None", 0

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_piece = self.new_piece()
        self.piece_x = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(self.current_piece[0]) // 2
        self.piece_y = 0
        self.score = 0

    def new_piece(self):
        return random.choice(SHAPES)

    def draw_grid(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, WHITE if self.grid[y][x] else BLACK, rect, 1)

    def draw_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect((self.piece_x + x) * BLOCK_SIZE, (self.piece_y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(screen, RED, rect)

    def move_piece(self, dx, dy):
        if not self.check_collision(dx, dy):
            self.piece_x += dx
            self.piece_y += dy
        elif dy > 0:  # 아래로 이동 중 충돌 시
            self.lock_piece()
            self.clear_lines()
            self.current_piece = self.new_piece()
            self.piece_x = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(self.current_piece[0]) // 2
            self.piece_y = 0
            if self.check_collision():  # 새 블록 생성 후 충돌 시 게임 오버
                print("Game Over")
                pygame.quit()
                exit()

    def check_collision(self, dx=0, dy=0):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.piece_x + x + dx
                    new_y = self.piece_y + y + dy
                    if new_y >= len(self.grid) or new_x < 0 or new_x >= len(self.grid[0]) or self.grid[new_y][new_x]:
                        return True
        return False

    def lock_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.piece_y + y][self.piece_x + x] = 1

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        cleared_lines = len(self.grid) - len(new_grid)
        self.grid = [[0] * len(self.grid[0]) for _ in range(cleared_lines)] + new_grid
        self.score += cleared_lines * 100  # 점수 추가

    def update(self):
        self.move_piece(0, 1)  # 아래로 이동

    def render(self):
        screen.fill(BLACK)
        self.draw_grid()
        self.draw_piece()
        pygame.display.flip()

def main():
    game = Tetris()
    running = True

    # 게임 시작 시 최고 점수 출력
    high_score = get_high_score()
    print(f"최고 점수: {high_score[1]} (플레이어: {high_score[0]})")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_piece(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move_piece(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move_piece(0, 1)

        game.update()
        game.render()
        clock.tick(FPS)

    # 게임 종료 시 점수 저장
    player_name = "Player1"  # 플레이어 이름
    save_score(player_name, game.score)

    pygame.quit()

if __name__ == "__main__":
    main()