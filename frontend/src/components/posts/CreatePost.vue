<template>
    <div class="max-w-4xl mx-auto bg-white p-8 rounded-lg shadow-md">
        <h2 class="text-2xl font-bold text-gray-800 mb-6">Create New Post</h2>
        <form action="#" method="POST">

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="title">
                    Post Title
                </label>
                <input class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="text" id="title" name="title" placeholder="Enter your post title">
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="content">
                    Post Content
                </label>
                <textarea class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" id="content" name="content" rows="10" placeholder="Write your post content here..."></textarea>
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