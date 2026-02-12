import os

OUTPUT = "/app/decrypted.txt"
EXPECTED = "I hope you all have a lot of fun during this Harbor workshop!"


def test_decrypted_file_exists():
    assert os.path.exists(OUTPUT), "decrypted.txt should exist in /app"


def test_decrypted_message_matches():
    with open(OUTPUT) as f:
        content = f.read().strip()
    assert content == EXPECTED, f"Expected '{EXPECTED}', got '{content}'"
