import { GoogleAuthProvider, signInWithPopup } from 'firebase/auth';

const provider = new GoogleAuthProvider();

const googleLogin = async () => {
    try {
        const result = await signInWithPopup(auth, provider);
        console.log('User logged in:', result.user);
    } catch (error) {
        console.error('Error during login:', error);
    }
};
