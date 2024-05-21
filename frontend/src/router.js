import { createWebHistory, createRouter } from 'vue-router'

import SignOut from './components/user/SignOut.vue'

import LandingPage from './pages/LandingPage.vue'
import Dashboard from './pages/Dashboard.vue'
import SignIn from './pages/SignIn.vue'
import SignUp from './pages/SignUp.vue'
import CreatePost from './pages/CreatePost.vue'
import ProfilePage from './pages/ProfilePage.vue'
import FullViewPost from './components/posts/FullViewPost.vue'

const routes = [
    { path: '/', component: LandingPage },
    { path: '/signin', component: SignIn },
    { path: '/signup', component: SignUp },
    { path: '/signout', component: SignOut },
    { path: '/dashboard', component: Dashboard },
    { path: '/create-post', component: CreatePost },
    { path: '/profile', component: ProfilePage },

    { path: '/post/:postId', component: FullViewPost}
]

export default createRouter({
    history: createWebHistory(),
    routes: routes,
 })