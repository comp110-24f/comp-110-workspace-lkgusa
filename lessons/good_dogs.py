"""Recursion practice over a list."""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    num_dogs: int = len(scores)
    if num_dogs <= idx:
        raise IndexError("idx too high")
    # Base case 1: First dog's score is below threshold
    elif int(scores[idx]["score"]) < thresh:
        return False
    # Base case 2: final dog's score is above threshold
    else:
        if num_dogs == idx + 1:
            return True
        # Recursive case
        else:
            print(f"Good dog, {scores[idx]["name"]}")
            return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]

print(all_good(scores=pack, thresh=8, idx=0))
print(all_good(scores=pack, thresh=7, idx=0))
