from collections import Counter


def solution1(A):
  """Your solution goes here."""
  if len(A) < 3 or not A:
    return ""
  bookedRooms = Counter()
  retRoom = []
  maxBooking = 0
  for room in A:
    if room[0] == '+':
      bookedRooms[room[1:]] += 1
      if bookedRooms[room[1:]] > maxBooking:
        maxBooking = bookedRooms[room[1:]]
        retRoom = []
        retRoom.append(room[1:])
      elif bookedRooms[room[1:]] == maxBooking:
        retRoom.append(room[1:])

  return min(retRoom) if maxBooking > 0 else ""

def solution2(T):
  # Your solution goes here.
  T = list(T)
  if T[0] == "?":
    if T[1] == "?":
      T[0] = '2'
    elif int(T[1]) < 4:
      T[0] = '2'
    else:
      T[0] = '1'
  if T[1] == "?":
    if T[0] == "?":
      T[1] = '3'
    elif int(T[0]) == 2:
      T[1] = '3'
    else:
      T[1] = '9'
  if T[3] == "?":
    T[3] = '5'
  if T[4] == "?":
    T[4] = '9'
  return "".join(T)


input = ['+1Z','+2A','-1A','+9Z','+1A']
print(solution(input))