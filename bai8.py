if __name__ == "__main__":
    input_string = input()

    answer = sum(1 for char in input_string if char.isalpha)

    print(answer)