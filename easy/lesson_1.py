

def pythagorean_triangle(l:list[int]) -> bool:
    n = len(l)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a, b, c = sorted([l[i], l[j], l[k]])
                if a ** 2 + b ** 2 == c ** 2:
                    return True
    return False


def test_pythagorean_triangle():
    assert pythagorean_triangle([5, 3, 4]) == True
    assert pythagorean_triangle([6, 8, 10]) == True
    assert pythagorean_triangle([100, 3, 65]) == False
    print("All tests passed!")

test_pythagorean_triangle()
