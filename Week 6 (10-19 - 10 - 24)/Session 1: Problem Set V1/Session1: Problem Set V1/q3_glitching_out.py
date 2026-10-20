'''
Problem 3: Glitching Out
The starter function below is meant to remove the first node with the
requested song. Find and fix its bug, then evaluate its complexity.

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


def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next
    current = playlist_head
    while current.next:
        if current.next.song == song:
            current = current.next.next
            return playlist_head
        current = current.next
    return playlist_head
