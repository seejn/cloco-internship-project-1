<template>
    <Toasts />
    <div class="max-w-4xl mx-auto bg-white p-8 rounded-lg shadow-md">
        <h2 class="text-2xl font-bold text-gray-800 mb-6">Create New Post</h2>
        <form @submit.prevent="createPost">

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="title">
                    Post Title
                </label>
                <input @blur="isTitleValid" v-model="post.title" :class="{'ring-red-600': !titleValidState.state}" class="block w-full rounded-md border-0 px-1 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" type="text" id="title" name="title" placeholder="Enter your post title">
                <span v-if="!titleValidState.state">
                    <p class="text-red-600 text-sm">{{ titleValidState.message }}</p>
                </span>
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="content">
                    Post Content
                </label>
                <textarea @blur="isContentValid" v-model="post.content" :class="{'ring-red-600': !contentValidState.state}" class="block w-full rounded-md border-0 px-1 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" id="content" name="content" rows="10" placeholder="Write your post content here..."></textarea>
                <span v-if="!contentValidState.state">
                    <p class="text-red-600 text-sm">{{ contentValidState.message }}</p>
                </span>
            </div>
            
            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="postImage">
                    Post Image
                </label>
                <input class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100" type="file" id="postImage" name="postImage">
            </div>

            <div>
                <button class="w-full px-4 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500" type="submit">
                    Publish Post
                </button>
            </div>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                post: {
                    title: "",
                    content: "",
                },
                titleValidState: {
                    state: true,
                    message: ""
                },
                contentValidState: {
                    state: true,
                    message: ""
                },
            }
        },
        methods: {
            isTitleValid() {
                if (this.post.title === "") {
                    this.titleValidState.state = false
                    this.titleValidState.message = "This field is required"
                    return false
                }
                this.titleValidState.state = true
                return true
            },
            isContentValid() {
                if (this.post.content === "") {
                    this.contentValidState.state = false
                    this.contentValidState.message = "This field is required"
                    return false
                }
                this.contentValidState.state = true
                return true
            },
            async createPost() {
                if(!this.isTitleValid()) return
                if(!this.isContentValid()) return

                await axios(`${import.meta.env.VITE_BASE_URL}/posts/create_post/`, {
                    method: "post",
                    headers: {
                        "Authorization": `Bearer ${import.meta.env.VITE_AUTH_TOKEN}` 
                    },
                    data: {
                        title: this.post.title,
                        content: this.post.content,
                    }
                })
                .then((response) => {
                    this.$store.commit("addToast", {
                        title: response.statusText,
                        isError: false,
                        message: response.data.message
                    })
                    this.$router.push("/dashboard")
                })
                .catch((error) => {
                    this.$store.commit("addToast", {
                        title: error.response.statusText,
                        isError: true,
                        message: error.response.data.message
                    })
                })
            }
        }
    }
</script>