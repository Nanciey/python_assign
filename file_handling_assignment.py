try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("First line\n")
        file.write("Second line with a number: 42\n")
        file.write("Third line with a float: 3.14\n")
        print("File 'my_file.txt' created successfully.")

    # File Reading and Display
    print("\nReading 'my_file.txt' and displaying contents:")
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Fourth line with a string: Hello!\n")
        file.write("Fifth line with a number: 12345\n")
        file.write("Sixth line with a float: 2.71828\n")
        print("\nThree lines appended to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("Script execution completed.")
