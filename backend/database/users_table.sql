CREATE TABLE users (
    id SERIAL PRIMARY KEY,              -- Unique user ID
    username VARCHAR(255) NOT NULL,    -- User's name or identifier
    email VARCHAR(255) UNIQUE NOT NULL,-- User's email (optional)
    trial_end TIMESTAMP,               -- Trial expiration date
    is_subscribed BOOLEAN DEFAULT FALSE, -- Whether the user is subscribed
    subscription_plan VARCHAR(50),    -- "monthly" or "yearly"
    payment_confirmed BOOLEAN DEFAULT FALSE -- Payment confirmation status
);
