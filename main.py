from breath_timer import BreathTimer


if __name__ == '__main__':
    print("Welcome to the Breath Tiimer inspired by the Book Breath by James Nestor.\n You can buy it here; https://a.co/d/fDpfxxc")
    breath_time = input("How many minutes do you want to breath for?: ")
    try:
        breath_time_seconds = int(breath_time)*60
        print("\nAlright starting timer\n")

        timer = BreathTimer(breath_time_seconds)
        timer.run()

    except(ValueError):
        print('Your time needs to be in minutes')

    except Exception as Argument:
        print("Something went wrong.\n")
        print(f"{Argument}")

    # TODO: add inhale and exhale cycle