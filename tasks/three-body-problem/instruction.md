Write a Rust program (no external crates) that simulates three equal bodies (m=1, G=1) interacting via Newtonian gravity in 2D. Integrate with dt=0.01 for total time 10.0. Positions and energy must be accurate to 0.1% tolerance. There is no internet access; Rust toolchain is pre-installed.

Write snapshots at t=0, 0.1, 1, 10 to `/app/output.csv` with a header row. Initial state (t=0 row):

```
t,x0,y0,x1,y1,x2,y2,vx0,vy0,vx1,vy1,vx2,vy2
0,0,1,-0.87,-0.5,0.87,-0.5,0.5,0,-0.25,0.43,-0.25,-0.43
```
