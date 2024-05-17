<template>
    <Toasts />
    <NavBar />
    <!-- <p class="text-red-500 p-5 font-black text-5xl">Landing Page</p> -->
    <div class="cards-collection py-4">
        <span v-for="post in posts">
            <Card :post="post" />
        </span>
    </div>
</template>

<script>
    import axios from 'axios'

    import Card from '../components/posts/Card.vue'
    import NavBar from '../components/Navbar/NavBar.vue'

    export default {
        components: {
            NavBar,
            Card,
        },
        data() {
            return {
                posts: [],
            }
        },
        methods: {
            async fetchPosts(){
                await axios(`${import.meta.env.VITE_BASE_URL}/posts/get_all_posts/`, {
                    method: 'get'
                })
                .then((response) => {
                    this.posts = response.data.data
                    this.$store.setPosts(this.posts)
                    console.log(this.posts)
                })
                .catch((error) => {
                    this.$store.commit("addToast", {
                        id: Math.random() * 1000,
                        title: error.response.statusText,
                        isError: true,
                        message: error.response.data.message || "Something went wrong"
                    })
                })
            },
            async fetchUser() {
                
                await axios(`${import.meta.env.VITE_BASE_URL}/authenticate/user/`,{
                    method: 'post',
                    withCredentials: true
                })
                .then((response) => {
                    this.$store.commit("addToast", {
                        title: response.statusStatus,
                        isError: false,
                        message: response.data.message
                    })
                    this.$router.push('/dashboard')
                })
                .catch((error) => {
                    this.fetchPosts()
                })
            }
        },
        mounted() {
            this.fetchUser()
        }
    }
</script>

<style>

</style>