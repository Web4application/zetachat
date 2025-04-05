import React, { useState, useEffect } from 'react';

function App() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState('all');

  // Load saved todos from localStorage
  useEffect(() => {
    const savedTodos = JSON.parse(localStorage.getItem('todos')) || [];
    setTodos(savedTodos);
  }, []);

  // Save todos to localStorage whenever they change
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  // Add a new todo
  const addTodo = () => {
    if (input.trim()) {
      setTodos([...todos, { id: Date.now(), text: input, completed: false, deadline: '' }]);
      setInput('');
    }
  };

  // Toggle completion status
  const toggleComplete = (id) => {
    setTodos(todos.map(todo => (
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    )));
  };

  // Delete a todo
  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  // Filter todos based on user selection
  const filteredTodos = todos.filter(todo =>
    filter === 'completed' ? todo.completed :
    filter === 'pending' ? !todo.completed :
    true
  );

  // Sort todos by deadline (if added in the future)
  const sortedTodos = [...filteredTodos].sort((a, b) => {
    if (!a.deadline || !b.deadline) return 0;
    return new Date(a.deadline) - new Date(b.deadline);
  });

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
        {sortedTodos.map(todo => (
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
