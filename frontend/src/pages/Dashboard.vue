<template>
    <Toasts />
    <UserNavBar />

    <div class="cards-collection py-4">
        <span v-for="post in posts">
            <Card :post="post" />
        </span>
    </div>
</template>

<script>

    import axios from 'axios'
    import UserNavBar from '../components/Navbar/UserNavBar.vue';
    import Card from '../components/posts/Card.vue';
    
    export default {
        components: {
            UserNavBar,
            Card,
        },
        data() {
            return {
                user: this.$store.state.user,
                posts: "",
            }
        },
        methods: {
            async getPosts() {
                await axios(`${import.meta.env.VITE_BASE_URL}/posts/get_all_posts/`, {
                    method: 'get',
                    withCredentials: true
                })
                .then((response) => {
                    this.$store.commit("setPosts",response.data.data)
                    this.posts = response.data.data
                    console.log("response",response)
                })
                .catch((error) => {
                    console.log(error)
                    if(
                        error.response.status === 400 ||
                        error.response.status === 401
                    ){
                        this.$store.commit('addToast', {
                            title: error.response.statusText,
                            isError: true,
                            message: error.response.data.message
                        });
                        this.$router.push("/signin")
                    }
                })
            }
        },
        mounted() {
            this.getPosts()
        }
    }
</script>