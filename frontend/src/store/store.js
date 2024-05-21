import { createStore } from 'vuex'
import axios from 'axios'

import router from '../router.js'

export default createStore({
    state: {
        user: null,
        posts: null,


        toasts: []
    },
    mutations: {
        setUser(state, user) {
            state.user = user
        },
        clearUser(state) {
            state.user = {}
        },


        setPosts(state, posts) {
            state.posts = posts
        },


        addToast(state, toast) {

            state.toasts.push({
                id: Math.random() * 1000,
                ...toast
            })
        },
        clearToast(state, toast) {
            const index = state.toasts.findIndex((t) => t.id === toast.id)
            state.toasts.splice(index, 1)
        }
    },
    actions: {

        async fetchUser(context) {
                
            await axios(`${import.meta.env.VITE_BASE_URL}/authenticate/user/`,{
                method: 'post',
                headers: {
                    "Authorization": `Bearer ${import.meta.env.VITE_AUTH_TOKEN}` 
                }
            })
            .then((response) => {
                console.log("Inside store fetchUser")
                console.log("before setting response user data to user store", context.state.user)
                context.commit("setUser", response.data.data)
                console.log("after setting reponse user data to user store", context.state.user)
                context.commit("addToast", {
                    title: response.statusText,
                    isError: false,
                    message: response.data.message
                })
                router.push('/dashboard')
            })
            .catch((error) => {
                router.push('/')
            })
        },
        async fetchPosts(context){
            await axios(`${import.meta.env.VITE_BASE_URL}/posts/get_all_posts/`, {
                method: 'get'
            })
            .then((response) => {
                console.log("Inside store fetchPosts")
                console.log("before setting response posts data to posts store", context.state.posts)
                context.commit("setPosts", response.data.data)
                console.log("after setting reponse posts data to posts store", context.state.posts)
            })
            .catch((error) => {
                console.log("error")
                context.commit("addToast", {
                    id: Math.random() * 1000,
                    title: error.response.statusText,
                    isError: true,
                    message: error.response.data.message || "Something went wrong"
                })
            })
        },
    }
})