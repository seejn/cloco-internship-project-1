import { createApp } from 'vue'

import './style.css'
import App from './App.vue'
import store from './store/store.js'
import router from './router.js'
// import mixin from './plugins/mixin.js'


import Toasts from './components/toasts/Toasts.vue'



const app = createApp(App)
app.use(store)
app.use(router)
// app.use(mixin)
app.component("Toasts", Toasts)
app.mount('#app')
