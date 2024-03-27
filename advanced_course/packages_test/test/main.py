from barcode import Code128
from barcode.writer import ImageWriter


code_text = str(input())

# Or to an actual file:
with open("some_file.jpeg", "wb") as f:
    Code128(code_text, writer=ImageWriter()).write(f)
