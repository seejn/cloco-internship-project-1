<template>
    <Toasts />
    <NavBar />
    <div class="cards-collection py-4">
        <span v-for="post in posts">
            <Card :post="post" />
        </span>
    </div>
</template>

<script>
    import axios from 'axios'

    import Card from '../components/posts/Card.vue'
    import NavBar from '../components/Navbar/NavBar.vue'

    export default {
        components: {
            NavBar,
            Card,
        },
        computed: {
            posts() {
                return this.$store.state.posts
            }
        },
        watch: {
            posts(newValue, oldValue) {
                console.log(`updating from ${oldValue} -> ${newValue}`)
            }
        },
        mounted() {
            this.$store.dispatch("fetchPosts")
        }
    }
</script>

<style>

</style>