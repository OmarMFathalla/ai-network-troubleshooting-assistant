from pathlib import Path
import re

nfc_file = Path.home() / "OneDrive" / "Desktop" / "GitHub213.nfc"

text = nfc_file.read_text(encoding="utf-8")

hex_bytes = []

for line in text.splitlines():
    match = re.match(r"Page \d+:\s+((?:[0-9A-Fa-f]{2}\s*)+)", line)
    if match:
        hex_bytes.extend(match.group(1).split())

data = bytes.fromhex(" ".join(hex_bytes))

print("RAW BYTES:")
print(data)

print("\nREADABLE TEXT:")
print("".join(chr(b) if 32 <= b <= 126 else "." for b in data))
# Search the decoded NFC memory for URL-like text
readable = "".join(chr(b) if 32 <= b <= 126 else " " for b in data)

url_match = re.search(
    r"(?:https?://)?(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]*)?",
    readable
)

print("\nDETECTED URL:")

if url_match:
    print(url_match.group())
else:
    print("No URL detected.")