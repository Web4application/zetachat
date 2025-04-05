const mongoose = require('mongoose');

const TodoSchema = new mongoose.Schema({
  text: { type: String, required: true },
  completed: { type: Boolean, default: false },
  deadline: { type: Date, required: false }
});

module.exports = mongoose.model('Todo', TodoSchema);
