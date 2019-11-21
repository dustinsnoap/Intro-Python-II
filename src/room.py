# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, cords, description=None):
        self.name = name
        self.cords = cords
        self.items = []
        self.description = description
    def __repr__(self):
        description = {"name": self.name, "cords": self.cords, "description": self.description}
        return f'{description}'
    def __getattr__(self, attr):
        print(f"{self.name}.{attr} isn't available.")

def update_room(room_cords, attr_name, attr_value):
    room = [r for r in rooms if r.cords == room_cords][0]
    setattr(room, attr_name, attr_value)
def get_room(room_cords):
    return [r for r in rooms if r.cords == [0,0,0]][0]

rooms = []
rooms.append(Room('r000', [0,-1,0]))
update_room([0,-1,0], 'description', f"You're in a hole; next to you are some planks. The only way out is up.")
rooms.append(Room('r000', [0,0,0]))
update_room([0,0,0], 'description', f"You're in a field standing next to a hole.")
rooms.append(Room('r100', [1,0,0]))
update_room([1,0,0], 'description', f"You come to a clearing; in front of you is an old bridge that is missing boards. The rope also seems loose.")

print(rooms)