<template>
  <div>
    <router-view></router-view>
    <!-- <CreatePost /> -->
  </div>
</template>

<script>

  import Card from './components/posts/Card.vue'
  import Comment from './components/posts/Comment.vue'
  import FullViewPost from './components/posts/FullViewPost.vue'
  import CreatePost from './components/posts/CreatePost.vue'

  import Profile from './components/user/Profile.vue'
  import EditProfile from './components/user/EditProfile.vue'
  import SignIn from './pages/SignIn.vue'
  import SignUp from './pages/SignUp.vue'
  import Alert from './components/Alert.vue'
  
  import Navbar from './components/Navbar/NavBar.vue'
  import UserNavbar from './components/Navbar/UserNavBar.vue'
  
  export default {
    components: {

      Navbar,
      UserNavbar,
      
      Card,
      Comment,
      FullViewPost,
      CreatePost,

      Profile,
      SignUp,
      EditProfile,
      SignIn,
      Alert,

    },
    computed: {
      isUserLoggedIn() {
        // return this.$store.
      }
    }
  }
</script>

<style scoped>

</style>
