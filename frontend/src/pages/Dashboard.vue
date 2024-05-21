<template>
    <Toasts />
    <UserNavBar />
    <div class="cards-collection py-4">
        <span v-for="post in posts">
            <Card :post="post" />
        </span>
    </div>
</template>

<script>

    import UserNavBar from '../components/Navbar/UserNavBar.vue';
    import Card from '../components/posts/Card.vue';
    
    export default {
        components: {
            UserNavBar,
            Card,
        },
        computed: {
            posts() {
                return this.$store.state.posts
            }
        },
        watch: {
            posts(newValue, oldValue) {
                console.log(`Inside Dashboard: Updating posts from ${oldValue} -> ${newValue}`)
            }
        },
        mounted() {
            if(!this.$store.state.posts) this.$store.dispatch("fetchPosts")
        }
    }
</script>