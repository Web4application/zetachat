<div className="flex flex-col items-center p-4 bg-gray-100 min-h-screen">
  <h1 className="text-3xl font-bold mb-4 text-blue-600">To-Do List</h1>
  <div className="flex gap-2">
    <input
      type="text"
      value={input}
      onChange={(e) => setInput(e.target.value)}
      placeholder="Add a task..."
      className="border rounded-md p-2 flex-1"
    />
    <button onClick={addTodo} className="bg-blue-500 text-white px-4 py-2 rounded-md">
      Add
    </button>
    <button onClick={clearCompleted} className="bg-red-500 text-white px-4 py-2 rounded-md">
      Clear Completed
    </button>
  </div>
  <ul className="mt-4 w-full max-w-md">
    {todos.map((todo) => (
      <li
        key={todo.id}
        className={`flex justify-between items-center p-2 border-b ${
          todo.completed ? 'line-through text-gray-500' : ''
        }`}
      >
        {todo.text}
        <div>
          <button onClick={() => toggleComplete(todo.id)} className="mr-2 text-green-500">
            ✓
          </button>
          <button onClick={() => deleteTodo(todo.id)} className="text-red-500">
            🗑️
          </button>
        </div>
      </li>
    ))}
  </ul>
</div>
