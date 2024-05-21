<template>
    <div class="max-w-lg my-5 mx-auto bg-white rounded-lg shadow-md overflow-hidden">
        <img class="w-full h-48 object-cover" src="https://via.placeholder.com/400x300" alt="Blog Post Image">
        <div class="p-6">
            <h2 class="text-2xl font-bold text-gray-800">{{ post.title }}</h2>
            <p class="mt-2 text-gray-600">
                {{ post.content }}
            </p>
            <div class="mt-4 flex items-center">
                <img class="w-10 h-10 rounded-full object-cover" src="https://via.placeholder.com/100" alt="Author Image">
                <div class="ml-3">
                    <p class="text-gray-800 font-semibold">{{ post.user.fullname }}</p>
                    <p class="text-gray-600 text-sm">{{ new Date(post.created_at).toLocaleString() }}</p>
                </div>
            </div>
            <div class="mt-4">
                <RouterLink :to="'/post/' + post.id" class="text-blue-600 hover:underline">Read more</RouterLink>
            </div>
        </div>
        <!-- <Comment /> -->
    </div>

</template>

<script>
    import Comment from './Comment.vue'

    export default {
        components: {
            Comment
        },
        props: {
            post: Object
        },
    }
</script>

<style>

</style>