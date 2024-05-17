<template>
    <Toasts />
    <div class="max-w-5xl mx-auto p-4">
        <div class="bg-white shadow rounded-lg p-6">
            <div class="flex items-center space-x-6">
                <img class="h-24 w-24 rounded-full object-cover" src="https://via.placeholder.com/150" alt="Profile Picture">
                <div>
                    <h2 class="text-2xl font-semibold text-gray-900">{{ user.firstname || "John"}} {{ user.lastname || "Doe" }} </h2>
                    <p class="text-gray-600">@{{ user.username || "username"}} </p>
                    <p class="text-gray-600">{{ user.email }}</p>
                    <button class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg shadow">Follow</button>
                </div>
            </div>
        </div>

        <div class="mt-6">
            <div class="bg-white shadow rounded-lg">
                <div class="flex items-center border-b border-gray-200 px-6 py-4">
                    <a href="#" class="text-blue-600 px-4 py-2">Profile</a>
                    <a href="#" class="text-gray-600 px-4 py-2">Posts</a>
                    <a href="#" class="text-gray-600 px-4 py-2">Friends</a>
                    <a href="#" class="text-gray-600 px-4 py-2">Photos</a>
                </div>
                <div class="p-6">
                    <h3 class="text-lg font-semibold text-gray-900">About</h3>
                    <p class="text-gray-600 mt-2">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel sapien felis. Mauris nec quam vitae tortor gravida faucibus.</p>
                    
                    <h3 class="text-lg font-semibold text-gray-900 mt-6">Interests</h3>
                    <ul class="list-disc list-inside text-gray-600 mt-2">
                        <li>Programming</li>
                        <li>Music</li>
                        <li>Traveling</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import axios from 'axios'

    export default {
        components: {
        },
        data() {
            return {
                user: {}
            }
        },
        methods: {
            async fetchUser() {
                
                await axios(`${import.meta.env.VITE_BASE_URL}/authenticate/user/`,{
                    method: 'post',
                    withCredentials: true
                })
                .then((response) => {
                    // this.$store.commit("addToast", {
                    //     title: "Your Profile",
                    //     isError: false,
                    //     message: "This is what others will see. "
                    // })
                    console.log(response.data.data)
                    this.user = response.data.data
                })
                .catch((error) => {
                    if(error.response.status === 401){
                        this.$router.push('/')
                    }
                    
                    this.$store.commit("addToast", {
                        title: error.response.statusText,
                        isError: true,
                        message: error.response.data.message || "Something went wrong"
                    })
                })
            },
        },
        mounted() {
            this.fetchUser()
        }
    }
</script>