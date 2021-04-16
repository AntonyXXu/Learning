//import { useState } from "react";
import IndividualTask from "./IndividualTask";
const Tasks = ({ taskList, onDelete, onToggle }) => {
  return (
    <>
      {taskList.map((task) => (
        <IndividualTask
          key={task.id}
          task={task}
          onDelete={() => onDelete(task.id)}
          onToggle={onToggle}
        />
      ))}
    </>
  );
};

export default Tasks;
