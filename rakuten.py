def solution(start, end):
    def is_prime_number(number, primes):
        for i in primes:
            if number % i == 0:
                return False
        primes.append(number)
        return True

    if start < 2:
        start = 2

    if end < start:
        return []

    primes = [2]
    primes = [i for i in range(3, start) if is_prime_number(i, primes)]

    return [i for i in range(start, end) if is_prime_number(i, primes)]


print(solution(-11, 100))
