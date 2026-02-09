#!/bin/bash



JUNIT_OUTPUT="${JUNIT_OUTPUT:-/logs/verifier/junit.xml}"
TIMEOUT="${TIMEOUT:-30}"

# Parse BIOME arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --junit-output-path)
      JUNIT_OUTPUT="$2"
      shift 2
      ;;
    --individual-timeout)
      TIMEOUT="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

# Run pytest directly (already installed)
# Use path relative to code_root (/app)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pytest --timeout="$TIMEOUT" \
  --ctrf /logs/verifier/ctrf.json \
  --junitxml="$JUNIT_OUTPUT" \
  "$SCRIPT_DIR/test_outputs.py" -rA

if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
