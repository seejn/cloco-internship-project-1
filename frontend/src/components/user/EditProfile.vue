<template>
    <div class="max-w-3xl mx-auto bg-white p-8 rounded-lg ">
        <h2 class="text-2xl font-bold text-gray-800 mb-6">Edit Profile</h2>
        <form @submit.prevent="saveChanges">
          
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
                    First Name
                </label>
                <input v-model="updatedUser.first_name" class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="text" id="name" >
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
                    Last Name
                </label>
                <input v-model="updatedUser.last_name" class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="text" id="name" >
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
                    Username
                </label>
                <input v-model="updatedUser.username" class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="text" id="name" >
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                    Email
                </label>
                <input v-model="updatedUser.email" class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="email" id="email" >
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
                    Contact
                </label>
                <input v-model="updatedUser.contact" class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="text" id="name" >
            </div>

            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
                    Address
                </label>
                <input v-model="updatedUser.address" class="w-full p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500" type="text" id="name" >
            </div>

            <div class="mb-6">
                <button class="w-full px-4 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500" type="submit">
                    Save Changes
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
                updatedUser: {
                    first_name: null,
                    last_name: null,
                    username: null,
                    contact: null,
                    address: null,
                    email: null,
                }
            }
        },
        methods: {
            seperateFullname(fullname) {
                this.updatedUser.first_name = fullname.split(" ")[0]
                this.updatedUser.last_name = fullname.split(" ")[1]
            },
            setUserInfo() {
                this.updatedUser.username = this.user.username
                this.updatedUser.contact = this.user.contact
                this.updatedUser.address = this.user.address
                this.updatedUser.email = this.user.email
            },
            async saveChanges() {
                await axios(`${import.meta.env.VITE_BASE_URL}/user/update/`, {
                    method: 'PATCH',
                    headers: {
                        'Authorization': `Bearer ${import.meta.env.VITE_AUTH_TOKEN}`
                    },
                    data: this.updatedUser
                })
                .then((response) => {
                    console.log(response.data)
                    this.$store.commit("addToast", {
                        title: response.statusText,
                        isError: false,
                        message: response.data.message
                    })
                    this.$store.commit("setUser", response.data.data)
                    this.$emit("handleSubmit")
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
        computed: {
            user() {
                return this.$store.state.user
            }
        },
        mounted() {
            this.seperateFullname(this.user.fullname)
            this.setUserInfo()
        }
    }
</script>