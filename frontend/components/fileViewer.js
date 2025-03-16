const renderFilePreview = (fileUrl) => {
    const isImage = /\.(jpeg|jpg|png|gif)$/.test(fileUrl);
    if (isImage) {
        return <img src={fileUrl} alt="Preview" style={{ maxWidth: "200px" }} />;
    }

    const isPDF = /\.pdf$/.test(fileUrl);
    if (isPDF) {
        return <iframe src={fileUrl} title="PDF Preview" style={{ width: "100%", height: "400px" }} />;
    }

    return <a href={fileUrl} target="_blank" rel="noopener noreferrer">Download File</a>;
};
