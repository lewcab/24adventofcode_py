def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    memory = [ln.strip() for ln in lines]

    print(f"Number of lines: {len(memory)}")
    print(memory)


if __name__ == '__main__':
    main()
