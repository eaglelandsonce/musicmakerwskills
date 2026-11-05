"""Sample SongSmith defaults independently and uniformly."""
import json
import random

OPTIONS = {
    "genre": ["pop", "rock", "hip-hop", "jazz", "electronic", "folk"],
    "key": ["C major", "A minor", "G major", "E minor", "F major", "D minor"],
    "tempo": ["70bpm", "90bpm", "110bpm", "130bpm", "150bpm"],
    "structure": ["verse-chorus", "AAA", "ABABCB", "ABAB", "sonata"],
    "verses": [1, 2, 3, 4],
    "choruses": [1, 2, 3],
    "bridges": [0, 1, 2],
    "mood": ["happy", "sad", "nostalgic", "romantic", "energetic", "chill"],
    "instr": ["guitar", "piano", "synth", "strings", "drums", "bass"],
}


def sample():
    rng = random.SystemRandom()
    return {key: rng.choice(values) for key, values in OPTIONS.items()}


if __name__ == "__main__":
    print(json.dumps(sample()))
