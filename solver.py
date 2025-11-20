import re

def load_puzzles(filename="data/puzzles.txt"):
    with open(filename, "r") as f:
        return [line.strip().upper() for line in f.readlines()]

def pattern_to_regex(pattern):
    """
    Convert a pattern like '_ _ E _   T _ _' 
    into a regex like '^..E. T..$'
    """
    return "^" + "".join("." if c == "_" else c for c in pattern.replace(" ", "")) + "$"

def solve_pattern(pattern, puzzles):
    regex = re.compile(pattern_to_regex(pattern))
    candidates = [p for p in puzzles if regex.match(p.replace(" ", ""))]
    return candidates


if __name__ == "__main__":
    puzzles = load_puzzles()

    pattern = "_ _ _ _   _ E _"  # example pattern
    candidates = solve_pattern(pattern, puzzles)

    print("Candidates:")
    for c in candidates:
        print(" -", c)
