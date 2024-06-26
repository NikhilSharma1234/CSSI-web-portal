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

export const CustomerService = {
  getData() {
      return [
          {
              id: 1007,
              name: 'James Butt',
              country: {
                  name: 'Algeria',
                  code: 'dz'
              },
              company: 'Benton, John B Jr',
              date: '2015-09-13',
              status: 'unqualified',
              verified: true,
              activity: 17,
              representative: {
                  name: 'Ioni Bowcher',
                  image: 'ionibowcher.png'
              },
              balance: 70663
          },
          {
            id: 1001,
            name: 'James Butt',
            country: {
                name: 'Algeria',
                code: 'dz'
            },
            company: 'Benton, John B Jr',
            date: '2015-09-13',
            status: 'unqualified',
            verified: true,
            activity: 17,
            representative: {
                name: 'Ioni Bowcher',
                image: 'ionibowcher.png'
            },
            balance: 70663
        },
        {
            id: 1002,
            name: 'James Butt',
            country: {
                name: 'Algeria',
                code: 'dz'
            },
            company: 'Benton, John B Jr',
            date: '2015-09-13',
            status: 'unqualified',
            verified: true,
            activity: 17,
            representative: {
                name: 'Crystal Mint',
                image: 'amyelsner.png'
            },
            balance: 70663
        },
        {
            id: 1003,
            name: 'James Butt',
            country: {
                name: 'Algeria',
                code: 'dz'
            },
            company: 'Benton, John B Jr',
            date: '2015-09-13',
            status: 'unqualified',
            verified: true,
            activity: 17,
            representative: {
                name: 'The Name',
                image: 'annafali.png'
            },
            balance: 70663
        },
        {
            id: 1004,
            name: 'Anna Jamie',
            country: {
                name: 'Algeria',
                code: 'dz'
            },
            company: 'Benton, John B Jr',
            date: '2015-09-13',
            status: 'unqualified',
            verified: true,
            activity: 17,
            representative: {
                name: 'Kaden Nesch',
                image: 'onyamalimba.png'
            },
            balance: 70663
        },
        {
            id: 1005,
            name: 'Michael Butt',
            country: {
                name: 'Algeria',
                code: 'dz'
            },
            company: 'Benton, John B Jr',
            date: '2015-09-13',
            status: 'unqualified',
            verified: true,
            activity: 17,
            representative: {
                name: 'Michael Rapaport',
                image: 'xuxuefeng.png'
            },
            balance: 70663
        },
        {
            id: 1006,
            name: 'Steward Butt',
            country: {
                name: 'Algeria',
                code: 'dz'
            },
            company: 'Benton, John B Jr',
            date: '2015-09-13',
            status: 'unqualified',
            verified: true,
            activity: 17,
            representative: {
                name: 'Kaden Nesch',
                image: 'onyamalimba.png'
            },
            balance: 70663
        },

      ];
  },

  getCustomersSmall() {
      return Promise.resolve(this.getData().slice(0, 10));
  },


};


// export the store
export default store