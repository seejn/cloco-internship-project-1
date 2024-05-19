<template>
    <Toasts />
    <UserNavBar />
    <header class="bg-white shadow">
        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
            <h1 class="text-3xl font-bold text-gray-900">{{ post.title }}</h1>
        </div>
    </header>
    <main class="max-w-4xl mx-auto py-6 sm:px-6 lg:px-8">
        <div class="bg-white shadow rounded-lg overflow-hidden">
            <img class="w-full h-96 object-cover" src="https://via.placeholder.com/800x400" alt="Post Image">
            <div class="p-6">
                <div class="flex items-center mb-4">
                    <img class="w-12 h-12 rounded-full object-cover" src="https://via.placeholder.com/100" alt="Author Image">
                    <div class="ml-3">
                        <p class="text-gray-800 font-semibold">{{ postedBy.fullname }}</p>
                        <p class="text-gray-600 text-sm">{{ post.created_at }}</p>
                    </div>
                </div>
                <p class="text-gray-600 mb-4">{{ post.content }}</p>
            </div>
        </div>
    </main>
    
    <!-- <Comment /> -->

</template>

<script>
    import Comment from './Comment.vue'
    import axios from 'axios'
    import UserNavBar from '../Navbar/UserNavBar.vue'

    export default {
        components: {
            Comment,
            UserNavBar
        },
        data() {
            return {
                post_id: this.$route.params.post_id,
                post: {},
                postedBy: {}
            }
        },
        methods: {
            async getPost() {
                await axios(`${import.meta.env.VITE_BASE_URL}/post/${this.post_id}/`, {
                    method: "get",
                })
                .then((response) => {
                    this.post = response.data.data
                    this.postedBy = this.post.posted_by
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