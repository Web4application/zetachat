app.post("/upload", async (req, res) => {
    const { file } = req.body; // Receive the file
    const { data, error } = await supabase.storage
        .from("chat-media")
        .upload(`uploads/${file.name}`, file);

    if (error) {
        res.status(500).json({ error: error.message });
    } else {
        res.status(200).json({ path: data.path });
    }
});
