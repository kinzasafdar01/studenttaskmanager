\# Student Task Manager User Guide



\## Start the application

Open a terminal in the studenttaskmanager folder and run:



```bash

python task\_manager.py

```



\## Add a task

Choose 1 and enter a title.

The application shows the new task ID.

Empty titles and titles containing only spaces are rejected.



\## Display tasks

Choose 2.

Each task shows its ID, title, and Pending or Completed status.

If the list is empty, the application displays a message.



\## Complete a task

Choose 3 and enter an existing task ID.

The selected task is marked as Completed.



\## Delete a task

Choose 4 and enter an existing task ID.

Only the selected task is removed.



\## Invalid input

Unknown task IDs produce an error message.

Task IDs must be whole numbers.

Invalid menu choices display a message.



\## Exit

Choose 5.

Tasks are stored only for the current session and are cleared on exit.

