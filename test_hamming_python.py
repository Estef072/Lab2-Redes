from client import send_message
import random
import string

def generate_random_string(max_length):
    length = random.randint(3, max_length)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    return random_string

def print_progress_bar(iteration, total, bar_length=40):
    progress = (iteration / total)
    arrow = '=' * int(round(progress * bar_length) - 1)
    spaces = ' ' * (bar_length - len(arrow))

    print(f'\r[{arrow}{spaces}] {int(progress * 100)}%', end='', flush=True)


def testing(amount, string_length, encoding, noise):
    print("Starting test")
    for x in range(amount):
        message = generate_random_string(string_length)
        send_message(message, encoding, noise)
        print_progress_bar(x, amount)
    print("Done")
    send_message("exit", "stop", noise)


if __name__ == "__main__":
    testing(10000, 40, "1", 0.001)