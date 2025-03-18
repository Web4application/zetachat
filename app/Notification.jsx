import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const addTodo = () => {
  if (input.trim()) {
    setTodos([...todos, { id: Date.now(), text: input, completed: false }]);
    setInput("");
    toast.success("Task added!");
  } else {
    toast.error("Please enter a task!");
  }
};

return (
  <div>
    <ToastContainer />
    {/* The rest of the code */}
  </div>
);
