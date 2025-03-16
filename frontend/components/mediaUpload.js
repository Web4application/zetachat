const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    const storageRef = supabase.storage.from("chat-media");
    const { data, error } = await storageRef.upload(`uploads/${file.name}`, file);

    if (error) {
        console.error("File upload error:", error);
    } else {
        console.log("Uploaded file URL:", data.path);
    }
};
