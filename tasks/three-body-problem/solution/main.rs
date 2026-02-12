use std::fs::File;
use std::io::Write;

const DT: f64 = 0.01;
const N_STEPS: usize = 1000;
const SNAPS: [usize; 4] = [0, 10, 100, 1000];
const N: usize = 3;
const S: usize = N * 4;
type State = [f64; 12];

fn deriv(s: &State) -> State {
    let mut d = [0.0; S];
    for i in 0..N {
        d[2 * i] = s[6 + 2 * i];
        d[2 * i + 1] = s[6 + 2 * i + 1];
    }
    for i in 0..N {
        let (mut ax, mut ay) = (0.0, 0.0);
        for j in 0..N {
            if i == j { continue; }
            let dx = s[2 * j] - s[2 * i];
            let dy = s[2 * j + 1] - s[2 * i + 1];
            let r3 = (dx * dx + dy * dy).powf(1.5);
            ax += dx / r3;
            ay += dy / r3;
        }
        d[6 + 2 * i] = ax;
        d[6 + 2 * i + 1] = ay;
    }
    d
}

fn add(a: &State, b: &State) -> State {
    let mut r = [0.0; S];
    for i in 0..S { r[i] = a[i] + b[i]; }
    r
}

fn mul(s: &State, c: f64) -> State {
    let mut r = [0.0; S];
    for i in 0..S { r[i] = s[i] * c; }
    r
}

fn rk4(s: &State) -> State {
    let k1 = deriv(s);
    let k2 = deriv(&add(s, &mul(&k1, DT / 2.0)));
    let k3 = deriv(&add(s, &mul(&k2, DT / 2.0)));
    let k4 = deriv(&add(s, &mul(&k3, DT)));
    let mut r = [0.0; S];
    for i in 0..S {
        r[i] = s[i] + (DT / 6.0) * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]);
    }
    r
}

fn main() {
    let mut s: State = [
        0.0, 1.0, -0.87, -0.5, 0.87, -0.5,
        0.5, 0.0, -0.25, 0.43, -0.25, -0.43,
    ];

    let mut f = File::create("/app/output.csv").unwrap();
    writeln!(f, "t,x0,y0,x1,y1,x2,y2,vx0,vy0,vx1,vy1,vx2,vy2").unwrap();

    let mut si = 0;
    for step in 0..=N_STEPS {
        if si < SNAPS.len() && step == SNAPS[si] {
            let t = step as f64 * DT;
            writeln!(f, "{:.15e},{:.15e},{:.15e},{:.15e},{:.15e},{:.15e},{:.15e},{:.15e},{:.15e},{:.15e},{:.15e},{:.15e},{:.15e}",
                t, s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11]).unwrap();
            si += 1;
        }
        if step < N_STEPS { s = rk4(&s); }
    }
}
