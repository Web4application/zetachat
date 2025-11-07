let currentUserId = null;

// Sign-Up
document.getElementById('signup-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  const res = await fetch('/signup', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  const data = await res.json();
  if(data.userId){
    currentUserId = data.userId;
    document.getElementById('signup-page').style.display = 'none';
    document.getElementById('profile-page').style.display = 'block';
  } else alert('Error: ' + data.error);
});

// Profile
document.getElementById('profile-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const profile = {
    userId: currentUserId,
    fullname: document.getElementById('fullname').value,
    age: document.getElementById('age').value,
    gender: document.getElementById('gender').value,
    address: document.getElementById('address').value,
    country: document.getElementById('country').value,
    occupation: document.getElementById('occupation').value,
    status: document.getElementById('status').value
  };

  const res = await fetch('/profile', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(profile)
  });
  const data = await res.json();
  if(data.profileId){
    document.getElementById('profile-page').style.display = 'none';
    document.getElementById('social-media-page').style.display = 'block';
  } else alert('Error: ' + data.error);
});

// Social Media
document.getElementById('social-media-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const platforms = [];
  document.querySelectorAll('input[name="social-media"]:checked').forEach(cb => platforms.push(cb.value));
  const res = await fetch('/social', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ userId: currentUserId, platforms })
  });
  const data = await res.json();
  if(data.success) alert('All done! Social media synced.');
});
