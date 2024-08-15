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

export async function checkServerHealth(): Promise<boolean> {
    const path = (import.meta.env.VITE_DB_URL + '/health')
    var serverDown = false
    try {
        await axios.get(path).then((response) => {
            serverDown = response.data
        })
    } catch {
        serverDown = true
    }
    return serverDown
}

export async function getAllApplications(): Promise<any> {
    const path = (import.meta.env.VITE_DB_URL + '/applications')
    axios.get(path).then((response) => {
        return response.data["applications"]
    }).catch((e) => {
        console.log(e)
    })
}