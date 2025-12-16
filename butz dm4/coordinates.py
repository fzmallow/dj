# Task 2.1: Coordinate System with Tuples
import math
import string
from collections import Counter
from typing import Tuple


Point = Tuple[float, float]


def calculate_distance(point1: Point, point2: Point) -> float:
    """Calculate the distance between two 2D points."""
    return math.dist(point1, point2)


def find_midpoint(point1: Point, point2: Point) -> Point:
    """Find the midpoint between two 2D points."""
    return ((point1[0] + point2[0]) / 2,
            (point1[1] + point2[1]) / 2)


def display_points(points: Tuple[Point, ...]) -> None:
    """Display a list of points."""
    for idx, point in enumerate(points, start=1):
        print(f"Point {idx}: {point}")


# Task 2.2: Unique Word Counter with Sets
def count_unique_words(text: str) -> None:
    """Analyze and display word statistics from text."""
    
    # Clean and normalize text
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.lower().translate(translator)
    words = cleaned_text.split()

    unique_words = set(words)
    word_freq = Counter(words)

    print("\n" + "=" * 40)
    print("TASK 2.2: Unique Word Counter")
    print("=" * 40)

    print(f"Original text:\n{text}")
    print(f"\nTotal words: {len(words)}")
    print(f"Unique words: {len(unique_words)}")

    print("\nUnique words (sorted):")
    print(sorted(unique_words))

    most_common_word, count = word_freq.most_common(1)[0]
    print(f"\nMost common word: '{most_common_word}' ({count} times)")

    print("\nWord frequencies:")
    for word, freq in word_freq.most_common():
        print(f"  {word}: {freq}")


def demonstrate_tuple_immutability(point: Point) -> None:
    """Show that tuples cannot be modified."""
    print("\n" + "=" * 40)
    print("Demonstrating Tuple Immutability")
    print("=" * 40)
    print(f"Original point: {point}")

    try:
        point[0] = 10
    except TypeError as e:
        print(f"Error: {e}")
        print("✔ Tuples are immutable and cannot be changed.")


# Main Program
if __name__ == "__main__":
    print("=" * 40)
    print("TASK 2.1: Coordinate System")
    print("=" * 40)

    point1 = (2, 3)
    point2 = (5, 7)
    point3 = (1, 1)

    all_points = (point1, point2, point3)
    display_points(all_points)

    distance = calculate_distance(point1, point2)
    midpoint = find_midpoint(point1, point2)

    print(f"\nDistance between {point1} and {point2}: {distance:.2f}")
    print(f"Midpoint between {point1} and {point2}: {midpoint}")

    demonstrate_tuple_immutability(point1)

    sample_text = (
        "Python is a programming language. "
        "Python is easy to learn. "
        "Python is powerful."
    )
    count_unique_words(sample_text)
