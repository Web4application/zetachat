import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState('all');

  // Load todos from the backend
  useEffect(() => {
    const fetchTodos = async () => {
      const response = await axios.get('http://localhost:5000/api/todos');
      setTodos(response.data);
    };
    fetchTodos();
  }, []);

  // Add a new todo
  const addTodo = async () => {
    if (input.trim()) {
      const newTodo = { text: input, completed: false };
      const response = await axios.post('http://localhost:5000/api/todos', newTodo);
      setTodos([...todos, response.data]);
      setInput('');
    }
  };

  // Toggle completion status
  const toggleComplete = async (id) => {
    const todo = todos.find(todo => todo.id === id);
    const updatedTodo = { ...todo, completed: !todo.completed };
    await axios.put(`http://localhost:5000/api/todos/${id}`, updatedTodo);
    setTodos(todos.map(todo => (todo.id === id ? updatedTodo : todo)));
  };

  // Delete a todo
  const deleteTodo = async (id) => {
    await axios.delete(`http://localhost:5000/api/todos/${id}`);
    setTodos(todos.filter(todo => todo.id !== id));
  };

  // Filter todos
  const filteredTodos = todos.filter(todo =>
    filter === 'completed' ? todo.completed :
    filter === 'pending' ? !todo.completed :
    true
  );

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Enhanced To-Do List</h1>

      {/* Input for adding new todos */}
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Add a task..."
        style={{ marginRight: '10px' }}
      />
      <button onClick={addTodo} style={{ padding: '5px 10px', background: 'blue', color: 'white', border: 'none' }}>
        Add Task
      </button>

      {/* Filter options */}
      <div style={{ marginTop: '20px' }}>
        <button onClick={() => setFilter('all')} style={{ marginRight: '5px' }}>All</button>
        <button onClick={() => setFilter('completed')} style={{ marginRight: '5px' }}>Completed</button>
        <button onClick={() => setFilter('pending')}>Pending</button>
      </div>

      {/* Todo list */}
      <ul style={{ listStyleType: 'none', padding: '0', marginTop: '20px' }}>
        {filteredTodos.map(todo => (
          <li key={todo.id} style={{ marginBottom: '10px' }}>
            <span style={{
              textDecoration: todo.completed ? 'line-through' : 'none',
              marginRight: '10px'
            }}>
              {todo.text}
            </span>
            <button onClick={() => toggleComplete(todo.id)} style={{ marginRight: '5px' }}>✓</button>
            <button onClick={() => deleteTodo(todo.id)} style={{ color: 'red' }}>🗑️</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
