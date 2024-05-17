<template>
    <UserNavBar />
    <ProfileComponent />
</template>

<script>
    import UserNavBar from '../components/Navbar/UserNavBar.vue'
    import ProfileComponent from '../components/user/Profile.vue'

    export default {
        components: {
            UserNavBar,
            ProfileComponent,
        }
    }
</script>