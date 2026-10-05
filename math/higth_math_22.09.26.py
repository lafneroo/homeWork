import math
import random
import cmath
import matplotlib.pyplot as plt


def to_polar(a, b):
    r = math.sqrt(a * a + b * b)
    phi = math.atan2(b, a)
    return r, phi


def to_algebraic(r, phi):
    a = r * math.cos(phi)
    b = r * math.sin(phi)
    return a, b


def check_level1():
    print("Уровень 1: конвертация")
    a, b = 3, -4
    r, phi = to_polar(a, b)
    a2, b2 = to_algebraic(r, phi)
    print("Исходное:", (a, b), "-> полярное:", (round(r, 4), round(phi, 4)),
          "-> обратно:", (round(a2, 4), round(b2, 4)))

    for _ in range(5):
        a = random.uniform(-10, 10)
        b = random.uniform(-10, 10)
        r1, phi1 = to_polar(a, b)
        r2, phi2 = cmath.polar(complex(a, b))
        assert math.isclose(r1, r2, rel_tol=1e-9)
        assert math.isclose(phi1, phi2, abs_tol=1e-9)

        a1, b1 = to_algebraic(r1, phi1)
        z3 = cmath.rect(r2, phi2)
        assert math.isclose(a1, z3.real, abs_tol=1e-9)
        assert math.isclose(b1, z3.imag, abs_tol=1e-9)
    print("Сверка с cmath пройдена.")
    print()


def power_demoivre(a, b, n):
    r, phi = to_polar(a, b)
    r_n = math.pow(r, n)
    phi_n = phi * n
    return to_algebraic(r_n, phi_n)


def check_level2_moivre():
    print("Уровень 2: формула Муавра")
    for _ in range(5):
        a = random.uniform(-5, 5)
        b = random.uniform(-5, 5)
        n = random.randint(1, 8)
        got = power_demoivre(a, b, n)
        expected = complex(a, b) ** n
        print(f"({a:.3f}+{b:.3f}i)^{n}: got=({got[0]:.4f}, {got[1]:.4f}) "
              f"vs expected=({expected.real:.4f}, {expected.imag:.4f})")
    print()


def rotate_shape(points, angle_deg):
    rot = cmath.rect(1, math.radians(angle_deg))
    result = []
    for x, y in points:
        z = complex(x, y) * rot
        result.append((z.real, z.imag))
    return result


def draw_shape(pts, color, label):
    closed = list(pts) + [pts[0]]
    xs, ys = zip(*closed)
    plt.plot(xs, ys, color=color, marker='o', label=label)


def check_rotation():
    print("Уровень 2: поворот корабля")
    ship = [(0, 1), (-0.6, -1), (0, -0.5), (0.6, -1)]
    rotated = rotate_shape(ship, 40)

    plt.figure(figsize=(6, 6))
    draw_shape(ship, 'gray', 'до поворота')
    draw_shape(rotated, 'purple', 'после поворота на 40')
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.savefig("ship_rotation.png", dpi=120)
    plt.show()
    print("Сохранено ship_rotation.png")
    print()


def spirograph(turns=8, points_per_turn=200, growth=0.02, r0=1.0, delta_phi=0.3):
    total = turns * points_per_turn
    xs, ys = [], []
    for k in range(total):
        r_k = r0 * math.pow(1 + growth, k)
        phi_k = k * delta_phi
        a, b = to_algebraic(r_k, phi_k)
        xs.append(a)
        ys.append(b)
    return xs, ys


def check_spirograph():
    print("BOSS: спирограф")
    xs, ys = spirograph(turns=8, points_per_turn=200, growth=0.02, delta_phi=0.3)
    plt.figure(figsize=(5, 5))
    plt.plot(xs, ys, linewidth=0.8, color='indigo')
    plt.axis('off')
    plt.gca().set_aspect('equal')
    plt.savefig("spirograph.png", dpi=150)
    plt.show()
    print("Сохранено spirograph.png")
    print()


def check_tasks():
    print("Задачи 1-5")

    r, phi = to_polar(1, math.sqrt(3))
    print(f"Задача 1: r={r:.4f}, phi={phi:.4f} (ожидаем 2, pi/3={math.pi/3:.4f})")

    got = power_demoivre(1, 1, 10)
    print(f"Задача 2: (1+i)^10 = ({got[0]:.4f}, {got[1]:.4f}) (ожидаем (0, 32))")

    r1, phi1 = to_polar(-1, 3)
    r2, phi2 = to_polar(-math.sqrt(3), -2)
    print(f"Задача 3: z1: r={r1:.4f}, phi={phi1:.4f} ({math.degrees(phi1):.1f} deg)")
    print(f"          z2: r={r2:.4f}, phi={phi2:.4f} ({math.degrees(phi2):.1f} deg)")

    r_prod = 2 * 5
    phi_prod = math.radians(40 + 20)
    r_div = 2 / 5
    phi_div = math.radians(40 - 20)
    print(f"Задача 4: z1*z2 = {r_prod}(cos{math.degrees(phi_prod):.0f} + i sin{math.degrees(phi_prod):.0f})")
    print(f"          z1/z2 = {r_div}(cos{math.degrees(phi_div):.0f} + i sin{math.degrees(phi_div):.0f})")

    got5 = power_demoivre(math.sqrt(3) / 2, 0.5, 12)
    print(f"Задача 5: результат = ({got5[0]:.6f}, {got5[1]:.6f}) (ожидаем (1, 0))")
    print()


if __name__ == "__main__":
    check_tasks()
    check_level1()
    check_level2_moivre()
    check_rotation()
    check_spirograph()