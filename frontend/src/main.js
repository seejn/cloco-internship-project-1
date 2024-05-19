import { createApp } from 'vue'
import { createWebHistory, createRouter } from 'vue-router'

import './style.css'
import App from './App.vue'
import store from './store/store.js'

import SignOut from './components/user/SignOut.vue'

import LandingPage from './pages/LandingPage.vue'
import Dashboard from './pages/Dashboard.vue'
import SignIn from './pages/SignIn.vue'
import SignUp from './pages/SignUp.vue'
import CreatePost from './pages/CreatePost.vue'
import Profile from './pages/Profile.vue'

import Toasts from './components/toasts/Toasts.vue'
import FullViewPost from './components/posts/FullViewPost.vue'

const routes = [
    { path: '/', component: LandingPage },
    { path: '/signin', component: SignIn },
    { path: '/signup', component: SignUp },
    { path: '/signout', component: SignOut },
    { path: '/dashboard', component: Dashboard },
    { path: '/create-post', component: CreatePost },
    { path: '/profile', component: Profile },

    { path: '/post/:post_id', component: FullViewPost}
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
 })

const app = createApp(App)
app.component("Toasts", Toasts)
app.use(router)
app.use(store)
app.mount('#app')
