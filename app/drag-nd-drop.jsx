import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";

const onDragEnd = (result) => {
  if (!result.destination) return;
  const reorderedTodos = Array.from(todos);
  const [movedItem] = reorderedTodos.splice(result.source.index, 1);
  reorderedTodos.splice(result.destination.index, 0, movedItem);
  setTodos(reorderedTodos);
};

<DragDropContext onDragEnd={onDragEnd}>
  <Droppable droppableId="todos">
    {(provided) => (
      <ul
        {...provided.droppableProps}
        ref={provided.innerRef}
        className="mt-4 w-full max-w-md"
      >
        {todos.map((todo, index) => (
          <Draggable key={todo.id} draggableId={`${todo.id}`} index={index}>
            {(provided) => (
              <li
                ref={provided.innerRef}
                {...provided.draggableProps}
                {...provided.dragHandleProps}
                className={`flex justify-between items-center p-2 border-b ${
                  todo.completed ? "line-through text-gray-500" : ""
                }`}
              >
                {todo.text}
                <div>
                  <button
                    onClick={() => toggleComplete(todo.id)}
                    className="mr-2 text-green-500"
                  >
                    ✓
                  </button>
                  <button
                    onClick={() => deleteTodo(todo.id)}
                    className="text-red-500"
                  >
                    🗑️
                  </button>
                </div>
              </li>
            )}
          </Draggable>
        ))}
        {provided.placeholder}
      </ul>
    )}
  </Droppable>
</DragDropContext>
