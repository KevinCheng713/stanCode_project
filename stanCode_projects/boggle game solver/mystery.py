def main():
    print(mystery(348))


def mystery(n):
    if n < 10:
        return 10*n+n
    else:
        a = mystery(n // 10)
        b = mystery(n % 10)
        return 100*a+b


if __name__ == '__main__':
    main()
