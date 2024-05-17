<template>
    <UserNavBar />
    <CreatePostComponent />   
    createpost 
</template>

<script>
    import CreatePostComponent from '../components/posts/CreatePost.vue'
    import UserNavBar from '../components/Navbar/UserNavBar.vue'

    export default {
        components: {
            CreatePostComponent,
            UserNavBar,
        }
    }
</script>