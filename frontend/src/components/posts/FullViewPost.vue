<template>

    <header class="bg-white shadow">
        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
            <h1 class="text-3xl font-bold text-gray-900">Blog Post Title</h1>
        </div>
    </header>
    <main class="max-w-4xl mx-auto py-6 sm:px-6 lg:px-8">
        <div class="bg-white shadow rounded-lg overflow-hidden">
            <img class="w-full h-96 object-cover" src="https://via.placeholder.com/800x400" alt="Post Image">
            <div class="p-6">
                <div class="flex items-center mb-4">
                    <img class="w-12 h-12 rounded-full object-cover" src="https://via.placeholder.com/100" alt="Author Image">
                    <div class="ml-3">
                        <p class="text-gray-800 font-semibold">John Doe</p>
                        <p class="text-gray-600 text-sm">May 16, 2024</p>
                    </div>
                </div>
                <p class="text-gray-600 mb-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel urna nec risus ultricies dictum non nec nulla. Suspendisse potenti. Quisque aliquet nulla id ipsum tempor, nec faucibus magna aliquam.</p>
                <p class="text-gray-600 mb-4">Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin ac dui dui. Praesent ac massa at ligula laoreet iaculis. Fusce suscipit, libero a molestie consequat, libero arcu vestibulum urna, at tempus risus elit vel urna.</p>
                <p class="text-gray-600 mb-4">Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse cursus faucibus finibus. Nunc ac pretium urna, a tincidunt dui.</p>
            </div>
        </div>
    </main>
    
    <Comment />

</template>

<script>
    import Comment from './Comment.vue'

    export default {
        components: {
            Comment
        }
    }
</script>