import sys

def main():
    # Default parameter
    param = "customtkinter"
    
    # Check if an argument is provided
    if len(sys.argv) > 1:
        param = sys.argv[1].lower()
    
    if param == "pygame":
        print("Pygame parameter selected")
        # Add your pygame related code here
    elif param == "tkinter":
        print("Tkinter parameter selected")
        # Add your tkinter related code here
    elif param == "customtkinter":
        print("CustomTkinter parameter selected")
        # Add your customtkinter related code here
    else:
        print(f"Unknown parameter: {param}")
        sys.exit(1)

if __name__ == "__main__":
    main()
