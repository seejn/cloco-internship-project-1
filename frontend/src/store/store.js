import { createStore } from 'vuex'

export default createStore({
    state: {
        user: {},
        posts: [],


        toasts: []
    },
    mutations: {
        addUser(state, user) {
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
    }
})