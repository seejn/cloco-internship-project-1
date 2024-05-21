<template>
    <Toasts />
    <nav class="bg-gray-800">
        <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div class="relative flex h-16 items-center justify-between">
            <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
                <div class="flex flex-shrink-0 items-center">
                <!-- <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company"> -->
                </div>
                <div class="hidden sm:ml-6 sm:block">
                <div class="flex space-x-4">
                    <RouterLink to="/dashboard" class="nav-menu hover:bg-gray-900 text-white rounded-md px-3 py-2 text-sm font-medium" >Dashboard</RouterLink>
                    <RouterLink to="/create-post" class="nav-menu hover:bg-gray-900 text-white rounded-md px-3 py-2 text-sm font-medium" >Create Post</RouterLink>
                </div>
                </div>
            </div>
            <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
                <!-- <button type="button" class="relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                <span class="absolute -inset-1.5"></span>
                <span class="sr-only">View notifications</span>
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
                </svg>
                </button> -->

                <div class="relative ml-3" @click="toggleMenu">
                <div>
                    <button type="button" class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                    <span class="absolute -inset-1.5"></span>
                    <span class="sr-only">Open user menu</span>
                    <img class="h-8 w-8 rounded-full" src="https://via.placeholder.com/150" alt="">
                    </button>
                </div>
                <div :class="menuToggleClassObject" class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                    <RouterLink to="/profile" class="block px-4 py-2 text-sm text-gray-700 hover:bg-zinc-300" role="menuitem" tabindex="-1" id="user-menu-item-0">Your Profile</RouterLink>
                    <RouterLink to="/dashboard" class="block px-4 py-2 text-sm text-gray-700 hover:bg-zinc-300" role="menuitem" tabindex="-1" id="user-menu-item-1">Settings</RouterLink>
                    <RouterLink to="/signout" class="block px-4 py-2 text-sm text-gray-700 hover:bg-zinc-300" role="menuitem" tabindex="-1" id="user-menu-item-2">Sign out</RouterLink>
                </div>
                </div>
            </div>
            </div>
        </div>

    </nav>
</template>

<script>
    import { RouterLink } from 'vue-router';

    export default {
        data() {
            return {
                profileIcon: true
            }
        },
        methods: {
            toggleMenu() {
                this.profileIcon = !this.profileIcon
            },
        },
        computed: {
            user() {
                return this.$store.state.user
            },
            menuToggleClassObject() {
                return{
                    "hidden": this.profileIcon
                }
            }
        },
        watch: {
            user(newValue, oldValue){
                console.log(`User Update from ${oldValue} to ${newValue}`)
            }
        },
        mounted() {
            if(!this.$store.state.user) this.$store.dispatch("fetchUser")
        }
    }
</script>

<style>
    .nav-menu.router-link-active{
        background-color: rgb(17 24 39);
    }
</style>