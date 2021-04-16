import { useState } from "react";
import Header from "./components/Header";
import Tasks from "./components/Tasks";
import AddTask from "./components/AddTask";

function App() {
  const [showAddTasks, setShowAddTasks] = useState(true);
  const [taskList, setTasks] = useState([
    {
      id: 1,
      text: "task1",
      day: "1",
      reminder: true,
    },
    {
      id: 2,
      text: "task2",
      day: "2",
      reminder: true,
    },
    {
      id: 3,
      text: "task3",
      day: "3",
      reminder: false,
    },
    {
      id: 4,
      text: "task4",
      day: "4",
      reminder: true,
    },
  ]);

  //delete tasks
  const deleteTask = (id) => {
    setTasks(taskList.filter((task) => task.id !== id));
  };

  //toggle reminder to true/false
  const toggleReminder = (id) => {
    setTasks(
      taskList.map((task) =>
        task.id === id ? { ...task, reminder: !task.reminder } : task
      )
    );
  };

  //AddTask function
  const addTask = (task) => {
    const id = Math.floor(Math.random() * 10000) + 1;
    const newTask = { id, ...task };
    setTasks([...taskList, newTask]);
  };

  return (
    <div className="container">
      <Header
        onAddButton={() => setShowAddTasks(!showAddTasks)}
        showAdd={showAddTasks}
      />
      {showAddTasks && <AddTask onAdd={addTask} />}
      {taskList.length > 0 ? (
        <Tasks
          taskList={taskList}
          onDelete={deleteTask}
          onToggle={toggleReminder}
        />
      ) : (
        "No Tasks"
      )}
    </div>
  );
}

export default App;
