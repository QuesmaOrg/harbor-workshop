#!/bin/bash
set -e

mkdir -p /app/src
cp /solution/main.rs /app/src/main.rs
cp /solution/Cargo.toml /app/Cargo.toml

cd /app
cargo build --release
./target/release/three-body
