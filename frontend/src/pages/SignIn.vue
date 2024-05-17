<template>
    <Toasts />
    <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm">
            <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
        </div>

        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
            <form class="space-y-6" @submit.prevent="signIn">
            <div>
                <label :class="{'text-red-600': !emailState.state}" for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                <div class="mt-2">
                <input @blur="isEmailFieldValid" :class="{'ring-red-600': !emailState.state}" v-model="input.email" id="email" name="email" type="email" autocomplete="email" required class="block w-full rounded-md border-0 px-1 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                <span v-if="!emailState.state">
                    <p class="text-red-600">{{ emailState.message }}</p>
                </span>
                </div>
            </div>

            <div>
                <div class="flex items-center justify-between">
                <label :class="{'text-red-600': !passwordState.state}" for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                <div class="text-sm">
                    <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
                </div>
                </div>
                <div class="mt-2">
                <input @blur="isPasswordFieldValid" :class="{'ring-red-600': !passwordState.state}" v-model="input.password" id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 px-1 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                <span v-if="!passwordState.state">
                    <p class="text-red-600">{{ passwordState.message }}</p>
                </span>
                </div>
            </div>

            <div>
                <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
            </div>
            </form>

            <p class="mt-10 text-center text-sm text-gray-500">
            Not a member?
            <RouterLink to="/signup" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Create Account</RouterLink>
            </p>
            
            <p class="mt-10 text-center text-sm text-gray-500">
            <RouterLink to="/" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Go back</RouterLink>
            </p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        components: {
        },
        data() {
            return {
                input: {
                    email: '',
                    password: '',
                },
                emailState: {
                    message: 'email message',
                    state: true,
                },
                passwordState: {
                    message: 'password message',
                    state: true,
                },
            }
        },
        methods: {
            alertToast(title, isError, message) {
                this.$store.commit("addToast", {
                    title: title,
                    isError: isError,
                    message: message
                })
            },
            isEmailFieldValid() {
                if(this.input.email === ""){
                    this.emailState.state = false
                    this.emailState.message = "This field is required"
                    return false
                }

                const emailregex = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/g
                if(!emailregex.test(this.input.email)){
                    this.emailState.state = false
                    this.emailState.message = "Email not valid"
                    return false
                }
                this.emailState.state = true
                return true
            },
            isPasswordFieldValid() {
                if(this.input.password === ""){
                    this.passwordState.state = false
                    this.passwordState.message = "This field is required"
                    return false
                }

                this.passwordState.state = true
                return true
            },
            resetFields() {
                this.input.email = ''
                this.input.password = ''
            },
            async signIn() {
                if( !this.isEmailFieldValid()) return

                if( !this.isPasswordFieldValid()) return

                await axios(`${import.meta.env.VITE_BASE_URL}/authenticate/user/`,{
                    method: 'post',
                    withCredentials: true,
                    headers: {
                        "Content-Type": "application/json"
                    },
                    data: {
                        "email": this.input.email,
                        "password": this.input.password,
                    }
                })
                .then((response) => {
                    console.log(response)
                    this.$store.commit("addUser", response.data.data)
                    this.$store.commit("addToast", {
                        title: "Login Success",
                        isError: false,
                        message: "You've successfully logged in"
                    })
                    this.$router.push('/dashboard')
                })
                .catch((error) => {
                    this.resetFields()
                    this.$store.commit("addToast", {
                        title: error.response.statusText,
                        isError: true,
                        message: error.response.data.message,
                    })
                    // this.alertToast(
                    //     error.response.statusText,
                    //     true,
                    //     error.response.data.message
                    // )
                })
            }
        }, 
        mounted() {
        }
    }
</script>