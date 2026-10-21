'''
Problem 2: Top Artists
Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity.


Example Usage:

print_linked_list(top_hits_2010s)
Example Output:

Uptown Funk -> Party Rock Anthem -> Bad Romance

UPI Plan

UNDERSTAND:
Input -
Output -
Edge Cases -

PLAN:

IMPLEMENT:
'''



class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    current = playlist
    frequency = {}
    while current:
        if current.artist in frequency:
            frequency[current.artist] += 1
        else:
            frequency[current.artist] = 1
        current = current.next
    return frequency


if __name__ == "__main__":
    playlist = SongNode(
        "Saturn",
        "SZA",
        SongNode(
            "Who",
            "Jimin",
            SongNode("Espresso", "Sabrina Carpenter", SongNode("Snooze", "SZA")),
        ),
    )
    print(get_artist_frequency(playlist))