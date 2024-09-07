import argparse
import json
from pathlib import Path

def reduce_length(languages, max_items=6):
    if len(languages) > max_items:
        other_percentage = 100.0
        reduced = languages[0:max_items-1]
        for l in reduced:
            other_percentage -= sum((float(v) for v in l.values()))
        reduced.append({"Other": f"{other_percentage:g}"})
        return reduced

    return languages

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reduce languages list")
    parser.add_argument(
        "-in", type=str, required=True, help="Input path"
    )

    args = parser.parse_args()
    input_path = getattr(args, "in")

    with open(input_path) as f:
        data = json.load(f)
        for repo in data:
            languages = repo["languages"]
            repo["languages"] = reduce_length(languages)
    with open(Path(input_path).with_name("repositoriesnew.json"), "w") as f:
        json.dump(data, f)
