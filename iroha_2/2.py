def judgeIentersected(ax, ay, bx, by, cx, cy, dx, dy):
    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)
    return tc * td < 0 and ta * tb < 0


x, y = map(int, input().split())
a, b = map(int, input().split())
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
if judgeIentersected(0, a, x, b, sx, sy, tx, ty):
    print('Yes')
else:
    print('No')
