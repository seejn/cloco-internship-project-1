<template>
    <!-- <div class="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow">
        <div class="flex items-start space-x-4">
            <img class="w-12 h-12 rounded-full object-cover" src="https://via.placeholder.com/100" alt="Commenter Profile Picture">
            <div>
                <div class="flex items-center space-x-2">
                    <h3 class="text-gray-900 font-semibold">Jane Doe</h3>
                    <span class="text-gray-600 text-sm">2 hours ago</span>
                </div>
                <p class="text-gray-700 mt-2">This is a sample comment text. It provides feedback or discussion related to the content above.</p>
            </div>
        </div>
    </div> -->
    <div class="max-w-4xl mx-auto space-y-6">
        <div class="bg-white p-6 rounded-lg shadow">
            <h3 class="text-xl font-semibold text-gray-800">Comments</h3>

            <div class="mt-6">
                <div class="flex items-start space-x-4">
                    <img class="w-12 h-12 rounded-full object-cover" src="https://via.placeholder.com/100" alt="Commenter Profile Picture">
                    <div class="flex-1">
                        <div class="flex items-center space-x-2">
                            <h4 class="text-gray-900 font-semibold">Jane Doe</h4>
                            <span class="text-gray-600 text-sm">2 hours ago</span>
                        </div>
                        <p class="text-gray-700 mt-2">This is a sample comment text. It provides feedback or discussion related to the content above.</p>

                        <button class="mt-2 text-blue-600 hover:underline" onclick="toggleReplyForm(this)">Reply</button>

                        <div class="mt-4 space-y-4 pl-12">
                            <div class="flex items-start space-x-4">
                                <img class="w-10 h-10 rounded-full object-cover" src="https://via.placeholder.com/100" alt="Replier Profile Picture">
                                <div>
                                    <div class="flex items-center space-x-2">
                                        <h5 class="text-gray-900 font-semibold">John Smith</h5>
                                        <span class="text-gray-600 text-sm">1 hour ago</span>
                                    </div>
                                    <p class="text-gray-700 mt-2">This is a sample reply to the comment.</p>
                                </div>
                            </div>
                        </div>

                        <div class="mt-4 pl-12 hidden">
                            <textarea class="w-full border rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500" rows="2" placeholder="Write your reply..."></textarea>
                            <button class="mt-2 px-4 py-2 bg-blue-600 text-white rounded-lg shadow">Post Reply</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="mt-6">
                <h4 class="text-lg font-semibold text-gray-800">Post a Comment</h4>
                <textarea class="w-full border rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 mt-2" rows="4" placeholder="Write your comment..."></textarea>
                <button class="mt-2 px-4 py-2 bg-blue-600 text-white rounded-lg shadow">Post Comment</button>
            </div>
        </div>
    </div>
</template>