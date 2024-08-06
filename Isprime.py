def is_prime(func):
    def wrapper(*args, **kwargs):
        resul = func(*args, **kwargs)
        if resul > 1:
            for i in range(2, resul):
                if resul % i == 0:
                    print("Составное")
                    break

            else:
                print("Простое")
        else:
            print("Составное")
        return resul

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
