import axios from 'axios';
import type { User } from 'firebase/auth';

export async function registerUserInDb(user: User, password: string = '', user_id = '') {
    const path = (import.meta.env.VITE_DB_URL + '/user')
    const payload = {
        'user_id': user_id,
        'name': user.displayName,
        'email': user.email,
        'password': password
    }
    axios.post(path, payload).then((response) => {
        console.log(response)
    }).catch((e) => {
        console.log(e)
    })
}

export async function GetUser(user_id: string) {
    const path = (import.meta.env.VITE_DB_URL + '/user?user_id=' + user_id)
    axios.get(path).then((response) => {
        console.log(response)
    }).catch((e) => {
        console.log(e)
    })
}

export async function UpdateUser(user_id: string, name: string, email: string) {
    const path = (import.meta.env.VITE_DB_URL + '/user')
    const payload = {
        'user_id': user_id,
        'name': name,
        'email': email
    }
    axios.put(path, payload).then((response) => {
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