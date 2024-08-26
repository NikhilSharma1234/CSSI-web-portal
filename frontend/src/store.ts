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
    async register(context, { email, password, name, userId }) {
      try {
        const response = await createUserWithEmailAndPassword(auth, email, password);
        if (response) {
          context.commit('SET_USER', response.user);
          await updateProfile(response.user, { displayName: name });
          await registerUserInDb(response.user, password, userId);
        } else {
          throw new Error('Unable to register user');
        }
      } catch (error) {
        console.error('Registration error:', error);
        throw error;
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

export const OrganizationNames = {
  getData() {
      return [
          {
              ID: 'kaden-1',
              name: 'UNR Organization',
              description: 'The official organization of UNR.',
              collaborators: 8
          },
          {
              ID: 'michael-organization',
              name: 'Computer Science Organization',
              description: 'An organization for computer science enthusiasts.',
              collaborators: 12
          },
          {
              ID: 'organization-1',
              name: 'Engineering Group',
              description: 'A collaborative group for engineering projects.',
              collaborators: 10
          },
          {
              ID: 'kaden-2',
              name: 'Art Society',
              description: 'A society dedicated to the promotion of the arts.',
              collaborators: 5
          },
          {
              ID: 'michael-2',
              name: 'Science Club',
              description: 'A club for students interested in scientific research.',
              collaborators: 14
          },
          {
              ID: 'organization-2',
              name: 'Literature Circle',
              description: 'A circle for the discussion and appreciation of literature.',
              collaborators: 7
          },
          {
              ID: 'steward-group',
              name: 'Music Ensemble',
              description: 'A group for students interested in performing music.',
              collaborators: 11
          }
      ];
  },

  getOrganizationNamesSmall() {
      return Promise.resolve(this.getData().slice(0, 10));
  }
};

export const ApplicationNames = {
  getData() {
      return [
          {
              ID: 'sensor-hub-1',
              name: 'Temperature Monitoring System',
              'devices': 18
          },
          {
              ID: 'env-group-2',
              name: 'Environmental Sensors Network',
              'devices': 12
          },
          {
              ID: 'agriculture-3',
              name: 'Smart Agriculture Setup',
              'devices': 20
          },
          {
              ID: 'building-control-4',
              name: 'Building Automation Sensors',
              'devices': 7
          },
          {
              ID: 'health-monitor-5',
              name: 'Health Monitoring Devices',
              'devices': 15
          },
          {
              ID: 'weather-station-6',
              name: 'Weather Station System',
              'devices': 10
          },
          {
              ID: 'water-quality-7',
              name: 'Water Quality Monitoring',
              'devices': 14
          }
      ];
  },

  getApplicationNamesSmall() {
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