<template>
    <div class="max-w-3xl mx-auto bg-white p-8 rounded-lg shadow-md">
        <h2 class="text-2xl font-bold text-gray-800 mb-6">Edit Profile</h2>
        <form action="#" method="POST">
          
            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="profilePicture">
                    Profile Picture
                </label>
                <div class="flex items-center">
                    <img class="w-16 h-16 rounded-full object-cover mr-4" src="https://via.placeholder.com/150" alt="Profile Picture">
                    <input class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100" type="file" id="profilePicture" name="profilePicture">
                </div>
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
                    Name
                </label>
                <input class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="text" id="name" name="name" value="John Doe">
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                    Email
                </label>
                <input class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="email" id="email" name="email" value="john.doe@example.com">
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="bio">
                    Bio
                </label>
                <textarea class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" id="bio" name="bio" rows="4" placeholder="Tell us a little about yourself...">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel urna nec risus ultricies dictum non nec nulla.</textarea>
            </div>

            <div class="mb-6">
                <button class="w-full px-4 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500" type="submit">
                    Save Changes
                </button>
            </div>
            
        </form>
    </div>

</template>