import random
import sys
import time
import pygame
from pygame.locals import *
from datetime import datetime
from absl import app, flags

# Flags
FLAGS = flags.FLAGS
flags.DEFINE_boolean("log_data", True, "Whether to log data.")
flags.DEFINE_string(
    "player_id", input("Enter a unique user ID: "), "The ID of the player."
)

# Constants
FPS = 30
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FLASH_SPEED = 500  # in milliseconds
FLASH_DELAY = 200  # in milliseconds
BUTTON_SIZE = 200
BUTTON_GAP_SIZE = 20
TIMEOUT = 4  # seconds before game over if no button is pushed

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHT_RED = (255, 0, 0)
RED = (155, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
GREEN = (0, 155, 0)
BRIGHT_BLUE = (0, 0, 255)
BLUE = (0, 0, 155)
BRIGHT_YELLOW = (255, 255, 0)
YELLOW = (155, 155, 0)
DARK_GRAY = (40, 40, 40)

# Button positions
YELLOW_RECT = pygame.Rect(BUTTON_GAP_SIZE, BUTTON_GAP_SIZE, BUTTON_SIZE, BUTTON_SIZE)
BLUE_RECT = pygame.Rect(
    BUTTON_GAP_SIZE + BUTTON_SIZE + BUTTON_GAP_SIZE,
    BUTTON_GAP_SIZE,
    BUTTON_SIZE,
    BUTTON_SIZE,
)
RED_RECT = pygame.Rect(
    BUTTON_GAP_SIZE,
    BUTTON_GAP_SIZE + BUTTON_SIZE + BUTTON_GAP_SIZE,
    BUTTON_SIZE,
    BUTTON_SIZE,
)
GREEN_RECT = pygame.Rect(
    BUTTON_GAP_SIZE + BUTTON_SIZE + BUTTON_GAP_SIZE,
    BUTTON_GAP_SIZE + BUTTON_SIZE + BUTTON_GAP_SIZE,
    BUTTON_SIZE,
    BUTTON_SIZE,
)


def log_data(event, timestamp, score, log_file_name):
    """
    Logs game data to a CSV file.

    Args:
        event (str): The event to log (e.g., button color).
        timestamp (float): The timestamp of the event.
        score (int): The current score.
        log_file_name (str): The name of the log file.
    """
    with open(log_file_name, "a") as log_file:
        log_file.write(f"{event},{timestamp},{score}\n")


def main(_):
    """
    The main game loop.
    """
    global FPS_CLOCK, DISPLAY_SURF, BASIC_FONT, BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Simulate")

    BASIC_FONT = pygame.font.Font("freesansbold.ttf", 16)

    info_surf = BASIC_FONT.render(
        "Match the pattern by clicking on the button or using the Q, W, A, S keys.",
        True,
        WHITE,
    )
    info_rect = info_surf.get_rect()
    info_rect.topleft = (10, WINDOW_HEIGHT - 25)

    # Load sound files
    BEEP1 = pygame.mixer.Sound("beep1.ogg")
    BEEP2 = pygame.mixer.Sound("beep2.ogg")
    BEEP3 = pygame.mixer.Sound("beep3.ogg")
    BEEP4 = pygame.mixer.Sound("beep4.ogg")

    # Initialize game variables
    pattern = []
    current_step = 0
    last_click_time = 0
    score = 0
    waiting_for_input = False
    user_response_start_time = 0
    bg_color = BLACK

    # Create log file
    if FLAGS.log_data:
        timestamp = datetime.now().strftime("%d_%H_%M")
        log_file_name = f"simon_log_{FLAGS.player_id}_{timestamp}.csv"
        with open(log_file_name, "w") as log_file:
            log_file.write("Event,Timestamp,Score\n")

    # Game loop
    while True:
        clicked_button = None
        DISPLAY_SURF.fill(bg_color)
        draw_buttons()

        score_surf = BASIC_FONT.render("Score: " + str(score), True, WHITE)
        score_rect = score_surf.get_rect()
        score_rect.topleft = (WINDOW_WIDTH - 100, 10)
        DISPLAY_SURF.blit(score_surf, score_rect)

        DISPLAY_SURF.blit(info_surf, info_rect)

        check_for_quit()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                clicked_button = get_button_clicked(mouse_x, mouse_y)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clicked_button = YELLOW
                elif event.key == K_w:
                    clicked_button = BLUE
                elif event.key == K_a:
                    clicked_button = RED
                elif event.key == K_s:
                    clicked_button = GREEN

        if not waiting_for_input:
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
            for button in pattern:
                flash_button_animation(button)
                pygame.time.wait(FLASH_DELAY)
            waiting_for_input = True
            user_response_start_time = (
                time.time()
            )  # Start the clock for the first click
        else:
            if clicked_button and clicked_button == pattern[current_step]:
                flash_button_animation(clicked_button)
                color = get_button_color(clicked_button)
                timestamp = time.time() - user_response_start_time
                if FLAGS.log_data:
                    log_data(color, timestamp, score, log_file_name)
                current_step += 1
                user_response_start_time = (
                    time.time()
                )  # Reset the clock after each click

                if current_step == len(pattern):
                    score += 1
                    waiting_for_input = False
                    current_step = 0

            elif (clicked_button and clicked_button != pattern[current_step]) or (
                current_step != 0 and time.time() - TIMEOUT > user_response_start_time
            ):
                game_over_animation()
                pattern = []
                current_step = 0
                waiting_for_input = False
                score = 0
                pygame.time.wait(1000)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def get_button_color(button):
    """
    Returns the color name of the given button.

    Args:
        button (pygame.Rect): The button rectangle.

    Returns:
        str: The color name of the button.
    """
    if button == YELLOW:
        return "yellow"
    elif button == BLUE:
        return "blue"
    elif button == RED:
        return "red"
    elif button == GREEN:
        return "green"
    return None


def terminate():
    """
    Terminates the game.
    """
    pygame.quit()
    sys.exit()


def check_for_quit():
    """
    Checks for quit events (closing the window or pressing the ESC key).
    """
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def flash_button_animation(color, animation_speed=50):
    """
    Flashes a button with the given color.

    Args:
        color (tuple): The color of the button to flash.
        animation_speed (int): The speed of the flashing animation.
    """
    if color == YELLOW:
        sound = BEEP1
        flash_color = BRIGHT_YELLOW
        rectangle = YELLOW_RECT
    elif color == BLUE:
        sound = BEEP2
        flash_color = BRIGHT_BLUE
        rectangle = BLUE_RECT
    elif color == RED:
        sound = BEEP3
        flash_color = BRIGHT_RED
        rectangle = RED_RECT
    elif color == GREEN:
        sound = BEEP4
        flash_color = BRIGHT_GREEN
        rectangle = GREEN_RECT

    orig_surf = DISPLAY_SURF.copy()
    flash_surf = pygame.Surface((BUTTON_SIZE, BUTTON_SIZE))
    flash_surf = flash_surf.convert_alpha()
    r, g, b = flash_color
    sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)):  # animation loop
        for alpha in range(start, end, animation_speed * step):
            check_for_quit()
            DISPLAY_SURF.blit(orig_surf, (0, 0))
            flash_surf.fill((r, g, b, alpha))
            DISPLAY_SURF.blit(flash_surf, rectangle.topleft)
            pygame.display.update()
            FPS_CLOCK.tick(FPS)
    DISPLAY_SURF.blit(orig_surf, (0, 0))


def draw_buttons():
    """
    Draws the buttons on the screen.
    """
    pygame.draw.rect(DISPLAY_SURF, YELLOW, YELLOW_RECT)
    pygame.draw.rect(DISPLAY_SURF, BLUE, BLUE_RECT)
    pygame.draw.rect(DISPLAY_SURF, RED, RED_RECT)
    pygame.draw.rect(DISPLAY_SURF, GREEN, GREEN_RECT)


def game_over_animation(color=WHITE, animation_speed=50):
    """
    Plays the game over animation.

    Args:
        color (tuple): The color of the animation.
        animation_speed (int): The speed of the animation.
    """
    # Play all beeps at once, then flash the background
    orig_surf = DISPLAY_SURF.copy()
    flash_surf = pygame.Surface(DISPLAY_SURF.get_size())
    flash_surf = flash_surf.convert_alpha()
    BEEP1.play()  # play all four beeps at the same time, roughly.
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    r, g, b = color
    for i in range(3):  # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animation_speed * step):  # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                check_for_quit()
                flash_surf.fill((r, g, b, alpha))
                DISPLAY_SURF.blit(orig_surf, (0, 0))
                DISPLAY_SURF.blit(flash_surf, (0, 0))
                draw_buttons()
                pygame.display.update()
                FPS_CLOCK.tick(FPS)


def get_button_clicked(x, y):
    """
    Returns the button that was clicked based on the mouse coordinates.

    Args:
        x (int): The x-coordinate of the mouse click.
        y (int): The y-coordinate of the mouse click.

    Returns:
        pygame.Rect: The button that was clicked, or None if no button was clicked.
    """
    if YELLOW_RECT.collidepoint((x, y)):
        return YELLOW
    elif BLUE_RECT.collidepoint((x, y)):
        return BLUE
    elif RED_RECT.collidepoint((x, y)):
        return RED
    elif GREEN_RECT.collidepoint((x, y)):
        return GREEN
    return None


if __name__ == "__main__":
    app.run(main)
