def outer():
    results = []
    def inner(x):
        result = x**2
        results.append(result)
        print(f"Results so far: {results}")
    return inner

def main():
    f = outer()
    print(f"Resulyt for f3 is: {f(3)}")
    print(f"Results for f4 is: {f(4)}")
    print(f"Result for f3 again is: {f(3)}")

if __name__ == '__main__':
    main()