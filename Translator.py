import zlib


class Translator:

    def __init__(self, input_text: str):
        if input_text.__contains__("🥵"):
            input_text = input_text.replace(" ", "").replace("\n", "")
            decoded_text = input_text.replace("🥵", "0").replace("🥶", "1")
            byte = int(decoded_text, 2).to_bytes((len(decoded_text) + 7) // 8, byteorder='big')
            decoded_text = (zlib.decompress(byte))
            self.translated = str(decoded_text)[:-1][2:]
        else:
            encoded_text = str.encode(input_text)
            encoded_text = (zlib.compress(encoded_text))
            bit_string = ''.join(format(byte, '08b') for byte in encoded_text)
            encoded_text = bit_string.replace("0", "🥵").replace("1", "🥶")
            self.translated = encoded_text

    def __str__(self):
        return self.translated
