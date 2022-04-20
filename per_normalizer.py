import parsivar
from tqdm import tqdm
import re


class Normalizer:
    """
    Persian text cleaner with additional features on Parsivar package.
    """

    def __init__(self):
        self.parsivar_normalizer = parsivar.Normalizer(statistical_space_correction=True)
        self.char_mappings = {
            "А": "a",
            "В": "b",
            "Е": "e",
            "Н": "h",
            "Р": "P",
            "С": "C",
            "Т": "T",
            "а": "a",
            "г": "r",
            "е": "e",
            "к": "k",
            "м": "m",
            "о": "o",
            "р": "p",
            "ڈ": "د",
            "ڇ": "چ",
            # Persian numbers (will be replaced by english one)
            "۰": "0",
            "۱": "1",
            "۲": "2",
            "۳": "3",
            "۴": "4",
            "۵": "5",
            "۶": "6",
            "۷": "7",
            "۸": "8",
            "۹": "9",
            ".": ".",
            # Arabic numbers (will be replaced by english one)
            "٠": "0",
            "١": "1",
            "٢": "2",
            "٣": "3",
            "٤": "4",
            "٥": "5",
            "٦": "6",
            "٧": "7",
            "٨": "8",
            "٩": "9",
            # Special Arabic Characters (will be replaced by persian one)
            "ك": "ک",
            "ى": "ی",
            "ي": "ی",
            "ؤ": "و",
            "ئ": "ی",
            "إ": "ا",
            "أ": "ا",
            "آ": "ا",
            "ة": "ه",
            "ء": "ی",
            # French alphabet (will be replaced by english one)
            "à": "a",
            "ä": "a",
            "ç": "c",
            "é": "e",
            "è": "e",
            "ê": "e",
            "ë": "e",
            "î": "i",
            "ï": "i",
            "ô": "o",
            "ù": "u",
            "û": "u",
            "ü": "u",
            # Comma (will be replaced by dots for floating point numbers)
            ",": ".",
            # And (will be replaced by dots for floating point numbers)
            "&": " and ",
            # Vowels (will be removed)
            "ّ": "",  # tashdid
            "َ": "",  # a
            "ِ": "",  # e
            "ُ": "",  # o
            "ـ": "",  # tatvil
            # Spaces
            "‍": "",  # 0x9E -> ZERO WIDTH JOINER
            "‌": " ",  # 0x9D -> ZERO WIDTH NON-JOINER
            # Arabic Presentation Forms-A (will be replaced by persian one)
            "ﭐ": "ا",
            "ﭑ": "ا",
            "ﭖ": "پ",
            "ﭗ": "پ",
            "ﭘ": "پ",
            "ﭙ": "پ",
            "ﭞ": "ت",
            "ﭟ": "ت",
            "ﭠ": "ت",
            "ﭡ": "ت",
            "ﭺ": "چ",
            "ﭻ": "چ",
            "ﭼ": "چ",
            "ﭽ": "چ",
            "ﮊ": "ژ",
            "ﮋ": "ژ",
            "ﮎ": "ک",
            "ﮏ": "ک",
            "ﮐ": "ک",
            "ﮑ": "ک",
            "ﮒ": "گ",
            "ﮓ": "گ",
            "ﮔ": "گ",
            "ﮕ": "گ",
            "ﮤ": "ه",
            "ﮥ": "ه",
            "ﮦ": "ه",
            "ﮪ": "ه",
            "ﮫ": "ه",
            "ﮬ": "ه",
            "ﮭ": "ه",
            "ﮮ": "ی",
            "ﮯ": "ی",
            "ﮰ": "ی",
            "ﮱ": "ی",
            "ﯼ": "ی",
            "ﯽ": "ی",
            "ﯾ": "ی",
            "ﯿ": "ی",
            # Arabic Presentation Forms-B (will be removed)
            "ﹰ": "",
            "ﹱ": "",
            "ﹲ": "",
            "ﹳ": "",
            "ﹴ": "",
            "﹵": "",
            "ﹶ": "",
            "ﹷ": "",
            "ﹸ": "",
            "ﹹ": "",
            "ﹺ": "",
            "ﹻ": "",
            "ﹼ": "",
            "ﹽ": "",
            "ﹾ": "",
            "ﹿ": "",
            # Arabic Presentation Forms-B (will be replaced by persian one)
            "ﺀ": "ی",
            "ﺁ": "ا",
            "ﺂ": "ا",
            "ﺃ": "ا",
            "ﺄ": "ا",
            "ﺅ": "و",
            "ﺆ": "و",
            "ﺇ": "ا",
            "ﺈ": "ا",
            "ﺉ": "ی",
            "ﺊ": "ی",
            "ﺋ": "ی",
            "ﺌ": "ی",
            "ﺍ": "ا",
            "ﺎ": "ا",
            "ﺏ": "ب",
            "ﺐ": "ب",
            "ﺑ": "ب",
            "ﺒ": "ب",
            "ﺓ": "ه",
            "ﺔ": "ه",
            "ﺕ": "ت",
            "ﺖ": "ت",
            "ﺗ": "ت",
            "ﺘ": "ت",
            "ﺙ": "ث",
            "ﺚ": "ث",
            "ﺛ": "ث",
            "ﺜ": "ث",
            "ﺝ": "ج",
            "ﺞ": "ج",
            "ﺟ": "ج",
            "ﺠ": "ج",
            "ﺡ": "ح",
            "ﺢ": "ح",
            "ﺣ": "ح",
            "ﺤ": "ح",
            "ﺥ": "خ",
            "ﺦ": "خ",
            "ﺧ": "خ",
            "ﺨ": "خ",
            "ﺩ": "د",
            "ﺪ": "د",
            "ﺫ": "ذ",
            "ﺬ": "ذ",
            "ﺭ": "ر",
            "ﺮ": "ر",
            "ﺯ": "ز",
            "ﺰ": "ز",
            "ﺱ": "س",
            "ﺲ": "س",
            "ﺳ": "س",
            "ﺴ": "س",
            "ﺵ": "ش",
            "ﺶ": "ش",
            "ﺷ": "ش",
            "ﺸ": "ش",
            "ﺹ": "ص",
            "ﺺ": "ص",
            "ﺻ": "ص",
            "ﺼ": "ص",
            "ﺽ": "ض",
            "ﺾ": "ض",
            "ﺿ": "ض",
            "ﻀ": "ض",
            "ﻁ": "ط",
            "ﻂ": "ط",
            "ﻃ": "ط",
            "ﻄ": "ط",
            "ﻅ": "ظ",
            "ﻆ": "ظ",
            "ﻇ": "ظ",
            "ﻈ": "ظ",
            "ﻉ": "ع",
            "ﻊ": "ع",
            "ﻋ": "ع",
            "ﻌ": "ع",
            "ﻍ": "غ",
            "ﻎ": "غ",
            "ﻏ": "غ",
            "ﻐ": "غ",
            "ﻑ": "ف",
            "ﻒ": "ف",
            "ﻓ": "ف",
            "ﻔ": "ف",
            "ﻕ": "ق",
            "ﻖ": "ق",
            "ﻗ": "ق",
            "ﻘ": "ق",
            "ﻙ": "ک",
            "ﻚ": "ک",
            "ﻛ": "ک",
            "ﻜ": "ک",
            "ﻝ": "ل",
            "ﻞ": "ل",
            "ﻟ": "ل",
            "ﻠ": "ل",
            "ﻡ": "م",
            "ﻢ": "م",
            "ﻣ": "م",
            "ﻤ": "م",
            "ﻥ": "ن",
            "ﻦ": "ن",
            "ﻧ": "ن",
            "ﻨ": "ن",
            "ﻩ": "ه",
            "ﻪ": "ه",
            "ﻫ": "ه",
            "ﻬ": "ه",
            "ﻭ": "و",
            "ﻮ": "و",
            "ﻯ": "ی",
            "ﻰ": "ی",
            "ﻱ": "ی",
            "ﻲ": "ی",
            "ﻳ": "ی",
            "ﻴ": "ی",
            "ﻵ": "لا",
            "ﻶ": "لا",
            "ﻷ": "لا",
            "ﻸ": "لا",
            "ﻹ": "لا",
            "ﻺ": "لا",
            "ﻻ": "لا",
            "ﻼ": "لا",
        }

        self.valid_chars = [
            " ",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "آ",
            "ئ",
            "ا",
            "ب",
            "ت",
            "ث",
            "ج",
            "ح",
            "خ",
            "د",
            "ذ",
            "ر",
            "ز",
            "س",
            "ش",
            "ص",
            "ض",
            "ط",
            "ظ",
            "ع",
            "غ",
            "ف",
            "ق",
            "ل",
            "م",
            "ن",
            "ه",
            "و",
            "پ",
            "چ",
            "ژ",
            "ک",
            "گ",
            "ی",
        ]

    @staticmethod
    def _replace_rep(t):
        """Replace repetitions at the character level: ccc -> c"""

        def __replace_rep(m):
            c, cc = m.groups()
            return f"{c}"

        re_rep = re.compile(r"(\S)(\1{2,})")
        return re_rep.sub(__replace_rep, t)

    @staticmethod
    def _replace_wrap(t):
        """Replace word repetitions: word word word -> word"""

        def __replace_wrap(m):
            c, cc = m.groups()
            return f"{c}"

        re_wrap = re.compile(r"(\b\w+\W+)(\1{2,})")
        return re_wrap.sub(__replace_wrap, t)

    def _normalize_text(self, x):
        """normalize a sentence"""

        x = str(x)
        x = self.parsivar_normalizer.normalize(x)  # apply `parsivar` normalizations
        x = re.sub(r"[\u200c\r\n]", " ", x)  # remove half space and new line characters
        x = x.lower()
        x = "".join(
            [self.char_mappings[xx] if xx in self.char_mappings else xx for xx in x]
        )  # substitute bad characters with appropriate ones
        x = re.sub(
            r"[^{}]".format("".join(self.valid_chars)), " ", x
        )  # just keep valid characters and substitute others with space
        x = re.sub(r"[a-z]+", r" \g<0> ", x)  # put space around words and numbers
        x = re.sub(r"[0-9]+", r" \g<0> ", x)  # put space around words and numbers
        x = re.sub(r"\s+", " ", x)  # remove more than one white spaces with space
        x = self._replace_rep(x)
        x = self._replace_wrap(x)
        return x.strip()

    def normalize_texts(self, text, use_tqdm=False):
        """normalize list of sentences"""

        if use_tqdm:
            text = [self._normalize_text(x) for x in tqdm(text)]
        else:
            text = [self._normalize_text(x) for x in text]
        return text
