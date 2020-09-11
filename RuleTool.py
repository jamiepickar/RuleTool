import argparse
from pathlib import Path


# Modular Functions
def extract_weight(prefix: str) -> float:
    if (prefix.find("<") > -1) and (prefix.find(">") > -1):
        weight_start = prefix.find("<") + 1
        weight_end = prefix.find(">")
        weight = prefix[weight_start:weight_end]
    else:
        weight = 1.0
    try:
        weight = float(weight)
    except ValueError:
        weight = 1.0
    return weight


# Procedural Functions
def read_file(file: str) -> str:
    if not (file and Path(file).is_file()):
        print("Invalid Path")
        exit(1)
    file_text = Path(file).read_text()
    return file_text


def enumerate_rules(file_text: str):
    rules = []
    while file_text.find("(0:") > -1:
        rule_start = file_text.find("(0:")
        rule_end = file_text.find(";}") + 2
        rule = file_text[rule_start:rule_end]
        rule_prefix = file_text[(rule_start - 10):rule_start]
        weight = extract_weight(rule_prefix)
        rules.append({
            "text": rule,
            "weight": weight
        })
        file_text = file_text[rule_end:]
    return rules


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("input", metavar="input_file_path", type=str, help="Path of input rule set file for "
                                                                           "examination.")
    args = parser.parse_args()
    txt = read_file(args.input)
    all_rules = enumerate_rules(txt)
