<template>
    <nav class="bg-gray-800">
        <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div class="relative flex h-16 items-center justify-between">
                <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
                    <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                    </svg>
                </div>
                <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
                    <div class="flex flex-shrink-0 items-center">
                    <!-- <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company"> -->
                    </div>
                    <div class="hidden sm:ml-6 sm:block">
                    <div class="flex space-x-4">
                        <a href="#" class="bg-gray-900 text-white rounded-md px-3 py-2 text-sm font-medium" aria-current="page">Dashboard</a>
                    </div>
                    </div>
                </div>
                <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
                    <RouterLink to="/signin" class="bg-indigo-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Sign In</RouterLink>
                </div>
            </div>
        </div>

    </nav>
</template>

<script>
    export default {
        data() {
            return {
                profileIcon: true
            }
        },
        methods: {
            toggleMenu() {
                this.profileIcon = !this.profileIcon
            }
        },
        computed: {
            menuToggleClassObject() {
                return{
                    "hidden": this.profileIcon
                }
            }
        }
    }
</script>

<style></style>