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

export async function CreateApplication(user_id: string, app_id: string, app_name: string, description: string): Promise<any> {
    const path = (import.meta.env.VITE_DB_URL + '/application')
    const payload = {
        'user_id': user_id,
        'name': app_name,
        'app_id': app_id,
        'description': description
    }
    axios.post(path, payload).then((response) => {
        console.log(response)
    }).catch((e) => {
        console.log(e)
    })
}


export async function GetApplication(app_id: string) {
    const path = (import.meta.env.VITE_DB_URL + '/application?app_id=' + app_id)
    axios.get(path).then((response) => {
        console.log(response)
    }).catch((e) => {
        console.log(e)
    })
}

export async function ListApplications(user_id: string): Promise<any> {
    const path = (import.meta.env.VITE_DB_URL + '/applications?user_id=' + user_id)
    axios.get(path).then((response) => {
        console.log(response)
    }).catch((e) => {
        console.log(e)
    })
}