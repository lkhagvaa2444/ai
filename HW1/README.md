Sure, here is a README.md file that documents the course scheduling system, describes the testing process, and provides sample output.

```markdown
# Course Scheduling System

## Overview

This project implements a simple course scheduling system using a hill-climbing algorithm. The system schedules courses for teachers in two classrooms, attempting to minimize conflicts where a teacher is double-booked.

## Course Information

### Courses

| Teacher | Name | Hours |
| ------- | ---- | ----- |
|         |      | -1    |
| 甲      | 機率  | 2     |
| 甲      | 線代  | 3     |
| 甲      | 離散  | 3     |
| 乙      | 視窗  | 3     |
| 乙      | 科學  | 3     |
| 乙      | 系統  | 3     |
| 乙      | 計概  | 3     |
| 丙      | 軟工  | 3     |
| 丙      | 行動  | 3     |
| 丙      | 網路  | 3     |
| 丁      | 媒體  | 3     |
| 丁      | 工數  | 3     |
| 丁      | 動畫  | 3     |
| 丁      | 電子  | 4     |
| 丁      | 嵌入  | 3     |
| 戊      | 網站  | 3     |
| 戊      | 網頁  | 3     |
| 戊      | 演算  | 3     |
| 戊      | 結構  | 3     |
| 戊      | 智慧  | 3     |

### Teachers

- 甲
- 乙
- 丙
- 丁
- 戊

### Rooms

- A
- B

### Slots

```
A11, A12, A13, A14, A15, A16, A17,
A21, A22, A23, A24, A25, A26, A27,
A31, A32, A33, A34, A35, A36, A37,
A41, A42, A43, A44, A45, A46, A47,
A51, A52, A53, A54, A55, A56, A57,
B11, B12, B13, B14, B15, B16, B17,
B21, B22, B23, B24, B25, B26, B27,
B31, B32, B33, B34, B35, B36, B37,
B41, B42, B43, B44, B45, B46, B47,
B51, B52, B53, B54, B55, B56, B57,
```

## Testing

### Steps to Test

1. **Initialize the Schedule:**
    - Ensure the initial random schedule is created correctly.
    - Print the initial schedule.

2. **Calculate Initial Conflicts:**
    - Verify the conflict calculation.
    - Print the number of initial conflicts.

3. **Generate Neighbors:**
    - Confirm neighbors are generated correctly.
    - Print a few neighbor schedules.

4. **Hill Climbing Optimization:**
    - Ensure the algorithm improves the schedule by reducing conflicts.
    - Print the final schedule and the number of conflicts.

### Sample Output

The output will include the initial conflicts, progress through each iteration, and the final optimized schedule. Below is an example of what the output might look like:

```
Initial conflicts: 10

Iteration 1: Conflicts: 8
Iteration 2: Conflicts: 6
Iteration 3: Conflicts: 5
Iteration 4: Conflicts: 3
Iteration 5: Conflicts: 1

Final Schedule:
Slot: A11, Course: 動畫, Teacher: 丁, Hours: 3
Slot: A12, Course: 動畫, Teacher: 丁, Hours: 3
Slot: A13, Course: 離散, Teacher: 甲, Hours: 3
Slot: A14, Course: 動畫, Teacher: 丁, Hours: 3
Slot: A15, Course: 系統, Teacher: 乙, Hours: 3
...
```

## Code

```python
import random

# Course Information
courses = [
    {'teacher': ' ', 'name':' ', 'hours': -1},  # No class in this slot
    {'teacher': '甲', 'name':'機率', 'hours': 2},
    {'teacher': '甲', 'name':'線代', 'hours': 3},
    {'teacher': '甲', 'name':'離散', 'hours': 3},
    {'teacher': '乙', 'name':'視窗', 'hours': 3},
    {'teacher': '乙', 'name':'科學', 'hours': 3},
    {'teacher': '乙', 'name':'系統', 'hours': 3},
    {'teacher': '乙', 'name':'計概', 'hours': 3},
    {'teacher': '丙', 'name':'軟工', 'hours': 3},
    {'teacher': '丙', 'name':'行動', 'hours': 3},
    {'teacher': '丙', 'name':'網路', 'hours': 3},
    {'teacher': '丁', 'name':'媒體', 'hours': 3},
    {'teacher': '丁', 'name':'工數', 'hours': 3},
    {'teacher': '丁', 'name':'動畫', 'hours': 3},
    {'teacher': '丁', 'name':'電子', 'hours': 4},
    {'teacher': '丁', 'name':'嵌入', 'hours': 3},
    {'teacher': '戊', 'name':'網站', 'hours': 3},
    {'teacher': '戊', 'name':'網頁', 'hours': 3},
    {'teacher': '戊', 'name':'演算', 'hours': 3},
    {'teacher': '戊', 'name':'結構', 'hours': 3},
    {'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']
rooms = ['A', 'B']
slots = [
    'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
    'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
    'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
    'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
    'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
    'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
    'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
    'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
    'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
    'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

class Schedule:
    def __init__(self, courses, slots):
        self.courses = courses
        self.slots = slots
        self.schedule = {slot: None for slot in slots}

    def initialize_random(self):
        for slot in self.slots:
            course = random.choice(self.courses)
            self.schedule[slot] = course

    def calculate_conflicts(self):
        conflicts = 0
        teacher_slots = {teacher: [] for teacher in teachers}
        for slot, course in self.schedule.items():
            if course['teacher'] != ' ':
                teacher_slots[course['teacher']].append(slot)

        for teacher, slots in teacher_slots.items():
            times = [int(slot[1:]) for slot in slots]
            if len(times) > len(set(times)):
                conflicts += 1

        return conflicts

    def get_neighbors(self):
        neighbors = []
        for slot in self.slots:
            for course in self.courses:
                if self.schedule[slot] != course:
                    neighbor = Schedule(self.courses, self.slots)
                    neighbor.schedule = self.schedule.copy()
                    neighbor.schedule[slot] = course
                    neighbors.append(neighbor)
        return neighbors

def hill_climb(schedule):
    current_schedule = schedule
    current_schedule.initialize_random()
    current_conflicts = current_schedule.calculate_conflicts()
    print(f"Initial conflicts: {current_conflicts}")

    iteration = 0
    while True:
        neighbors = current_schedule.get_neighbors()
        best_neighbor = min(neighbors, key=lambda x: x.calculate_conflicts())
        best_neighbor_conflicts = best_neighbor.calculate_conflicts()

        if best_neighbor_conflicts >= current_conflicts:
            break

        current_schedule = best_neighbor
        current_conflicts = best_neighbor_conflicts
        iteration += 1
        print(f"Iteration {iteration}: Conflicts: {current_conflicts}")

    return current_schedule

# Create an initial schedule
initial_schedule = Schedule(courses, slots)
optimal_schedule = hill_climb(initial_schedule)

# Print the optimal schedule
print("\nFinal Schedule:")
for slot, course in optimal_schedule.schedule.items():
    print(f"Slot: {slot}, Course: {course['name']}, Teacher: {course['teacher']}, Hours: {course['hours']}")
