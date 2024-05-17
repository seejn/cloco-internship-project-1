<script>
    import axios from 'axios'

    export default {
        methods: {
            redirectToRoot(title, message) {
                this.$store.commit("addToast", {
                        title: title,
                        isError: true,
                        message: message
                    })
                    this.$router.push("/")
            },
            async signOut() {
                await axios(`${import.meta.env.VITE_BASE_URL}/user/signout/`, {
                    method: 'get',
                    withCredentials: true
                })
                .then((response) => {
                    this.redirectToRoot(
                        response.statusText,
                        response.data.message,
                    )
                })
                .catch((error) => {
                    console.log(error.response)
                    this.redirectToRoot(
                        error.response.statusText,
                        error.response.data.message,
                    )
                })
            }
        },
        mounted() {
            this.signOut()
        }
    }
</script>