from pathlib import Path
import re

SOURCE = Path.home() / "OneDrive" / "Desktop" / "Blank213.nfc"
OUTPUT = Path.home() / "OneDrive" / "Desktop" / "GitHub213.nfc"

TARGET_URL = input("Enter URL: ").strip()

text = SOURCE.read_text(encoding="utf-8")

# Collect all NTAG213 page bytes
pages = {}

for line in text.splitlines():
    match = re.match(r"Page (\d+):\s+((?:[0-9A-Fa-f]{2}\s*)+)", line)
    if match:
        page_number = int(match.group(1))
        page_bytes = bytes.fromhex(match.group(2))
        pages[page_number] = page_bytes

# Build a standard NDEF URI record.
# URI prefix 0x04 means "https://"
uri_body = TARGET_URL.removeprefix("https://").encode("utf-8")

ndef_record = bytes([
    0xD1,             # NDEF record header
    0x01,             # type length
    len(uri_body) + 1,# payload length
    0x55,             # type = URI
    0x04,             # URI prefix = https://
]) + uri_body

# Wrap the NDEF message inside an NFC TLV
payload = bytes([
    0x03,             # NDEF TLV
    len(ndef_record)
]) + ndef_record + bytes([
    0xFE              # terminator TLV
])

# NTAG213 user memory starts at page 4.
# Pad remaining writable user memory with zeros.
user_memory = payload.ljust((40 * 4), b"\x00")

for page_number in range(4, 44):
    start = (page_number - 4) * 4
    pages[page_number] = user_memory[start:start + 4]

# Rewrite only the Page X lines in a fresh copy
output_lines = []

for line in text.splitlines():
    match = re.match(r"Page (\d+):", line)

    if match:
        page_number = int(match.group(1))

        if page_number in pages:
            hex_text = " ".join(f"{b:02X}" for b in pages[page_number])
            output_lines.append(f"Page {page_number}: {hex_text}")
        else:
            output_lines.append(line)
    else:
        output_lines.append(line)

OUTPUT.write_text("\n".join(output_lines) + "\n", encoding="utf-8")

print("Created:")
print(OUTPUT)

print("\nTarget URL:")
print(TARGET_URL)