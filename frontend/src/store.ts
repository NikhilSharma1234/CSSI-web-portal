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



export const OrganizationList = {
  getData() {
      return [
          {
              name: 'James Butt',
              owner: { name: 'Ioni Bowcher' },
              role: { name: 'Member' }
          },
          {
              name: 'Sara Thomas',
              owner: { name: 'Anna Figueroa' },
              role: { name: 'Admin' }
          },
          {
              name: 'David Cameron',
              owner: { name: 'Crystal Mint' },
              role: { name: 'Member' }
          },
          {
              name: 'Laura May',
              owner: { name: 'Ashley Carter' },
              role: { name: 'Admin' }
          },
          {
              name: 'Anna Jamie',
              owner: { name: 'Kaden Nesch' },
              role: { name: 'Member' }
          },
          {
              name: 'Michael Lopez',
              owner: { name: 'Michael Rapaport' },
              role: { name: 'Admin' }
          },
          {
              name: 'Steward Douglas',
              owner: { name: 'Kaden Nesch' },
              role: { name: 'Member' }
          }
      ];
  },

  getOrganizationSmall() {
      return Promise.resolve(this.getData().slice(0, 10));
  }
};


export const SensorList = {
  getData() {
      return [
          { name: 'Sensor1', owner: { name: 'Kaden Nesch' } },
          { name: 'Sensor2', owner: { name: 'Michael George' } },
          { name: 'Sensor3', owner: { name: 'George Nesch' } },
          { name: 'Sensor4', owner: { name: 'Michael Nesch' } },
          { name: 'Sensor5', owner: { name: 'Kaden Nesch' } },
          { name: 'Sensor6', owner: { name: 'Michael George' } },
      ];
  },

  getSensorSmall() {
      return Promise.resolve(this.getData().slice(0, 10));
  }
};


// export the store
export default store