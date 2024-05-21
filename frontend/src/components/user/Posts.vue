<template>
    <div class="cards-collection py-4">
        <span v-for="post in posts">
            <Card :post="post" />
        </span>
    </div>
</template>
<script>
    import axios from 'axios'
    import Card from '../posts/Card.vue'

    export default {
        props: {
            user: {
                type: Object,
                required: true
            }
        },
        components: {
            Card
        },
        data() {
            return {
                posts: {
                },
            }
        },
        methods: {
            addUserToPosts() {
                console.log("Add user to posts: ", this.posts)
                this.posts.user = this.user
            },
            async getPost() {
                await axios(`${import.meta.env.VITE_BASE_URL}/user/${this.user.id}/get_posts/`,{
                    method: 'get',
                })
                .then((response) => {
                    this.posts = response.data.data
                })
                .catch((error) => {
                    this.$store.commit("addToast", {
                        title: error.response.statusText,
                        isError: true,
                        message: error.response.data.message
                    })
                })
            }
        },
        mounted() {
            this.getPost()
        }
    }
</script>