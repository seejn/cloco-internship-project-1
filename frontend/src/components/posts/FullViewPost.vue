<template>
    <Toasts />
    <span v-if="!isLoggedIn">
        <NavBar />
    </span>
    <span v-else="isLoggedIn">
        <UserNavBar />
    </span>
    <section v-if="!isEditing">
        <header class="bg-white shadow flex justify-between items-center">
            <div class="max-w-7xl  py-6 px-4 sm:px-6 lg:px-8">
                <h1 class="text-3xl font-bold text-gray-900">{{ post.title }}</h1>
            </div>
            <div v-if="isAdmin" class="sm:px-6 lg:px-8">
                <button @click="deletePost" class="bg-red-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Delete</button>
            </div>
        </header>
        <main class="max-w-4xl mx-auto py-6 sm:px-6 lg:px-8">
            <div class="bg-white shadow rounded-lg overflow-hidden">
                <img class="w-full h-96 object-cover" src="https://via.placeholder.com/800x400" alt="Post Image">
                <div class="p-6">
                    <div class="flex items-center mb-4">
                        <img class="w-12 h-12 rounded-full object-cover" src="https://via.placeholder.com/100" alt="Author Image">
                        <div class="flex justify-between w-full">
                            <div class="ml-3">
                                <p class="text-gray-800 font-semibold">{{ postedBy.fullname }}</p>
                                <p class="text-gray-600 text-sm">{{ post.created_at }}</p>
                            </div>
                            <div v-if="isAdmin">
                                <button @click="toggleEditing" class="bg-indigo-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Edit</button>
                            </div>
                        </div>
                    </div>
                    <p class="text-gray-600 mb-4">{{ post.content }}</p>
                </div>
            </div>
        </main>
    </section>
    <section v-else="isAdmin">

        <div class="max-w-4xl mx-auto my-5 bg-white p-8 rounded-lg shadow-md">
            <div class="flex justify-between">
                <h2 class="text-2xl font-bold text-gray-800 mb-6">Edit Post</h2>
                <div>
                    <button @click="toggleEditing" class="bg-red-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Close</button>
                </div>
            </div>
            <form action="#" method="POST">

                <div class="mb-6">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="title">
                        Post Title
                    </label>
                    <input v-model="updatedPost.title" class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="text" id="title" name="title" placeholder="Enter your post title" >
                </div>

                <div class="mb-6">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="content">
                        Post Content
                    </label>
                    <textarea v-model="updatedPost.title" class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" id="content" name="content" rows="10" placeholder="Write your post content here..."></textarea>
                </div>
                
                <div class="mb-6">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="postImage">
                        Post Image
                    </label>
                    <div class="flex items-center">
                        <img class="w-32 h-32 object-cover mr-4 rounded" src="https://via.placeholder.com/150" alt="Post Image">
                        <input class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100" type="file" id="postImage" name="postImage">
                    </div>
                </div>

                <div>
                    <button class="w-full px-4 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500" type="submit">
                        Save Changes
                    </button>
                </div>
            </form>
        </div>



    </section>
    
    <!-- <Comment /> -->

</template>

<script>
    import Comment from './Comment.vue'
    import axios from 'axios'
    import NavBar from '../Navbar/NavBar.vue'
    import UserNavBar from '../Navbar/UserNavBar.vue'

    export default {
        components: {
            Comment,
            NavBar,
            UserNavBar
        },
        data() {
            return {
                isLoggedIn: Boolean(this.$store.state.user),
                postId: this.$route.params.postId,
                post: {},
                updatedPost: {
                    title: null,
                    content: null
                },
                postedBy: {},
                isAdmin: null,
                isEditing: false
            }
        },
        methods: {
            async deletePost () {
                await axios(`${import.meta.env.VITE_BASE_URL}/post/${this.postId}/delete/`, {
                    method: 'delete',
                    headers: {
                        'Authorization': `Bearer ${import.meta.env.VITE_AUTH_TOKEN}`
                    }
                })
                .then((response) => {
                    console.log(response.data.data)
                    this.$store.commit("setPosts", response.data.data)
                    this.$store.commit("addToast", {
                        title: response.statusText,
                        isError: false,
                        message: response.data.message
                    })
                    this.$router.push('/dashboard')
                })
                .catch((error) => {
                    this.$store.commit("addToast", {
                        title: error.response.statusText,
                        isError: true,
                        message: error.response.data.message
                    })
                })
            },
            toggleEditing() {
                this.isEditing = !this.isEditing
            },
            async getPost() {
                await axios(`${import.meta.env.VITE_BASE_URL}/post/${this.postId}/`, {
                    method: "get",
                })
                .then((response) => {
                    this.post = response.data.data
                    this.updatedPost.title = this.post.title
                    this.updatedPost.content = this.post.content
                    this.postedBy = this.post.posted_by
                    this.isAdmin = (this.postedBy.id === this.$store.state.user.id)
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