import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, updateProfile, GoogleAuthProvider, signInWithPopup } from 'firebase/auth';
import { createStore } from 'vuex'
import { auth } from './firebaseAuth';

const store = createStore({
    state() {
        return {
            user: {
                loggedIn: false,
                data: null
            }
        }
      },
      getters: {
        user(state){
          return state.user
        }
      },
      mutations: {
        SET_LOGGED_IN(state, value) {
          state.user.loggedIn = value;
        },
        SET_USER(state, data) {
          state.user.data = data;
        }
      },
      actions: {
        async register(context, { email, password, name}){
            console.log(name)
            const response = await createUserWithEmailAndPassword(auth, email, password)
            if (response) {
                context.commit('SET_USER', response.user)
                await updateProfile(response.user, {displayName: name});
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
            } else {
              throw new Error('Unable to sign in with Google');
            }
          } catch (error) {
            throw new Error('Unable to sign in with Google');
          }
        },
    
        async logIn(context, { email, password }){
          const response = await signInWithEmailAndPassword(auth, email, password)
          if (response) {
              context.commit('SET_USER', response.user)
          } else {
              throw new Error('Login failed')
          }
      },
  
      async logOut(context){
          await signOut(auth)
          context.commit('SET_USER', null)
      },
  
      async fetchUser(context ,user) {
        context.commit("SET_LOGGED_IN", user !== null);
        if (user) {
          context.commit("SET_USER", {
            displayName: user.displayName,
            email: user.email
          });
        } else {
          context.commit("SET_USER", null);
        }
    },
    

    }
})

// export the store
export default store