import csv
import math

OUTPUT = "/app/output.csv"
TOL = 1e-3

REF = {
    0.1: [(0.04995241296, 0.99712220445), (-0.89248961732, -0.45560246290), (0.84253720436, -0.54151974155)],
    1.0: [(0.44590937456, 0.70208892652), (-0.83559624924, 0.03193467442), (0.38968687469, -0.73402360093)],
    10.0: [(0.42595984679, -0.18819612906), (-1.11903664268, -0.17936960508), (0.69307679589, 0.36756573414)],
}


def load():
    with open(OUTPUT) as f:
        return list(csv.DictReader(f))


def energy(row):
    x = [float(row[f"x{i}"]) for i in range(3)]
    y = [float(row[f"y{i}"]) for i in range(3)]
    vx = [float(row[f"vx{i}"]) for i in range(3)]
    vy = [float(row[f"vy{i}"]) for i in range(3)]
    ke = sum(0.5 * (vx[i] ** 2 + vy[i] ** 2) for i in range(3))
    pe = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            pe -= 1.0 / math.hypot(x[j] - x[i], y[j] - y[i])
    return ke + pe


def test_output_has_4_rows():
    assert len(load()) == 4


def test_position_at_t0_1():
    row = load()[1]
    for i, (rx, ry) in enumerate(REF[0.1]):
        assert abs(float(row[f"x{i}"]) - rx) < TOL, f"body {i} x: got {row[f'x{i}']}, expected {rx}"
        assert abs(float(row[f"y{i}"]) - ry) < TOL, f"body {i} y: got {row[f'y{i}']}, expected {ry}"


def test_position_at_t1():
    row = load()[2]
    for i, (rx, ry) in enumerate(REF[1.0]):
        assert abs(float(row[f"x{i}"]) - rx) < TOL, f"body {i} x: got {row[f'x{i}']}, expected {rx}"
        assert abs(float(row[f"y{i}"]) - ry) < TOL, f"body {i} y: got {row[f'y{i}']}, expected {ry}"


def test_position_at_t10():
    row = load()[3]
    for i, (rx, ry) in enumerate(REF[10.0]):
        assert abs(float(row[f"x{i}"]) - rx) < TOL, f"body {i} x: got {row[f'x{i}']}, expected {rx}"
        assert abs(float(row[f"y{i}"]) - ry) < TOL, f"body {i} y: got {row[f'y{i}']}, expected {ry}"


def test_energy_at_t0_1():
    rows = load()
    e0, e = energy(rows[0]), energy(rows[1])
    assert abs((e - e0) / e0) < TOL, f"t=0.1: relative energy error {abs((e - e0) / e0):.2e}"


def test_energy_at_t1():
    rows = load()
    e0, e = energy(rows[0]), energy(rows[2])
    assert abs((e - e0) / e0) < TOL, f"t=1: relative energy error {abs((e - e0) / e0):.2e}"


def test_energy_at_t10():
    rows = load()
    e0, e = energy(rows[0]), energy(rows[3])
    assert abs((e - e0) / e0) < TOL, f"t=10: relative energy error {abs((e - e0) / e0):.2e}"
