def main():
    print("Hello, World!")
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    data = [ln.strip() for ln in lines]
    m = len(data)
    n = len(data[0])

    print(f"Dimensions: {m} * {n}")


if __name__ == '__main__':
    main()
