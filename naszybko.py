def map_to_points_and_lines(p):
    n = len(p)
    L = [(p[i], p[(i + 1) % n]) for i in range(n)]
    P = [Point(p[i][0], p[i][1]) for i in range(n)]

    return P, L


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.chain = None
        self.index = None

    def set_chain(self, chain):
        self.chain = chain

    def get_coords(self):
        return (self.x, self.y)


def is_connective_or_separative(a, b, c):
    determinant = orient(a, b, c)
    if a[1] > b[1] and c[1] > b[1] and determinant < -EPS:
        return True
    elif a[1] < b[1] and c[1] < b[1] and determinant < -EPS:
        return True
    return False


def y_monotonic(points):
    for i in range(0, len(points) - 1):
        if is_connective_or_separative(points[i - 1], points[i], points[i + 1]):
            return False

    if is_connective_or_separative(points[-2], points[-1], points[0]):
        return False
    return True


EPS = 1e-12
def orient(a, b, c):
    return a[0]*b[1] + a[1]*c[0] + b[0]*c[1] - b[1]*c[0] - a[1]*b[0] - a[0]*c[1]

def inside_polygon(a, b, c, chain):
    o = orient(a, b, c)

    if abs(o) < EPS:
        return False

    if chain == 1:
        return o < 0
    else:
        return o > 0


def do_not_follow(p1, p2, n):
    return abs(p1.index - p2.index) != 1 and abs(p1.index - p2.index) != n - 1


def triangulate(p):
    if not y_monotonic(p):
        print('Wielokąt nie jest monotoniczny!')
        return None, None

    P, L = map_to_points_and_lines(p)
    n = len(P)

    min_index = P.index(min(P, key=lambda v: v.y))
    max_index = P.index(max(P, key=lambda v: v.y))

    x = max_index
    while x != min_index:
        P[x].chain = 1
        P[x].index = x
        x = (x + 1) % n

    while x != max_index:
        P[x].chain = 2
        P[x].index = x
        x = (x + 1) % n

    P = sorted(P, key=lambda v: v.y, reverse=True)

    stack = []
    stack.append(P[0])
    stack.append(P[1])
    scenes = []

    diagonals = []

    for i in range(2, n):

        if P[i].chain != stack[-1].chain:
            first = stack[-1]
            while len(stack) > 1:
                top = stack.pop()
                if do_not_follow(P[i], top, n):
                    diagonals.append((P[i].get_coords(), top.get_coords()))

            stack.pop()
            stack.append(first)
        else:
            top = stack.pop()
            top_prev = stack.pop()
            while inside_polygon(P[i].get_coords(), top.get_coords(), top_prev.get_coords(), P[i].chain):
                if do_not_follow(P[i], top_prev, n):
                    diagonals.append((P[i].get_coords(), top_prev.get_coords()))

                if not len(stack):
                    stack = stack + [top_prev]
                    break
                top, top_prev = top_prev, stack.pop()
            else:
                stack = stack + [top_prev, top]
        stack.append(P[i])



    return diagonals


points=[[-0.05080846909553775, -0.04829350695890539],
[0.04255846638833323, -0.0385202226451799],
[0.028364918001236444, -0.03110600695890539],
[0.044776208323817096, -0.022680761860866164],
[0.015945563162526766, -0.0159405657824348],
[0.048546369614139676, -0.0017861540177289137],
[0.030582659936720324, 0.004954042060702463],
[0.052316530904462255, 0.015738355786192662],
[0.04011895025930097, 0.020119483237173053],
[0.05276007929155904, 0.029218747943055415],
[0.02237701477543, 0.03595894402148679],
[0.048546369614139676, 0.042362130295996586],
[0.04189314380768806, 0.04708026755089856],
[0.028143143807688065, 0.052472424413643665],
[0.0137278212270429, 0.0541574734332515]]
print(triangulate(points)[-1])