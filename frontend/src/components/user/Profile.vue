<template>
    <div class="max-w-5xl mx-auto p-4">
        <div class="bg-white shadow rounded-lg p-6">
            <div class="flex items-center space-x-6 relative">
                <img class="h-24 w-24 rounded-full object-cover" src="https://via.placeholder.com/150" alt="Profile Picture">
                <div>
                    <h2 class="text-2xl font-semibold text-gray-900">{{ user.fullname }}</h2>
                    <p class="text-gray-600">@{{ user.username || "username"}} </p>
                    <!-- <button class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg shadow">Follow</button> -->
                </div>
                <button @click="deleteAccount" class="absolute top-6 right-6 bg-red-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Delete Account</button>
            </div>
        </div>

        <div class="mt-6">
            <div class="bg-white shadow rounded-lg">
                <div class="flex items-center border-b border-gray-200 px-6 py-4">
                    <button 
                    @click="changeComponent('Information')"
                    :class="{'active': stateComponents.information.state}"
                    class="px-4 py-2">
                        Profile
                    </button>

                    <button
                    @click="changeComponent('Posts')"
                    :class="{'active': stateComponents.posts.state}"
                    class="text-gray-600 px-4 py-2">
                        Posts
                    </button>
                </div>
                <div class="p-6 relative">
                    <span v-if="!stateComponents.editProfile.state">
                        <button @click="changeComponent('editProfile')" class="absolute top-6 right-6 bg-indigo-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Edit Profile</button>
                    </span>
                    <span v-else="!stateComponents.editProfile.state">
                        <button @click="changeComponent('Information')" class="absolute top-6 right-6 bg-red-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Close</button>
                    </span>

                    <span v-if="stateComponents.information.state">
                        <Information :user="user" />
                    </span>
                    <span v-else-if="stateComponents.editProfile.state">
                        <EditProfile @handleSubmit="changeComponent('Information')" />
                    </span>
                    <span v-else="stateComponents.posts.state">
                        <Posts :user="user"/>
                    </span>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import Posts from './Posts.vue'
    import Information from './Information.vue'
    import EditProfile from './EditProfile.vue';
    
    export default {
        
        components: {
            Information,
            Posts,
            EditProfile
        },
        data() {
            return {
                // userId: this.$route.param.userId,
                // user: null,
                currentComponent: Information,
                stateComponents: {
                    information: {
                        name: "Information",
                        state: true
                    },
                    posts: {
                        name: "Posts",
                        state: false
                    },
                    editProfile: {
                        name: "editProfile",
                        state: false
                    },
                }

            }
        },
        computed: {
            user() {
                return this.$store.state.user
            }
        },
        methods: {
            changeComponent(component) {
                for(const comp in this.stateComponents){
                    if(this.stateComponents[comp].name === component){
                        this.stateComponents[comp].state = true
                    }else{
                        this.stateComponents[comp].state = false
                    }
                }
            },    
        },
    }
</script>
<style scoped>
    button.active{
        color: rgb(37 99 235);
    }
</style>