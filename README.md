# studenttaskmanager

Python console application for managing student tasks using Git and GitHub.

## Development

The application supports adding, displaying, completing, and deleting tasks.
Each feature was developed and reviewed through a separate feature branch.
## Features
- Add tasks with unique IDs.
- Reject empty and whitespace-only titles.
- Display tasks with Pending or Completed status.
- Complete a task using its ID.
- Delete a task using its ID.
- Report invalid task IDs.

## Requirements
- Python 3
- Git for cloning the repository
- No external Python packages are required.

## Setup
```bash
git clone https://github.com/kinzasafdar01/studenttaskmanager.git
cd studenttaskmanager
```

## Usage
```bash
python task_manager.py
```

Choose a menu option:
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit

Use the ID shown when displaying tasks to complete or delete a task.
Tasks are stored in memory and are cleared when the program closes.

## Tests
Run from the repository root:

```bash
python -m unittest discover -s tests -v
```

Tests cover adding tasks, rejecting empty titles, completing tasks,
and deleting tasks. Completion and deletion tests also check missing IDs.

GitHub Actions runs tests on pushes to main and Pull Requests targeting main.

## Branching
The feature/addtask, feature/completetask, and feature/deletetask
branches each contain separate implementation and testing commits.
Branches isolate work so changes can be reviewed before merging.

## Merge Conflict Exercise
Two branches changed the same project status line from Planning
to Development and Testing. Git reported a conflict when the second
branch was merged. The conflict was resolved by combining the statuses
and keeping all unrelated README content.

## User Guide
See [docs/userguide.md](docs/userguide.md).

## License
MIT License. See LICENSE.