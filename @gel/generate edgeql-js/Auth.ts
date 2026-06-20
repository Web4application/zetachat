// Fetching a user and their posts automatically mapped to nested JSON objects
const query = e.select(e.User, (user) => ({
  id: true,
  username: true,
  posts: e.select(user.posts, (post) => ({
    title: true,
    content: true
  }))
}));

const usersWithPosts = await query.run(client);
