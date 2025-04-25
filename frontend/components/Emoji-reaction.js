import React, { useState } from 'react';

function EmojiReactions() {
    const [reactions, setReactions] = useState([]);
    const emojis = ['👍', '❤️', '😂', '😲'];

    const addReaction = (emoji) => {
        setReactions((prev) => [...prev, emoji]);
    };

    return (
        <div>
            <div>
                {reactions.map((emoji, index) => (
                    <span key={index}>{emoji}</span>
                ))}
            </div>
            <div>
                {emojis.map((emoji) => (
                    <button key={emoji} onClick={() => addReaction(emoji)}>
                        {emoji}
                    </button>
                ))}
            </div>
        </div>
    );
}

export default EmojiReactions;
