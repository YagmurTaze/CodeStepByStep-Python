def to_binary(n):
    bin = ""
    if n == 0:
        return "0"
    while n > 0:
        bin += str(n % 2)
        n = n // 2
    return bin[::-1]
