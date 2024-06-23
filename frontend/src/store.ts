import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, updateProfile, GoogleAuthProvider, signInWithPopup, sendPasswordResetEmail, getAdditionalUserInfo, type User } from 'firebase/auth';
import { createStore } from 'vuex'
import { auth } from './firebaseAuth';
import { registerUserInDb } from './helpers';

const store = createStore({
  state() {
    return {
      user: null
    }
  },
  getters: {
    user(state): User | null {
      return state.user
    }
  },
  mutations: {
    SET_USER(state, data) {
      state.user = data;
    }
  },
  actions: {
    async register(context, { email, password, name }) {
      console.log(name)
      const response = await createUserWithEmailAndPassword(auth, email, password)
      if (response) {
        context.commit('SET_USER', response.user)
        await updateProfile(response.user, { displayName: name });
        await registerUserInDb(response.user);
      } else {
        throw new Error('Unable to register user')
      }
    },

    async signInWithGoogle(context) {
      try {
        const provider = new GoogleAuthProvider();
        const response = await signInWithPopup(auth, provider);
        if (response) {
          context.commit('SET_USER', response.user);
          // Optionally, update user profile here if needed
          if (getAdditionalUserInfo(response)?.isNewUser && auth.currentUser) {
            await registerUserInDb(auth.currentUser)
          }
        } else {
          throw new Error('Unable to sign in with Google');
        }
      } catch (error) {
        throw new Error('Unable to sign in with Google');
      }
    },

    async logIn(context, { email, password }) {
      const response = await signInWithEmailAndPassword(auth, email, password)
      console.log(response)
      if (response) {
        context.commit('SET_USER', response.user)
        console.log(auth.currentUser)
        console.log("Login Successful")
      } else {
        throw new Error('Login failed')
      }
    },

    async logOut(context) {
      await signOut(auth)
      context.commit('SET_USER', null)
    },
    async sendResetEmail(context, { email }) {
      await sendPasswordResetEmail(auth, email)
    }
  }
})

// export the store
export default store