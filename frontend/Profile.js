import React, { useState } from 'react';

function Profile() {
    const [profileImage, setProfileImage] = useState(null);

    const handleProfileImageChange = (e) => {
        setProfileImage(URL.createObjectURL(e.target.files[0]));
    };

    const handleProfileImageUpload = () => {
        const formData = new FormData();
        formData.append('profileImage', profileImage);

        fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => alert('Profile image uploaded successfully'))
        .catch(err => alert('Upload failed'));
    };

    return (
        <div>
            <h2>Upload Profile Picture</h2>
            <input type="file" onChange={handleProfileImageChange} />
            <button onClick={handleProfileImageUpload}>Upload</button>
            {profileImage && <img src={profileImage} alt="Profile" />}
        </div>
    );
}

export default Profile;
