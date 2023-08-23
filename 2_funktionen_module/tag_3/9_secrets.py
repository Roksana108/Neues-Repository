"""
Das -modul secrest deint zur Generierung krypograpischen starker Zufallszahlen
"""
import secrets
secrets.compare_digest

print(f"token_urlsafe: {secrets.token_urlsafe(nbytes=32)}")  # 32 bytes base64 encoded
print(f"token hex: {secrets.token_hex(nbytes=4)}")  # 4 Bytes hex Token
print(f"bits: {secrets.randbits(k=8)}")  # 2 ** 8 bit