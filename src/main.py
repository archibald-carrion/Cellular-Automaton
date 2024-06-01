import generic_cellular_automaton

def main():
    # Create an instance of the GameOfLife class
    application = generic_cellular_automaton.GameOfLife(50, 50)
    application.run()


if __name__ == "__main__":
    main()
