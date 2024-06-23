import axios from 'axios';
import type { User } from 'firebase/auth';

export async function registerUserInDb(user: User) {
    const path = (import.meta.env.VITE_DB_URL + '/user')
    const payload = {
        'name': user.displayName,
        'email': user.email
    }
    axios.post(path, payload).then((response) => {
        console.log(response)
    }).catch((e) => {
        console.log(e)
    })
}